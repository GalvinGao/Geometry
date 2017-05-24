function flip(times, heads, faces) {
    var chits = 0;
    var rtimes = times
    var headhit = 0;
    for (ii = 0; ii < rtimes; ii++) {

        for (i = 0; i < 10; i++) {
			var thistime = Math.floor(Math.random() * faces); //console.log(thistime);
			if (thistime == 1) {
				chits = chits + 1;
			} //console.log("i "+i+" "+thistime+" "+chits);
            var thistime = 0;
		}
		if (chits >= heads) {
			headhit = headhit + 1;
		}
         var chits = 0
//console.log("== ii "+ii+" "+headhit+" ==");
	}
	var posibilityc1 = headhit/times;
    var posibilityc2 = posibilityc1 * 100;
    var posibility = posibilityc2 + "%";
	document.getElementById("result").innerHTML=posibility;

}