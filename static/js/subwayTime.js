var myChart;
var dynamicColors = function() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ")";
};
var make_data = function(result) {
    var data = [];
    for(var i=0; i<result.score.length; i++){
        var data2 = [];
        for(var j=0; j<result.score.length; j++){
            data2.push(result.score[j][i]);
        }
        data.push(data2);
    }
    
    var datasets = [];
    for(var i=0; i<result.time.length-1; i++){
        datasets.push({ 
            label: result.time[i+1],
            data: data[i],
            backgroundColor: dynamicColors()
        })
    }
    
    var data = {
        labels: result.label,
        datasets: datasets
    };
    
    return data;
}
var getData = $.get('/subwayTime/up/total/아침');

getData.done(function (result) {
    var data = make_data(result);
    var ctx = document.getElementById('myChart').getContext("2d");
    var options = {}
    myChart = new Chart(ctx, { type: 'bar', data: data, options: options });
    $('.analysis').text(result.analysis);
});

function updateChart(up_down, line, time) {
    var updatedData = $.get('/subwayTime/'+up_down+'/'+line+'/'+time);
    updatedData.done(function (result) {
        var data = make_data(result);
        myChart.data = data;
        myChart.update();
        $('.analysis').text(result.analysis);
    });
}