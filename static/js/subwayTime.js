
var getData = $.get('/subwayTime');
var myChart;

getData.done(function (result) {
    console.log(result.label);
    console.log(result.time);
    console.log(result.score);
    
    var datasets;
    for(var i=0; i<result.score.length; i++){
        datasets.push({ 
            label : result.time[i],
            data: result.score[i]       
        })
    }
    var ctx = document.getElementById('myChart').getContext("2d");
    var data = {
        labels: ['Mon', 'Tue', 'Wed', 'Thr', 'Fri'],
        datasets: [ datasets ]
    };
    var options = {
        width: 800,
        height: 600
    }
    myChart = new Chart(ctx, { type: 'bar', data: data, data, options: options });
});

function updateChart() {
    console.log("update")
    var updatedData = $.get('/subwayTime');
    updatedData.done(function (results) {
        console.log(results.result)
        myChart.data.datasets[0].data = results.result
        myChart.update();
    });
}

$('.update').on('click', updateChart);