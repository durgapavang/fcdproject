$(function() {
	$('#savelogin').click(function() {
	    $("#loginForm").validate({
	        rules: {
	            email: {
	                required: true,
	            }

	        },
	        messages: {
	            email: {
	                required: " (required)",
	            },
	            password: {
	                required: " (required)",
	            },
	        },
	});
})