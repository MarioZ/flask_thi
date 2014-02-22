$(function(){
	
	var note = $('#note'),
		ts = document.getElementById("time_remain").innerHTML,
		newYear = true;
	
	if(ts > 0){
		// The new year is here! Count towards something else.
		// Notice the *1000 at the end - time must be in milliseconds
		ts = (new Date()).getTime() + ts*1000;
		newYear = false;
	}
		
	$('#countdown').countdown({
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){
			
			var message = "";
			
			message += "Thời gian làm bài còn " + hours + " hour" + ( hours==1 ? '':'s' ) + ", ";
			message += minutes + " minute" + ( minutes==1 ? '':'s' ) + " and ";
			message += seconds + " second" + ( seconds==1 ? '':'s' ) + " <br />";
			
            if(minutes == 0){
                if(seconds == 0){
                    newYear = true;
                }
			}
            
			if(newYear){
                message="Timeout!";
                setTimeout("window.location.replace('/');", 3000);
			}
			else {
				message += "<input type=submit name=doexam value='" + document.getElementById("button").innerHTML + "'>";
			}
			
            note.html(message);
            
		}
	});
	
});
