$(document).ready(function() {
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
		})
	});

	$('#savejson').click(function() {
	    $("#dashboard").validate({
	    	rules: {
	            json_file: {
	                required: true,
	            }

	        },
	        messages: {
	            json_file: {
	                required: " (required)",
	            },
	        },
		})
	});
})