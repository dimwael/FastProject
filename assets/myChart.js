var ctx = document.getElementById("myChart").getContext("2d");

var data = {
    labels: ["Chocolate", "Vanilla", "Strawberry","hello","zee"],
    datasets: [
        {
            label: "Old Version",
            backgroundColor: "rgba(50,50,255,0.3)",
            data: [3,7,4,8,2]
        },
        {
            label: "After Commit",
            backgroundColor: "rgba(255,50,50,0.3)",
            data: [4,3,5,7,5]
        }

    ]
};

var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
        barValueSpacing: 10,
        scales: {
            yAxes: [{
                ticks: {
                    min: 0,
                }
            }]
        }
    }
});
