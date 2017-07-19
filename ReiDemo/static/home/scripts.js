$(document).ready(function() {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
});

$(document).ready(function() {
    $('#campaign_table').DataTable();
} );

$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
});

function myFunction() {
    document.getElementById("demo").innerHTML = "Hello World";
}