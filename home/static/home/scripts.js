$(document).ready(function() {
    $('#campaign_table').DataTable({
        "order": [ 0, 'asc' ]
    });

    $('#transaction_table').DataTable({
        "order": [ 0, 'asc' ]
    });

    $('#users_table').DataTable({
        //"columnDefs": [
        //{ "width": "2.5%", "targets": [0,1] },
        //{ "width": "13.5%", "targets": [2,3] }],
        "order": [ 0, 'asc' ]
    });

    $('#proposal_table').DataTable({
        "columnDefs": [
        { "width": "2.5%", "targets": [0] },
        { "width": "19%", "targets": [1,2,3,4,5,6] }],
        "order": [ 0, 'asc' ]
    });

    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Running', 33],
            ['Pending', 103],
            ['Failed',  3],
            ['Finished', 10],
        ]);

        var options = {
            'pieHole': 0.65,
            'colors':['#f0579a','#5769ef', '#3fbfc0', '#f0a258'],
            'height': 250,
            'width': 300,
            'chartArea': {
                'width': '100%', 'height': '80%',
            },
            'legend': {'position': 'bottom'},
            'backgroundColor': '#EEEEEE',
            'fontSize': 12,
            'pieSliceText': 'none',
            'pieSliceBorderColor': 'white',
            'pieStartAngle': 240,
            'tooltip': {
                'ignoreBounds': true,
                'isHtml': true,
                'text': 'both',
                'textStyle': {
                    'bold': true,
                    'fontSize': 15
                }
            }
        };

        var chart = new google.visualization.PieChart(document.getElementById('donut_div'));
        chart.draw(data, options);
    }
} );
