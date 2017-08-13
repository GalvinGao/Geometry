function calc(interR, outerR, times) {
    // === Variable Initiation === //
    
    var counter = 0;
    var x = 0.0;
    var y = 0.0;
    var z = 0.0;
    var d = 0.0;

    var trueR = outerR - interR;
    var circleD = trueR * 2;
    var trueRDouble = trueR * trueR;
    var height = outerR * Math.PI * 2;

    var picker1 = Math.floor(Math.random() * times);
    var picker2 = Math.floor(Math.random() * times);
    var picker3 = Math.floor(Math.random() * times);
    var picker4 = Math.floor(Math.random() * times);
    var picker5 = Math.floor(Math.random() * times);
    
    
    // === Question 1 === //

    for (var i = 0; i < times; i++) {
        x = Math.random() * circleD;
        y = Math.random() * circleD;
        z = Math.random() * height;

        var distanceWithoutSqrt = (x - trueR) * (x - trueR) + (y - trueR) * (y - trueR);
        var distanceToCenter = Math.sqrt(distanceWithoutSqrt);

        if (distanceToCenter <= trueR) {
            if (0 < z < height) {
                counter += 1;
            }
        }

        if (i == picker1 || i == picker2 || i == picker3 || i == picker4 || i == picker5) {
            console.log("x: " + x + " y: " + y + " z: " + z + " d: " + d);
        }
    }
    
    
    // === Question 2 === //
    
    var equationVolume = 2 * Math.PI * Math.PI * outerR * trueR * trueR;
    
    
    // === Calculation / Debug Output === //
    
    var resultPosibility = counter / times;
    var result = (trueR * 2) * (trueR * 2) * height * resultPosibility;
    var rawRatio = equationVolume / result;
    var resultRatio = (rawRatio) * 100;
    console.log("trueR: " + trueR + " Pi: " + Math.PI + " height: " + height + " resultPosibility: " + resultPosibility + " counter: " + counter + " result: " + result);
    document.getElementById("TitleWrite").innerHTML = "Calculation result of program 'inner radius "+interR+", outer radius "+outerR+" and random for "+times+" times'";
    document.getElementById("ResultWrite").innerHTML = result.toFixed(8);
    document.getElementById("EVWrite").innerHTML = equationVolume.toFixed(4);
    document.getElementById("RatioWrite").innerHTML = resultRatio.toFixed(4) + "%";
}