(function () {
  function collapse() {
    var toggles = document.querySelectorAll(".md-sidebar--primary input.md-nav__toggle");
    toggles.forEach(function (box) {
      var item = box.closest("li");
      if (box.id === "__toc") return;
      if (item && item.classList.contains("md-nav__item--section")) return;
      box.checked = false;
      box.indeterminate = false;
      box.classList.remove("md-toggle--indeterminate");
    });
  }
  function run() {
    collapse();
    setTimeout(collapse, 0);
  }
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(run);
  } else {
    document.addEventListener("DOMContentLoaded", run);
  }
  window.addEventListener("load", run);
})();
