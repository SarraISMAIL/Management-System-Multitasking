function makeTableHTML(myArray) {
    var result = " <table class=\"table table-striped\"> <thead> <tr>" ;
        result+= " <th class=\"text-center\" scope=\"col\">PID</th>";
        result += " <th class=\"text-center\" scope=\"col\">Name</th>"
        result += " <th class=\"text-center\" scope=\"col\">Status</th>"
        result += " <th class=\"text-center\" scope=\"col\">Memory usage</th>"
        result += " <th class=\"text-center\" scope=\"col\">CPU usage</th>"
        result += " <th scope=\"col\"></th>"
        result += " </tr> </thead> <tbody> ";
    for(var i=0; i<myArray.length; i++) {
        result += `<tr id=${i}>`;
        for(var j=0; j<myArray[i].length; j++){
            result += "<td class=\"text-center\">"+myArray[i][j]+"</td>";
        }
        result += "</tr>";
    }
    result += "</table>";
    return result;
}
var table = makeTableHTML({% data %} );
document.querySelector("#section").innerHTML = table ;


// var socket = new WebSocket('ws://localhost:8000/ws/graph/');

// socket.onmessage = function(e){
//     var d = JSON.parse(e.data);
//     var newGDatat = graphData.data.datasets[0].data;
    
    
//     console.log("---> d = " + d);
//     console.log("---> new gData = " + newGDatat);
    
//     graphData.data.datasets[0].data = newGDatat;
//     myLineChart.update();
//     document.querySelector("#section").innerHTML = ;
