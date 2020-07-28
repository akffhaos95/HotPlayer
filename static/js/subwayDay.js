var myChart;
var dynamicColors = function() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ")";
};
var make_data = function(result) {
    var datasets = [];
    for(var i=0; i<result.label.length; i++){
        var color = dynamicColors()
        datasets.push({ 
            label: result.label[i],
            data: result.score[i],
            borderColor: color,
            backgroundColor: color,
            fill: false,
            lineTension: 0
        })
    }
    
    var data = {
        labels: result.time,
        datasets: datasets,
    };
    return data;
}

var getData = $.get('/subwayDay/days');

getData.done(function (result) {
    var data = make_data(result);
    var ctx = document.getElementById('myChart').getContext("2d");
    var options = {
        responsive: false,
        options: {
            responsive: true,
        }
    }
    myChart = new Chart(ctx, { type: 'line', data: data, options: options });
    $('.analysis').text(result.analysis);
});

function updateChart(day) {
    var updatedData = $.get('/subwayDay/'+day);
    updatedData.done(function (result) {
        var data = make_data(result);
        myChart.data = data;
        myChart.update();
        $('.analysis').text(result.analysis);
    });
}