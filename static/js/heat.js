var heatmap
var getData = $.get('/heatMap/line1');

var make_data = function (result) {
    var heat = result.heat;
    var station = result.station;
    var brand = result.brand;
    var dataset = [];
   
    for (var i = 0; i < result.brand.length; i++) {
        var data = [];
        for (var j = 0; j < result.station.length; j++) {
            data.push({
                x: station[j],
                y: heat[i][j]
            });
        }
        dataset.push({
            name: brand[i],
            data: data
        })
    }
    return dataset;
}

getData.done(function (result) {
    var ctx = document.querySelector("#heatmap")
    var data = make_data(result);

    heatmap = new ApexCharts(ctx,
        option = {
            chart: {
                type: 'heatmap'
            },
            series: data
        });
    heatmap.render();
})

function updateHeat(line) {
    var updatedData = $.get('/heatMap/'+line);
    updatedData.done(function (result) {
        var data = make_data(result);
        console.log(data);
        heatmap.updateSeries(
            data)
    });
}