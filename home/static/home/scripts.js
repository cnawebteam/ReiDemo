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

    Morris.Donut({
        element: 'donut_div',
        data: [
            {label: "Running", value: 33},
            {label: "Pending", value: 103},
            {label: "Failed", value: 3},
            {label: "Finished", value: 10}
        ],
        colors: [
            '#f0579a',
            '#5769ef',
            '#3fbfc0',
            '#f0a258'
        ],
    });
} );
