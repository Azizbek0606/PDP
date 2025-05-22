document.addEventListener('DOMContentLoaded', function () {
    // Sidebar toggle functionality
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const toggle = document.getElementById("themeToggle");

    sidebarToggle.addEventListener('click', function () {
        sidebar.classList.toggle('collapsed');
        mainContent.classList.toggle('expanded');

        // Store state in localStorage
        const isCollapsed = sidebar.classList.contains('collapsed');
        localStorage.setItem('sidebarCollapsed', isCollapsed);
    });

    // Check for saved state
    if (localStorage.getItem('sidebarCollapsed') === 'true') {
        sidebar.classList.add('collapsed');
        mainContent.classList.add('expanded');
    }

    // Submenu toggle functionality
    const menuItemsWithSubmenu = document.querySelectorAll('.sidebar-menu li:has(.submenu)');

    menuItemsWithSubmenu.forEach(item => {
        const link = item.querySelector('a');
        const submenu = item.querySelector('.submenu');

        link.addEventListener('click', function (e) {
            // Don't toggle if we're clicking on a submenu link
            if (e.target.tagName === 'A' && e.target.parentElement.tagName === 'LI') {
                return;
            }

            // Close other open submenus first
            if (!submenu.style.maxHeight || submenu.style.maxHeight === '0px') {
                closeAllSubmenus();
            }

            // Toggle current submenu
            if (submenu.style.maxHeight) {
                submenu.style.maxHeight = null;
                item.classList.remove('active');
            } else {
                submenu.style.maxHeight = submenu.scrollHeight + 'px';
                item.classList.add('active');
            }

            e.preventDefault();
        });
    });

    function closeAllSubmenus() {
        document.querySelectorAll('.submenu').forEach(submenu => {
            submenu.style.maxHeight = null;
        });
        document.querySelectorAll('.sidebar-menu li').forEach(item => {
            item.classList.remove('active');
        });
    }

    // Mobile menu toggle
    function handleMobileMenu() {
        if (window.innerWidth <= 768) {
            sidebar.classList.add('collapsed');
            mainContent.classList.add('expanded');
        } else {
            // Restore desktop state from localStorage
            if (localStorage.getItem('sidebarCollapsed') === 'true') {
                sidebar.classList.add('collapsed');
                mainContent.classList.add('expanded');
            } else {
                sidebar.classList.remove('collapsed');
                mainContent.classList.remove('expanded');
            }
        }
    }

    // Initial check
    handleMobileMenu();

    // Add resize listener
    window.addEventListener('resize', handleMobileMenu);

    // Active menu item highlighting
    const menuItems = document.querySelectorAll('.sidebar-menu li:not(:has(.submenu)) a');

    menuItems.forEach(item => {
        item.addEventListener('click', function () {
            menuItems.forEach(i => i.parentElement.classList.remove('active'));
            this.parentElement.classList.add('active');
        });
    });

    // Simulate loading content when menu items are clicked
    const allMenuLinks = document.querySelectorAll('.sidebar-menu a');

    allMenuLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            if (this.getAttribute('href') === '#') {
                e.preventDefault();

                // Update content header
                const contentHeader = document.querySelector('.content-header h1');
                contentHeader.textContent = this.querySelector('span')?.textContent || this.textContent;

                // Update breadcrumb
                const breadcrumb = document.querySelector('.breadcrumb');
                breadcrumb.innerHTML = `<span>Home</span> / <span>${this.querySelector('span')?.textContent || this.textContent}</span>`;

                // Simulate content loading
                const contentBody = document.querySelector('.content-body');
                contentBody.innerHTML = `
                    <div class="welcome-message">
                        <h2>${this.querySelector('span')?.textContent || this.textContent} Section</h2>
                        <p>This is a simulated content loading for demonstration purposes.</p>
                    </div>
                `;
            }
        });
    });

    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.documentElement.classList.add("dark");
        toggle.checked = true;
    } else {
        document.documentElement.classList.remove("dark");
        toggle.checked = false;
    }

    toggle.addEventListener("change", () => {
        if (toggle.checked) {
            document.documentElement.classList.add("dark");
            localStorage.setItem("theme", "dark");
        } else {
            document.documentElement.classList.remove("dark");
            localStorage.setItem("theme", "light");
        }
    });
    const userProfileToggle = document.getElementById('userDropdownToggle');
    const dropdown = document.getElementById('userDropdown');

    userProfileToggle.addEventListener('click', function (e) {
        e.stopPropagation(); // boshqalar bilan to‘qnashmasligi uchun
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    });

    // Tashqi joy bosilganda yopiladi
    document.addEventListener('click', function () {
        dropdown.style.display = 'none';
    });
});
window.openModal = function (modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.add('active');
};

window.closeModal = function (modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('active');
};