from flask import Flask, render_template, url_for, redirect, flash, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LogIn,SignUp,TaskForm
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv
import os

load_dotenv('.env')

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DB_URI')
db.init_app(app)


login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


bootstrap=Bootstrap5(app)


class User(db.Model,UserMixin):
    __tablename__='user_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=False  ,nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    tasks: Mapped[list['Task']] = relationship(back_populates='user')

class Task(db.Model):
    __tablename__='task_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(nullable=False,unique=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'), nullable=False)
    complete: Mapped[bool] = mapped_column(nullable=False)
    user: Mapped[User] = relationship(back_populates='tasks')


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


all_task=[]
@app.route('/',methods=['GET','POST'])
def home():
    global all_task
    form=TaskForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            new_task=Task(task=form.task.data,
                      user_id=current_user.id,
                      complete=False,
                      )
            db.session.add(new_task)
            db.session.commit()
        else:
            all_task.append(form.task.data)


    logged_in=False
    if current_user.is_authenticated:
        logged_in=True
        all_task=db.session.execute(db.select(Task).where(Task.user_id==current_user.id)).scalars().all()

    if current_user.is_authenticated and request.args.get('logout')=='True':
        logout_user()
        all_task=[]
        return redirect(url_for('home'))
    return render_template('index.html',logged_in=logged_in,form=form,all_task=all_task)



@app.route('/login',methods=['GET','POST'])
def login():
    form=LogIn()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        user = db.session.execute(db.select(User).where(User.email==email)).scalar_one_or_none()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid Credentials. Please try again.')

    return render_template('login.html',form=form)



@app.route('/signup',methods=['GET','POST'])
def signup():
    form=SignUp()
    if form.validate_on_submit():
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256',
                salt_length=8
            )
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('User already exists.')
            return redirect(url_for('signup'))

        except Exception as e:
            print(e)
            db.session.rollback()
            flash('Something went wrong.')
            return redirect(url_for('signup'))

        return redirect(url_for('login'))

    return render_template('signup.html',form=form)


@app.route('/delete/<task_id>')
def delete_task(task_id):
    if current_user.is_authenticated:
        task_to_delete=db.session.execute(db.select(Task).where(Task.id==int(task_id))).scalar()
        db.session.delete(task_to_delete)
        db.session.commit()
    else:
        all_task.pop(all_task.index(task_id))
    return redirect(url_for('home'))


@app.route('/toggle_task/<task_id>',methods=['GET','POST'])
def toggle_task(task_id):
    if current_user.is_authenticated:
        task_to_change=db.session.execute(db.select(Task).where(Task.id==int(task_id))).scalar()
        task_to_change.complete=not task_to_change.complete
        db.session.commit()
    else:
        pass
    return redirect(url_for('home'))



if __name__=='__main__':
    app.run(debug=True)