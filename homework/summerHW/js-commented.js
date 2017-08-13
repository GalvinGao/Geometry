function calculationDemoSummerHomeworkByGalvin(interR, outerR, times) {
    
    // === Variable Initiation === //
    
    var counter = 0;
    var x = 0.0; // Initialize the variable 'x'
    var y = 0.0; // Initialize the variable 'y'
    var z = 0.0; // Initialize the variable 'z'
    var d = 0.0; // Initialize the variable 'd'

    var trueR = outerR - interR; // The ring's radius
    var circleD = trueR * 2; // The circle diameter 
    var trueRDouble = trueR * trueR; // The double of ring's radius, used as calculating surface area.
    var height = outerR * Math.PI * 2;

    var picker1 = Math.floor(Math.random() * times); // Randomly pick up the data to debug. No worries about performance
    var picker2 = Math.floor(Math.random() * times); // Randomly pick up the data to debug. No worries about performance
    var picker3 = Math.floor(Math.random() * times); // Randomly pick up the data to debug. No worries about performance
    var picker4 = Math.floor(Math.random() * times); // Randomly pick up the data to debug. No worries about performance
    var picker5 = Math.floor(Math.random() * times); // Randomly pick up the data to debug. No worries about performance
    
    
    // === Question 1 === //

    for (var i = 0; i < times; i++) {
        x = Math.random() * circleD; // Generate random x for the point
        y = Math.random() * circleD; // Generate random y for the point
        z = Math.random() * height; // Generate random z for the point

        // d = (x - trueR) * (x - trueR) + (y - trueR) * (y - trueR); //[Backup Method] THIS IS THE METHOD 2. CURRENTLY USING METHOD 1
        // Center X and Y are all trueR.
        // \sqrt{(x-trueR)^2+(y-trueR)^2} in JavaScript can not be calculated by one equation. We have to introduce the Math.sqrt() method.

        var distanceWithoutSqrt = (x - trueR) * (x - trueR) + (y - trueR) * (y - trueR); 
        var distanceToCenter = Math.sqrt(distanceWithoutSqrt); // Calculate the distance from the point to the center

        //if (d < trueRDouble) { // [Backup Method] THIS IS THE METHOD 2. CURRENTLY USING METHOD 1
        if (distanceToCenter <= trueR) { // See if the point is greater than the radius or not
            if (0 < z < height) { // If the x and y check is passed, let us check z
                counter += 1; // Bingo! Now add the counter
                // document.getElementById("resultdiv").innerHTML += ""+x+","+y+","+z+"<br>";
            }
        }

        if (i == picker1 || i == picker2 || i == picker3 || i == picker4 || i == picker5) { // Match the random pick point to debug
            console.log("x: " + x + " y: " + y + " z: " + z + " d: " + d); // Print out the debug message to the console
        }
        
        // document.getElementById("resultdiv").innerHTML += ""+x+","+y+","+z+"<br>";
    }
    
    
    // === Question 2 === //
    
    var equationVolume = 2 * Math.PI * Math.PI * outerR * trueR * trueR; // A simple equation to get the volume
    
    
    // === Calculation / Debug Output === //
    
    var resultPosibility = counter / times; // Calculate the posibility to get in the shape
    var result = (trueR * 2) * (trueR * 2) * height * resultPosibility; // Calculate the volume 
    var rawRatio = equationVolume / result; // Just the ratio. Preparing for the percentage format.
    var resultRatio = (rawRatio) * 100; // Multiply by 100 to give it a percentage number! We will add the '%' later on
    console.log("trueR: " + trueR + " Pi: " + Math.PI + " height: " + height + " resultPosibility: " + resultPosibility + " counter: " + counter + " result: " + result); // Debug message to help us find the problem
    document.getElementById("TitleWrite").innerHTML = "Calculation result of program 'inner radius "+interR+", outer radius "+outerR+" and random for "+times+" times'"; // Write the title to the message box - modal
    document.getElementById("ResultWrite").innerHTML = result.toFixed(8); // Fix 8 decimals and then write the result
    document.getElementById("EVWrite").innerHTML = equationVolume.toFixed(4); // Fix 4 decimals and then write the equation volume result
    document.getElementById("RatioWrite").innerHTML = resultRatio.toFixed(4) + "%"; // Fix 4 decimals and then write the ratio
    
    // And we finally done - with calculations!
}