
var getData = $.get('/subwayTime');
var myChart;

getData.done(function (result) {
    console.log(result.label);
    console.log(result.time);
    console.log(result.score);
    
    
    var ctx = document.getElementById('myChart').getContext("2d");
    var data = {
        labels: ['Mon', 'Tue', 'Wed', 'Thr', 'Fri'],
        datasets: [
        {
            label: "Blue",
            fillColor: "blue",
            data: [3,7,4]
        },
        {
            label: "Red",
            fillColor: "red",
            data: [4,3,5]
        },
        {
            label: "Green",
            fillColor: "green",
            data: [7,2,6]
        }]
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