document.addEventListener('DOMContentLoaded', () => {

    // ========================
    // Checkbox Logic
    // ========================

    document.querySelectorAll('.check-task').forEach(checkbox => {

        if (checkbox.dataset.completed === "True") {
            checkbox.checked = true;
            const taskText = checkbox.closest('li').querySelector('.task-text');
            taskText.classList.add('task-completed');
        }

        checkbox.addEventListener('change', (e) => {
            const taskText = e.target.closest('li').querySelector('.task-text');
            taskText.classList.toggle('task-completed', e.target.checked);

            const taskId = e.target.dataset.id;

            fetch(`/toggle_task/${taskId}`, {
                method: 'POST'
            });
        });
    });

    // ========================
    // Side Menu Logic
    // ========================

    const menu = document.getElementById("sideMenu");
    const overlay = document.getElementById("overlay");
    const openBtn = document.getElementById("menuToggle");
    const closeBtn = document.getElementById("closeMenu");

    openBtn.addEventListener("click", () => {
        menu.classList.add("active");
        overlay.classList.add("active");
    });

    closeBtn.addEventListener("click", () => {
        menu.classList.remove("active");
        overlay.classList.remove("active");
    });

    overlay.addEventListener("click", () => {
        menu.classList.remove("active");
        overlay.classList.remove("active");
    });

});
