/* El Pibble Chef — comportamiento de la página */
(function () {
    'use strict';

    /* ----- Menú desplegable ----- */
    var btn = document.getElementById('menu-btn');
    var panel = document.getElementById('menu-panel');

    function setMenu(open) {
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.hidden = !open;
    }

    btn.addEventListener('click', function (e) {
        e.stopPropagation();
        setMenu(panel.hidden);
    });
    panel.addEventListener('click', function (e) {
        if (e.target.closest('a')) setMenu(false);
    });
    document.addEventListener('click', function (e) {
        if (!panel.hidden && !e.target.closest('.menu')) setMenu(false);
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && !panel.hidden) {
            setMenu(false);
            btn.focus();
        }
    });

    /* ----- Línea inferior del encabezado al hacer scroll ----- */
    var header = document.getElementById('top');
    function onScroll() {
        header.classList.toggle('scrolled', window.scrollY > 8);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* ----- Abrir la sección legal al llegar desde el menú ----- */
    function openLegal() {
        if (!location.hash) return;
        var target = document.querySelector(location.hash);
        if (!target) return;
        var first = target.querySelector('details');
        if (first) first.open = true;
    }
    window.addEventListener('hashchange', openLegal);

    /* ----- Galería: ver foto en grande ----- */
    var box = document.getElementById('lightbox');
    var boxImg = document.getElementById('lightbox-img');
    var boxTitle = document.getElementById('lightbox-title');
    var boxClose = document.getElementById('lightbox-close');

    if (box && typeof box.showModal === 'function') {
        document.querySelectorAll('.shot').forEach(function (shot) {
            shot.addEventListener('click', function () {
                boxImg.src = shot.getAttribute('data-full');
                boxImg.alt = shot.getAttribute('data-title') || '';
                boxTitle.textContent = shot.getAttribute('data-title') || '';
                box.showModal();
            });
        });
        boxClose.addEventListener('click', function () { box.close(); });
        box.addEventListener('click', function (e) {
            if (e.target === box) box.close();
        });
    }

    /* ----- Año del pie de página ----- */
    var year = document.getElementById('year');
    if (year) year.textContent = new Date().getFullYear();
})();
