var mins;
var secs;
var set = "{{ set_id }}";

function cd() {
 	mins = 1 * m("3"); // change minutes here
 	secs = 0 + s(":01"); // change seconds here (always add an additional second to your total)
 	redo();
}

function m(obj) {
 	for(var i = 0; i < obj.length; i++) {
  		if(obj.substring(i, i + 1) == ":")
  		break;
 	}
 	return(obj.substring(0, i));
}

function s(obj) {
 	for(var i = 0; i < obj.length; i++) {
  		if(obj.substring(i, i + 1) == ":")
  		break;
 	}
 	return(obj.substring(i + 1, obj.length));
}

function dis(mins,secs) {
 	var disp;
 	if(mins <= 9) {
  		disp = " 0";
 	} else {
  		disp = " ";
 	}
 	disp += mins + ":";
 	if(secs <= 9) {
  		disp += "0" + secs;
 	} else {
  		disp += secs;
 	}
 	return(disp);
}

function redo() {
 	secs--;
 	if(secs == -1) {
  		secs = 59;
  		mins--;
 	}
 	document.cd.disp.value = dis(mins,secs); // setup additional displays here.
 	if((mins == 0) && (secs == 0)) {
  		window.alert("Time is up. Press OK to continue."); // change timeout message as required
  		if (set == 'SET-1') {
  			window.location = "http://localhost:8000/pupil/test4";
  			}
  		else if (set == "SET-2"){
  			window.location = "http://localhost:8000/pupil/test5";
  			}
  		else if (set == "SET-3"){
  			window.location = "http://localhost:8000/pupil/test6";
  			}
  		else   {
  			window.location = "http://localhost:8000/pupil/test5";
  			}
 	} else {
 		cd = setTimeout("redo()",1000);
 	}
}

function init() {
  cd();
}

window.onload = init;





