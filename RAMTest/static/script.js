const gateSelect = document.getElementById("gateSelect");
const outputEl = document.getElementById("output");
const statusEl = document.getElementById("status");
const logOutput = document.getElementById("logOutput");

// GATE LOGIC TEST
function runTest() {
    const gate = gateSelect.value;
    fetch("/run_test", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ gate: gate })
    }).then(res => res.json()).then(data => {
        outputEl.textContent = data.output || data.error;
        statusEl.textContent = data.status === "Passed" ? "✅ Passed" : "❌ Failed";
        statusEl.className = data.status.toLowerCase();
        loadLogs();
    });
}

// GATE TRUTH TABLE
function loadTruthTable() {
    const gate = gateSelect.value;
    fetch("/get_truth_table", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ gate: gate })
    }).then(res => res.json()).then(data => {
        const truthTableEl = document.getElementById("truthTable");
        if (data.table) {
            let html = '';
            data.table.forEach(row => {
                html += '<tr>' + row.map(col => `<td>${col}</td>`).join('') + '</tr>';
            });
            truthTableEl.innerHTML = html;
        } else {
            alert(data.error);
        }
        loadLogs();
    });
}

// Synthesis button (for both gate and RAM mode)
function runSynthesis() {
    fetch("/synthesize", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            alert(data.message || data.error);
            loadLogs();
            location.reload();  // Refresh to load SVG if generated
        });
}

// GTKWave button
function runWaveform() {
    fetch("/gtkwave", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            alert(data.message || data.error);
            loadLogs();
        });
}

// RAM Simulation
function runSimulation() {
    fetch("/simulate", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            alert(data.message || data.error);
            loadLogs();
        });
}

// LOGS
function loadLogs() {
    fetch("/get_logs")
        .then(res => res.json())
        .then(data => {
            logOutput.textContent = data.logs;
        });
}

// Initial load
window.onload = loadLogs;
