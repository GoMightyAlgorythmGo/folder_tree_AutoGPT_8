document.addEventListener('DOMContentLoaded', function () {
    let folders = document.querySelectorAll('.folder');
    
    folders.forEach(folder => {
        folder.addEventListener('click', function () {
            let subTree = this.nextElementSibling;
            subTree.classList.toggle('visible');
        });
    });
});