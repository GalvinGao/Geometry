function qone(heads){

var mainCount = 0;

for (j=0;j<10000;j++){

var matchCount = 0;
for (i=0;i<10;i++){
  var randomNumber = Math.floor(Math.random()*2) // Random Generates 0,1 two conditions
  if (randomNumber == 0){
    var matchCount = matchCount + 1;
  }
}

if (matchCount > heads){
  var mainCount = mainCount + 1;
}

}

var posibility = mainCount/10000;
document.getElementById("result").innerHTML = posibility;

}



















/*

// Beautified Code //
// For Question 1.(a) to 1.(c)

function hahaha(heads) {

	var mainCount = 0;

	for (j = 0; j < 10000; j++) {

		var matchCount = 0;
		for (i = 0; i < 10; i++) {
			var randomNumber = Math.floor(Math.random() * 2) // Random Generates 0,1 two conditions
			if (randomNumber == 0) {
				var matchCount = matchCount + 1;
			}
		}

		if (matchCount >= heads) {
			var mainCount = mainCount + 1;
		}

	}

	var posibility = mainCount / 10000;
	document.getElementById("result").innerHTML = posibility;

}

// End Beautified Code //

*/ 











