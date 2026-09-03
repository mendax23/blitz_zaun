/* BLITZ-ZAUN – Navigation, Galerie-Filter, Lightbox. Ohne Abhängigkeiten. */
(function () {
  'use strict';

  /* Navigation auf dem Handy */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('hauptnav');
  if (toggle && nav) {
    var schliesseNav = function () {
      nav.classList.remove('offen');
      toggle.setAttribute('aria-expanded', 'false');
    };
    toggle.addEventListener('click', function () {
      var offen = nav.classList.toggle('offen');
      toggle.setAttribute('aria-expanded', String(offen));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('offen')) {
        schliesseNav();
        toggle.focus();
      }
    });
    if (window.matchMedia) {
      window.matchMedia('(min-width: 900px)').addEventListener('change', function (e) {
        if (e.matches) { schliesseNav(); }
      });
    }
  }

  /* Galerie-Filter */
  var filter = document.querySelector('.filter');
  var kacheln = Array.prototype.slice.call(document.querySelectorAll('.raster--galerie .raster-bild'));
  if (filter && kacheln.length) {
    var leer = document.querySelector('.filter-leer');
    var setzeFilter = function (kat) {
      var sichtbar = 0;
      kacheln.forEach(function (k) {
        var zeigen = kat === 'alle' || k.getAttribute('data-kat') === kat;
        k.hidden = !zeigen;
        if (zeigen) { sichtbar++; }
      });
      filter.querySelectorAll('[data-filter]').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === kat));
      });
      if (leer) { leer.hidden = sichtbar > 0; }
    };
    filter.addEventListener('click', function (e) {
      var knopf = e.target.closest('[data-filter]');
      if (!knopf) { return; }
      var kat = knopf.getAttribute('data-filter');
      setzeFilter(kat);
      if (window.history && history.replaceState) {
        history.replaceState(null, '', kat === 'alle' ? location.pathname : '#' + kat);
      }
    });
    var hash = location.hash.slice(1);
    if (hash && hash.indexOf('bild-') !== 0 && filter.querySelector('[data-filter="' + hash + '"]')) {
      setzeFilter(hash);
    }
  }

  /* Lightbox */
  var lb = document.getElementById('lightbox');
  if (lb && typeof lb.showModal === 'function') {
    var links = Array.prototype.slice.call(document.querySelectorAll('.galerie-link'));
    var bild = lb.querySelector('img');
    var kat = lb.querySelector('.lightbox-kat');
    var text = lb.querySelector('.lightbox-text');
    var zaehler = lb.querySelector('.lightbox-zaehler');
    var aktuell = 0;

    var sichtbare = function () {
      return links.filter(function (a) { return !a.closest('.raster-bild').hidden; });
    };
    var zeige = function (n) {
      var liste = sichtbare();
      if (!liste.length) { return; }
      aktuell = (n + liste.length) % liste.length;
      var a = liste[aktuell];
      bild.src = a.href;
      bild.alt = a.getAttribute('data-alt');
      bild.width = a.getAttribute('data-breite');
      bild.height = a.getAttribute('data-hoehe');
      kat.textContent = a.getAttribute('data-kategorie');
      text.textContent = a.getAttribute('data-alt');
      zaehler.textContent = (aktuell + 1) + ' / ' + liste.length;
    };

    links.forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        zeige(sichtbare().indexOf(a));
        lb.showModal();
      });
    });
    lb.addEventListener('click', function (e) {
      var knopf = e.target.closest('[data-lb]');
      if (knopf) {
        var was = knopf.getAttribute('data-lb');
        if (was === 'schliessen') { lb.close(); }
        else { zeige(aktuell + (was === 'weiter' ? 1 : -1)); }
        return;
      }
      if (e.target === lb) { lb.close(); }
    });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { zeige(aktuell + 1); }
      if (e.key === 'ArrowLeft') { zeige(aktuell - 1); }
    });
    var startX = null;
    lb.addEventListener('touchstart', function (e) { startX = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (startX === null) { return; }
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 50) { zeige(aktuell + (dx < 0 ? 1 : -1)); }
      startX = null;
    });
    lb.addEventListener('close', function () { bild.removeAttribute('src'); });
  }
})();
