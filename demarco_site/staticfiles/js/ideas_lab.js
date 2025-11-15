/* ===============================
   TEAM PRODUCTIVITY WIDGET
   =============================== */
function buildTeamProductivityWidget(root) {
    root.innerHTML = `
        <label><b>Team Size:</b> <span id="team-size-display">5</span></label>
        <input id="team-size" type="range" min="1" max="20" value="5">
        <canvas id="teamChart"></canvas>
    `;

    const slider = root.querySelector("#team-size");
    const display = root.querySelector("#team-size-display");
    const ctx = root.querySelector("#teamChart");

    const labels = [...Array(20).keys()].map(i => i + 1);

    function computeProductivity() {
        const data = [];
        for (let t = 1; t <= 20; t++) {
            let overhead = t * (t - 1) / 2;  
            let productivity = Math.max(150 - overhead, 0);
            data.push(productivity);
        }
        return data;
    }

    let chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Productivity Index",
                data: computeProductivity(),
                borderWidth: 3,
                pointRadius: labels.map(() => 4),
                pointBackgroundColor: labels.map(() => "#3b82f6")
            }]
        }
    });

    function update(val) {
        display.textContent = val;
        const index = val - 1;

        // Highlight the selected team size
        chart.data.datasets[0].pointRadius = labels.map((_, i) =>
            i === index ? 10 : 4
        );
        chart.data.datasets[0].pointBackgroundColor = labels.map((_, i) =>
            i === index ? "#ef4444" : "#3b82f6"
        );

        chart.update();
    }

    slider.addEventListener("input", e => update(e.target.value));
    update(5);
}


/* ===============================
   SLACK CAPACITY WIDGET
   =============================== */
function buildSlackWidget(root) {
    root.innerHTML = `
        <label><b>Utilization (%):</b> <span id="util-display">80</span></label>
        <input id="util-range" type="range" min="50" max="100" value="80">
        <canvas id="slackChart"></canvas>
    `;

    const slider = root.querySelector("#util-range");
    const display = root.querySelector("#util-display");
    const ctx = root.querySelector("#slackChart");

    let chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Slack (%)"],
            datasets: [{
                label: "Slack Capacity",
                data: [20],
                borderWidth: 3
            }]
        }
    });

    function update(val) {
        display.textContent = val;
        chart.data.datasets[0].data = [100 - val];
        chart.update();
    }

    slider.addEventListener("input", e => update(e.target.value));
    update(80);
}


/* ===============================
   FLOW TIME WIDGET
   =============================== */
function buildFlowTimeWidget(root) {
    root.innerHTML = `
        <label><b>Interruptions per day:</b> <span id="int-display">3</span></label>
        <input id="int-range" type="range" min="0" max="10" value="3">
        <p><b>Daily Flow Time Lost:</b> <span id="flow-lost">0</span> minutes</p>
    `;

    const slider = root.querySelector("#int-range");
    const disp = root.querySelector("#int-display");
    const lost = root.querySelector("#flow-lost");

    function update(val) {
        disp.textContent = val;
        let minutesLost = val * 20; // avg 20 min lost per interruption
        lost.textContent = minutesLost;
    }

    slider.addEventListener("input", e => update(e.target.value));
    update(3);
}


/* ===============================
   COST OF DELAY WIDGET
   =============================== */
function buildCostOfDelayWidget(root) {
    root.innerHTML = `
        <label><b>Delay (days):</b> <span id="delay-display">5</span></label>
        <input id="delay-range" type="range" min="0" max="60" value="5">
        <p><b>Estimated Cost:</b> <span id="delay-cost">0</span> k$</p>
        <canvas id="delayChart"></canvas>
    `;

    const slider = root.querySelector("#delay-range");
    const display = root.querySelector("#delay-display");
    const costDisplay = root.querySelector("#delay-cost");
    const ctx = root.querySelector("#delayChart");

    const labels = [...Array(61).keys()];

    function computeCostCurve() {
        return labels.map(d => Math.round(Math.exp(d / 15) * 2));
    }

    let curve = computeCostCurve();

    let chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Cost of Delay (k$)",
                    data: curve,
                    borderWidth: 3,
                    borderColor: "#2563eb"
                },
                {
                    label: "Current Delay",
                    data: labels.map(() => null),
                    pointRadius: labels.map(() => 0),
                    pointBackgroundColor: "#ef4444"
                }
            ]
        }
    });

    function update(val) {
        display.textContent = val;

        let cost = curve[val];
        costDisplay.textContent = cost;

        // Show a highlighted point on the curve
        chart.data.datasets[1].data = labels.map((_, i) =>
            i === Number(val) ? curve[i] : null
        );

        chart.data.datasets[1].pointRadius = labels.map((_, i) =>
            i === Number(val) ? 8 : 0
        );

        chart.update();
    }

    slider.addEventListener("input", e => update(e.target.value));
    update(5);
}


/* ===============================
   MONTE CARLO RISK DISTRIBUTION
   =============================== */
function buildMonteCarloWidget(root) {
    root.innerHTML = `
        <button id="runMonteCarlo">Run Monte Carlo Simulation</button>
        <canvas id="mcChart"></canvas>
    `;

    const btn = root.querySelector("#runMonteCarlo");
    const ctx = root.querySelector("#mcChart");

    let chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: [],
            datasets: [{
                label: "Occurrences",
                data: []
            }]
        }
    });

    function runSimulation() {
        let results = [];
        for (let i = 0; i < 1000; i++) {
            let duration = 100 + (Math.random() - 0.5) * 60;
            results.push(Math.round(duration));
        }

        // Histogram
        let buckets = {};
        results.forEach(r => {
            buckets[r] = (buckets[r] || 0) + 1;
        });

        const keys = Object.keys(buckets).sort((a, b) => a - b);
        const vals = keys.map(k => buckets[k]);

        chart.data.labels = keys;
        chart.data.datasets[0].data = vals;
        chart.update();
    }

    btn.addEventListener("click", runSimulation);
}


/* ===============================
   RISK DISTRIBUTION WIDGET
   =============================== */
function buildRiskDistributionWidget(root) {
    root.innerHTML = `
        <button id="runRiskDist">Generate Risk Distribution</button>
        <canvas id="riskChart"></canvas>
    `;

    const btn = root.querySelector('#runRiskDist');
    const ctx = root.querySelector('#riskChart');

    let chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Optimistic', 'Most Likely', 'Pessimistic'],
            datasets: [{
                label: 'Duration (days)',
                data: [0, 0, 0],
                backgroundColor: ['#34d399', '#3b82f6', '#ef4444']
            }]
        }
    });

    function generate() {
        const optimistic = Math.round(20 + Math.random() * 10);
        const likely = Math.round(40 + Math.random() * 20);
        const pessimistic = Math.round(70 + Math.random() * 40);

        chart.data.datasets[0].data = [optimistic, likely, pessimistic];
        chart.update();
    }

    btn.addEventListener('click', generate);
}


/* ===============================
   AUTO-WIRE WIDGETS TO SLUGS
   =============================== */
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".widget").forEach(widget => {
        const id = widget.id;

        if (id === "peopleware") buildTeamProductivityWidget(widget);
        if (id === "communication-overhead") buildTeamProductivityWidget(widget);

        if (id === "slack") buildSlackWidget(widget);

        if (id === "flow-time") buildFlowTimeWidget(widget);

        if (id === "cost-of-delay") buildCostOfDelayWidget(widget);

        if (id === "project-risk-distributions") buildRiskDistributionWidget(widget);
        if (id === "monte-carlo-projects") buildMonteCarloWidget(widget);
    });
});
