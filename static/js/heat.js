var heatmap
var getData = $.get('/heatMap/line1');

var make_data = function (result) {
    var heat = result.heat;
    var station = result.station;
    var brand = result.brand;

    var data = [];

    for (var i = 0; i < result.station.length; i++) {
        for (var j = 0; j < result.brand.length; j++) {
            data.push({
                y: j,
                x: i,
                a: 1,
                v: heat[j][i]
            });
        }
    }
    return data;
}

getData.done(function (result) {
    var ctx = document.getElementById('heatMap').getContext('2d');
    var station = result.station;
    var brand = result.brand;
    var data = make_data(result);

    console.log(data)
    heatmap = new Chart(ctx, {
        type: 'heatmap',
        data: {
            xLabels: station,
            yLabels: brand,
            datasets: [{
                data: data
            }]
        },
        options: {
            yColors: [ // colors for each lines
                { r: 0, g: 150, b: 136 },
                { r: 255, g: 235, b: 59 },
                { r: 255, g: 152, b: 0 },
                { r: 244, g: 67, b: 54 }
            ],
        }
    })
})