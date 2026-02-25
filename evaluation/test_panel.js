(function () {
  "use strict";

  /* ── Styles ── */
  var style = document.createElement("style");
  style.textContent = `
    #tp-root {
      position: fixed; top: 0; right: 0; bottom: 0;
      width: 380px; z-index: 999999;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 13px; color: #1a1a1a;
      display: flex; flex-direction: column;
      background: #fff; border-left: 1px solid #d0d0d0;
      box-shadow: -2px 0 12px rgba(0,0,0,.08);
      transition: transform .2s ease;
    }
    #tp-root.tp-collapsed { transform: translateX(100%); }
    body.tp-panel-open { margin-right: 380px !important; transition: margin-right .2s ease; }
    #tp-root *, #tp-root *::before, #tp-root *::after {
      box-sizing: border-box;
    }

    #tp-toggle {
      position: fixed; top: 12px; right: 12px; z-index: 999998;
      padding: 6px 12px; border-radius: 6px;
      background: #2563eb; color: #fff; border: none;
      font-size: 12px; font-weight: 600; cursor: pointer;
      box-shadow: 0 2px 6px rgba(0,0,0,.15);
      transition: right .2s ease;
    }
    #tp-toggle.tp-panel-open { right: 392px; }

    #tp-header {
      padding: 14px 16px; background: #f8f9fb;
      border-bottom: 1px solid #e0e0e0;
      display: flex; align-items: center; justify-content: space-between;
    }
    #tp-header h2 { margin: 0; font-size: 15px; font-weight: 700; }
    #tp-score { font-size: 13px; font-weight: 600; color: #16a34a; }

    #tp-filters {
      display: flex; gap: 6px; padding: 10px 16px;
      border-bottom: 1px solid #e0e0e0; background: #f8f9fb;
    }
    #tp-filters button {
      padding: 4px 10px; border-radius: 4px; border: 1px solid #d0d0d0;
      background: #fff; font-size: 12px; cursor: pointer; font-weight: 500;
    }
    #tp-filters button.active {
      background: #2563eb; color: #fff; border-color: #2563eb;
    }

    #tp-list {
      flex: 1; overflow-y: auto; padding: 8px 0;
    }
    .tp-task {
      padding: 8px 16px; cursor: pointer; display: flex;
      align-items: center; gap: 8px; border-bottom: 1px solid #f0f0f0;
    }
    .tp-task:hover { background: #f3f4f6; }
    .tp-task.tp-selected { background: #eff6ff; border-left: 3px solid #2563eb; }

    .tp-badge {
      font-size: 10px; font-weight: 600; padding: 2px 6px;
      border-radius: 3px; text-transform: uppercase; flex-shrink: 0;
    }
    .tp-badge-easy   { background: #dcfce7; color: #166534; }
    .tp-badge-medium { background: #fef9c3; color: #854d0e; }
    .tp-badge-hard   { background: #fee2e2; color: #991b1b; }

    .tp-task-id { font-weight: 600; width: 56px; flex-shrink: 0; }
    .tp-task-status { flex-shrink: 0; width: 18px; text-align: center; }
    .tp-task-instr { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

    #tp-detail {
      border-top: 1px solid #e0e0e0; padding: 14px 16px;
      background: #f8f9fb; min-height: 180px;
    }
    #tp-detail-empty { color: #888; font-style: italic; }
    #tp-detail-instr {
      margin: 8px 0; line-height: 1.5; font-size: 13px;
      max-height: 80px; overflow-y: auto;
    }
    #tp-actions { display: flex; gap: 8px; margin-top: 10px; }
    #tp-actions button {
      padding: 7px 16px; border-radius: 6px; border: none;
      font-size: 13px; font-weight: 600; cursor: pointer;
    }
    #tp-btn-reset {
      background: #e5e7eb; color: #374151;
    }
    #tp-btn-reset:hover { background: #d1d5db; }
    #tp-btn-verify {
      background: #2563eb; color: #fff;
    }
    #tp-btn-verify:hover { background: #1d4ed8; }
    #tp-btn-verify:disabled, #tp-btn-reset:disabled {
      opacity: .5; cursor: not-allowed;
    }

    #tp-result {
      margin-top: 10px; padding: 8px 12px; border-radius: 6px;
      font-size: 13px; line-height: 1.4; display: none;
    }
    #tp-result.tp-pass { background: #dcfce7; color: #166534; display: block; }
    #tp-result.tp-fail { background: #fee2e2; color: #991b1b; display: block; }
  `;
  document.head.appendChild(style);

  /* ── State ── */
  var tasks = [];
  var selectedId = null;
  var filter = "all";
  var storageKey = "tp-progress:" + window.location.origin;
  var progress = {}; // task_id -> { passed: bool }

  function loadProgress() {
    try { progress = JSON.parse(localStorage.getItem(storageKey)) || {}; } catch (e) { progress = {}; }
  }
  function saveProgress() {
    try { localStorage.setItem(storageKey, JSON.stringify(progress)); } catch (e) {}
  }

  /* ── DOM ── */
  var toggle = document.createElement("button");
  toggle.id = "tp-toggle";
  toggle.textContent = "Test Panel";
  toggle.className = "tp-panel-open";
  document.body.appendChild(toggle);

  var root = document.createElement("div");
  root.id = "tp-root";
  root.innerHTML = [
    '<div id="tp-header"><h2>Test Panel</h2><span id="tp-score"></span></div>',
    '<div id="tp-filters">',
    '  <button data-f="all" class="active">All</button>',
    '  <button data-f="easy">Easy</button>',
    '  <button data-f="medium">Medium</button>',
    '  <button data-f="hard">Hard</button>',
    '</div>',
    '<div id="tp-list"></div>',
    '<div id="tp-detail"><span id="tp-detail-empty">Select a task above</span></div>',
  ].join("");
  document.body.appendChild(root);

  var panelOpen = true;
  document.body.classList.add("tp-panel-open");
  toggle.addEventListener("click", function () {
    panelOpen = !panelOpen;
    root.classList.toggle("tp-collapsed", !panelOpen);
    toggle.classList.toggle("tp-panel-open", panelOpen);
    document.body.classList.toggle("tp-panel-open", panelOpen);
  });

  document.addEventListener("keydown", function (e) {
    if (e.ctrlKey && e.shiftKey && e.key === "T") {
      e.preventDefault();
      toggle.click();
    }
  });

  /* ── Filters ── */
  root.querySelector("#tp-filters").addEventListener("click", function (e) {
    if (e.target.tagName !== "BUTTON") return;
    filter = e.target.dataset.f;
    root.querySelectorAll("#tp-filters button").forEach(function (b) {
      b.classList.toggle("active", b.dataset.f === filter);
    });
    renderList();
  });

  /* ── Rendering ── */
  function passCount() {
    var n = 0;
    for (var k in progress) { if (progress[k] && progress[k].passed) n++; }
    return n;
  }

  function renderScore() {
    root.querySelector("#tp-score").textContent = passCount() + " / " + tasks.length + " passed";
  }

  function renderList() {
    var list = root.querySelector("#tp-list");
    var visible = tasks.filter(function (t) {
      return filter === "all" || t.difficulty === filter;
    });
    list.innerHTML = visible.map(function (t) {
      var cls = "tp-task" + (t.id === selectedId ? " tp-selected" : "");
      var badge = "tp-badge tp-badge-" + t.difficulty;
      var status = "";
      if (progress[t.id]) {
        status = progress[t.id].passed ? "\u2705" : "\u274c";
      }
      return '<div class="' + cls + '" data-id="' + t.id + '">' +
        '<span class="tp-task-status">' + status + '</span>' +
        '<span class="tp-task-id">' + t.id + '</span>' +
        '<span class="' + badge + '">' + t.difficulty + '</span>' +
        '<span class="tp-task-instr">' + escHtml(t.instruction) + '</span>' +
        '</div>';
    }).join("");
  }

  function renderDetail() {
    var detail = root.querySelector("#tp-detail");
    if (!selectedId) {
      detail.innerHTML = '<span id="tp-detail-empty">Select a task above</span>';
      return;
    }
    var task = tasks.find(function (t) { return t.id === selectedId; });
    if (!task) return;
    detail.innerHTML = [
      '<strong>' + escHtml(task.id) + '</strong>',
      ' <span class="tp-badge tp-badge-' + task.difficulty + '">' + task.difficulty + '</span>',
      '<div id="tp-detail-instr">' + escHtml(task.instruction) + '</div>',
      '<div id="tp-actions">',
      '  <button id="tp-btn-reset">Reset</button>',
      '  <button id="tp-btn-verify">Verify</button>',
      '</div>',
      '<div id="tp-result"></div>',
    ].join("");

    detail.querySelector("#tp-btn-reset").addEventListener("click", doReset);
    detail.querySelector("#tp-btn-verify").addEventListener("click", doVerify);

    // Restore last result if any
    if (progress[selectedId]) {
      showResult(progress[selectedId].passed, progress[selectedId].message || "");
    }
  }

  function showResult(passed, message) {
    var el = root.querySelector("#tp-result");
    if (!el) return;
    el.className = passed ? "tp-pass" : "tp-fail";
    el.style.display = "block";
    el.textContent = (passed ? "PASSED" : "FAILED") + (message ? " \u2014 " + message : "");
  }

  function escHtml(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
  }

  /* ── Task selection ── */
  root.querySelector("#tp-list").addEventListener("click", function (e) {
    var row = e.target.closest(".tp-task");
    if (!row) return;
    selectedId = row.dataset.id;
    renderList();
    renderDetail();
  });

  /* ── Actions ── */
  function setButtons(disabled) {
    var r = root.querySelector("#tp-btn-reset");
    var v = root.querySelector("#tp-btn-verify");
    if (r) r.disabled = disabled;
    if (v) v.disabled = disabled;
  }

  function doReset() {
    setButtons(true);
    var res = root.querySelector("#tp-result");
    if (res) { res.style.display = "none"; }
    fetch("/api/reset", { method: "POST" })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        setButtons(false);
        if (!d.seed_restored) {
          showResult(false, "No seed state yet \u2014 reload the page first");
        }
      })
      .catch(function (e) {
        setButtons(false);
        showResult(false, "Reset error: " + e.message);
      });
  }

  function doVerify() {
    if (!selectedId) return;
    setButtons(true);
    var res = root.querySelector("#tp-result");
    if (res) { res.style.display = "none"; }
    fetch("/api/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ task_id: selectedId }),
    })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        setButtons(false);
        progress[d.task_id] = { passed: d.passed, message: d.message };
        saveProgress();
        showResult(d.passed, d.message);
        renderScore();
        renderList();
      })
      .catch(function (e) {
        setButtons(false);
        showResult(false, "Verify error: " + e.message);
      });
  }

  /* ── Init ── */
  loadProgress();
  fetch("/api/tasks")
    .then(function (r) { return r.json(); })
    .then(function (data) {
      tasks = data;
      renderScore();
      renderList();
    })
    .catch(function (e) {
      root.querySelector("#tp-list").innerHTML =
        '<div style="padding:16px;color:#991b1b;">Failed to load tasks: ' + e.message + '</div>';
    });
})();
