var ctxD = document.getElementById("cpuChart").getContext('2d');
var graphData = {
    type: 'doughnut',
    data: {
        labels: ["Used", "Free"],
        datasets: [{
            label: "Disk Usage",
            data: [0,0],
            backgroundColor: ["#007bff", "#6DE441"],
            hoverBackgroundColor: ["#FF5A5E", "#5AD3D1"]
        }]
    },
    options: {
        responsive: true,
        plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'RAM Usage (GB)'
        }
        }
    },
}

var myLineChart = new Chart(ctxD, graphData);
var socket = new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage = function(e){
    var d = JSON.parse(e.data);
    var newGDatat = graphData.data.datasets[0].data;
    newGDatat.shift();
    newGDatat.push(d.ram.used);
    newGDatat.shift();
    newGDatat.push(d.ram.free);
    
    console.log("---> d = " + d);
    console.log("---> new gData = " + newGDatat);
    
    graphData.data.datasets[0].data = newGDatat;
    myLineChart.update();
    // document.querySelector("#value").innerText = d.min;
}