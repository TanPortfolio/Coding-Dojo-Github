$(document).ready(function(){
  $("#start").datepicker({
    minDate: 0,
    onSelect: function (date) {
      var date2 = $('#start').datepicker('getDate');
      $('#end').datepicker('option', 'minDate', date2);
    }
  }); 
  $("#start").datepicker(); 
  $("form").on("submit",function(){
    var errors = [];
    var date_from = $("#start").val();
    var date_to = $("#end").val();
    var name = $("#name").val();
    if(date_from == "")
      errors.push("Date from cannot be empty");
    if(date_to == "")
      errors.push("Date to cannot be empty");
    if(name == "")
      errors.push("Name cannot be empty");
    if(errors.length > 0)
    {
      $("#message").html("");
      for(var i in errors){
        $("#message").append("<p id='error_message'>" + errors[i] + "</p>");
      }
    }
    else
      {
        $("#message").html("");
        alert("Thanks " + name + "! Your cruise leaves on " +
        date_from + " and returns on " + date_to + "!");
      }
    return false;
  });
});  