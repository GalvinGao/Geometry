// = Question 1 = //

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
document.getElementById("ResultWrite").innerHTML = posibility;

}

// = Question 2 = //

function qtwo(rtimes,match){
 var matched=0;
 for (k=0;k<rtimes;k++){
  var dice1=Math.floor(Math.random()*6+1);
  var dice2=Math.floor(Math.random()*6+1);
  var dice3=Math.floor(Math.random()*6+1);
  var diceSum=dice1+dice2+dice3;
  if (diceSum>match){
    matched=matched+1;
  }
 }
 var posibility2=matched/rtimes;
 document.getElementById("ResultWrite").innerHTML=posibility2;
}



















/*

// Beautified Code //
// For Question 1.(a) to 1.(c) //

function question1Calculation(heads) {

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

// End Beautified Code / Question 1.(a) to 1.(c) //

*/ 











