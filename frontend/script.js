$("#start_date").val("2021-03-01");
$("#end_date").val("2021-03-31");
$("#submit").click(() => {
    const solar_plant_uid = $("#solar_plant_uid").val();
    const start_date = $("#start_date").val();
    const end_date = $("#end_date").val();
    console.log(solar_plant_uid, start_date, end_date);
    if (!solar_plant_uid || !start_date || !end_date) {
        $(".form_error").show();
        setTimeout(() => {
            $(".form_error").hide();
        }, 3000);
        return;
    }
    $(".loading").show();
    $.get(`http://localhost:8000/dashboard/stats/solar_plant/${solar_plant_uid}?start_date=${start_date}&end_date=${end_date}`).then((response) => {
        $(".loading").hide();
        $("form_error").hide();
        console.log(response);
        let dates = $.unique(response.map((x) => x.reading_date).sort());
        let values_generation = dates.map((x) => {
            return parseFloat(response.find((y) => y.reading_date === x && y.reading_type === "generation").reading_value);
        });
        let values_irradiation = dates.map((x) => {
            return parseFloat(response.find((y) => y.reading_date === x && y.reading_type === "irradiation").reading_value);
        });
        console.log(dates);
        console.log(values_generation);
        console.log(values_irradiation);
        init_chart(dates, values_generation, values_irradiation);
    });
});

function init_chart(dates, values_generation, values_irradiation) {
    Highcharts.chart("container", {
        chart: {
            type: "spline",
        },
        title: {
            text: "Solar Plant Readings",
        },
        xAxis: {
            categories: dates,
        },
        yAxis: {
            title: {
                text: "Reading Value",
            },
            labels: {
                formatter: function () {
                    return this.value;
                },
            },
        },
        tooltip: {
            crosshairs: true,
            shared: true,
        },
        plotOptions: {
            spline: {
                marker: {
                    radius: 4,
                    lineColor: "#666666",
                    lineWidth: 1,
                },
            },
        },
        series: [
            {
                name: "Generation",
                marker: {
                    symbol: "square",
                },
                data: values_generation,
            },
            {
                name: "Irradiation",
                marker: {
                    symbol: "diamond",
                },
                data: values_irradiation,
            },
        ],
    });
}
