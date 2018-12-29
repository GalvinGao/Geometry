/* function flip(times, heads, faces) {
    var chits = 0;
    var rtimes = times
    var headhit = 0;
    for (ii = 0; ii < rtimes; ii++) {

			var thistime = Math.floor(Math.random() * faces); //console.log(thistime);
			if (thistime == 1) {
				chits = chits + 1;
			} 
            var thistime = 0;
		
		if (chits >= heads) {
			headhit = headhit + 1;
		}
         var chits = 0
console.log("== ii "+ii+" "+headhit+" "+thistime+" "+chits" ==");
	}
	var posibilityc1 = headhit/times;
    var posibilityc2 = posibilityc1 * 100;
    var posibility = posibilityc2 + "%";
	document.getElementById("result").innerHTML=posibility;

} */

// 0 代表正面，1 代表反面

function 233(){

var mainCount = 0;

for (j=0;j<10000;j++){

var matchCount = 0;
for (i=0;i<10;i++){
  var randomNumber = Math.floor(Math.random()*2) // Random Generates 0,1 two conditions
  if (randomNumber == 0){
    var matchCount = matchCount + 1;
  }
}

if (matchCount >= 5){
  var mainCount = mainCount + 1;
}

}

var posibility = mainCount/10000;
document.getElementById("result").innerHTML = posibility;

}