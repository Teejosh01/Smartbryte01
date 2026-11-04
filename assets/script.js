/* SmartBryte homepage — progressive enhancement only.
   The page is fully readable with JavaScript disabled. */
(function () {
  "use strict";

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* Footer year */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* Header elevation once the page scrolls */
  var header = document.getElementById("site-header");
  function onScroll() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Entrance reveals */
  var revealEls = document.querySelectorAll(".reveal");
  if (reducedMotion.matches || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.18, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* Gentle pointer parallax on selected hero shapes (fine pointers only).
     Tiles keep their own CSS float; only [data-depth] accents drift. */
  var stage = document.querySelector(".hero-stage");
  var finePointer = window.matchMedia("(pointer: fine)").matches;
  if (stage && finePointer && !reducedMotion.matches) {
    var drifters = stage.querySelectorAll("[data-depth]");
    var raf = null;

    stage.addEventListener("pointermove", function (e) {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        var r = stage.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        drifters.forEach(function (el) {
          var d = parseFloat(el.getAttribute("data-depth")) || 0;
          el.style.translate = (x * d) + "px " + (y * d) + "px";
        });
        raf = null;
      });
    });

    stage.addEventListener("pointerleave", function () {
      drifters.forEach(function (el) { el.style.translate = ""; });
    });
  }
})();
