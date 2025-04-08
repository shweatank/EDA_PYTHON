const gateSelect = document.getElementById("gateSelect");
const outputEl = document.getElementById("output");
const statusEl = document.getElementById("status");
const truthTableEl = document.getElementById("truthTable");
const logOutput = document.getElementById("logOutput");

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

function loadTruthTable() {
    const gate = gateSelect.value;
    fetch("/get_truth_table", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ gate: gate })
    }).then(res => res.json()).then(data => {
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

function runSynthesis() {
    const gate = gateSelect.value;
    fetch("/run_synthesis", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ gate: gate })
    }).then(res => res.json()).then(data => {
        alert(data.message || data.error);
        loadLogs();
    });
}

function runWaveform() {
    const gate = gateSelect.value;
    fetch("/run_waveform", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ gate: gate })
    }).then(res => res.json()).then(data => {
        alert(data.message || data.error);
        loadLogs();
    });
}

function loadLogs() {
    fetch("/get_logs")
        .then(res => res.json())
        .then(data => {
            logOutput.textContent = data.logs;
        });
}
function listFiles() {
    const gate = document.getElementById("gateSelect").value;
    fetch("/list_files", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ gate })
    })
    .then(res => res.json())
    .then(data => {
        const fileList = document.getElementById("fileList");
        const fileContent = document.getElementById("fileContent");
        fileList.innerHTML = "";
        fileContent.innerHTML = "";

        if (data.files && data.files.length > 0) {
            data.files.forEach(file => {
                const fileId = file[0];
                const fileName = file[1];

                const li = document.createElement("li");

                // View Button
                const viewBtn = document.createElement("button");
                viewBtn.textContent = "🔍 View";
                viewBtn.onclick = () => {
                    fetch(`/view_file/${fileId}`)
                        .then(res => res.json())
                        .then(fileData => {
                            if (fileData.content) {
                                fileContent.innerHTML = `<h4>${fileData.filename}</h4><pre>${fileData.content}</pre>`;
                            } else {
                                fileContent.innerHTML = `<p style="color:red;">Error: ${fileData.error}</p>`;
                            }
                        });
                };

                // Download Link
                const downloadLink = document.createElement("a");
                downloadLink.href = `/download_file/${fileId}`;
                downloadLink.textContent = "📥 Download";
                downloadLink.style.marginLeft = "10px";
                downloadLink.download = fileName;

                // Label
                const label = document.createElement("span");
                label.textContent = " " + fileName;
                label.style.marginRight = "10px";
                label.style.marginLeft = "10px";

                li.appendChild(viewBtn);
                li.appendChild(label);
                li.appendChild(downloadLink);
                fileList.appendChild(li);
            });
        } else {
            fileList.innerHTML = "<li>No files found.</li>";
        }
    })
    .catch(err => console.error("File list error:", err));
}


// Initial load
window.onload = loadLogs;
