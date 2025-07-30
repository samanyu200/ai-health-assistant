const API_BASE = "/api";
const token = localStorage.getItem("token");
if (!token) window.location = "login.html";

async function authFetch(path, opts = {}) {
  opts.headers = { ...opts.headers, "Authorization": `Bearer ${token}` };
  return fetch(API_BASE + path, opts);
}

async function loadStatus() {
  const res = await authFetch("/planner/status");
  const data = await res.json();
  const div = document.getElementById("status");
  div.innerHTML = `
    <div class="bg-white p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-bold">Health Overview</h2>
      <div class="mt-4 space-y-2">
        <div>Energy: <strong>${data.energy}</strong></div>
        <div>Hydration: <strong>${data.hydration}</strong></div>
        <div>Nutrition Score: <strong>${data.nutrition_score}</strong></div>
      </div>
    </div>`;
}

async function scanImage() {
  const file = document.getElementById("imgInput").files[0];
  if (!file) return alert("Select an image first.");
  const fd = new FormData();
  fd.append("file", file);
  const res = await authFetch("/food/scan-food", { method: "POST", body: fd });
  const result = await res.json();
  document.getElementById("scanResult").innerHTML = `
    <p><strong>Food:</strong> ${result.food}</p>
    <p><strong>Safe to eat:</strong> ${result.safe_to_eat}</p>`;
}

async function loadPlan() {
  const res = await authFetch("/planner/plan");
  const plan = await res.json();
  let html = "<ul class='space-y-1'>";
  for (let m in plan) html += `<li><strong>${m}:</strong> ${plan[m]}</li>`;
  html += "</ul>";
  document.getElementById("planContent").innerHTML = html;
}

async function loadAlerts() {
  const res = await authFetch("/alerts/future-risk");
  const alerts = await res.json();
  let html = `<p>Risk Level: <strong>${alerts.risk_level}</strong></p>`;
  html += `<ul class='list-disc ml-4'>`;
  alerts.recommendations.forEach(r => { html += `<li>${r}</li>`; });
  html += "</ul>";
  document.getElementById("alertsContent").innerHTML = html;
}

async function askChat() {
  const q = document.getElementById("question").value;
  if (!q) return alert("Ask something first.");
  const res = await authFetch("/advice/ask", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ question: q })
  });
  const ans = await res.json();
  document.getElementById("chatAnswer").innerText = ans.answer;
}

window.addEventListener("DOMContentLoaded", () => {
  loadStatus();
  loadPlan();
  loadAlerts();
});
