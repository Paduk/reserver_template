/*
	reserve table js
	hj 19.02.12
*/

$(document).ready(function() {
    console.log("ready!");

    let element = document.getElementById("tb_col_1");
    element.addEventListener("click", function(){
  		console.log("asd")
	});
    
    $("#tb_col_2").mousedown(function() {
	  	alert("Sorry, This time is checked out");
	});
});