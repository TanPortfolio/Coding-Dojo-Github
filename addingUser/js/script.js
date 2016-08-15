$(document).ready(function() {
	$('input').val("");
	$('form').submit(function(){
    return false;
	});
});
$(document).on('click', 'button.add', function() {
	$firstName = $('#firstName').val();
	$lastName = $('#lastName').val(); 
	$email = $('#email').val(); 
	$number = $('#number').val(); 
	$('table').append("<tr><td>"+$firstName+"</td>"+"<td>"+$lastName+"</td>"+"<td>"+$email+"</td>"+"<td>"+$number+"</td></tr>");
});
$(document).on('click', 'button.reset', function() {
	$('input').val("");
});