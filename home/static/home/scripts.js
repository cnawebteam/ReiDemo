$(document).ready(function() {
    $('#campaign_table').DataTable();
    $('#transaction_table').DataTable();
    $('#users_table').DataTable({
        "columnDefs": [
        { "width": "2.5%", "targets": [0,1] },
        { "width": "13.5%", "targets": [2,3,4,5,6,7,8] }]
    });
    $('#proposal_table').DataTable({
        "columnDefs": [
        { "width": "2.5%", "targets": [0,1] },
        { "width": "19%", "targets": [2,3,4,5,6] }]
    });
} );