function cityAlert(){
    alert("Loading weather report...");
}

function acceptCookies(){
    var cookieBox = document.getElementById('alert');
    cookieBox.parentNode.removeChild(cookieBox);
}

/* 
var highTempCel = document.getElementById('high-temp').innerText;
console.log(highTempCel);
highTempCel = parseFloat(highTempCel);
console.log(highTempCel);

var highTempFar = ((highTempCel)*1.8+32)
console.log(highTempFar)

function changeTemp(){
    if (document.getElementById('celcius').value == '&#8451'){

    }
    else{
    document.getElementById('high-temp').innerHTML = highTempFar + '&#176';
}
}
*/


function c2f(temp) {
    return Math.round(9 / 5 * temp + 32);
}

function f2c(temp) {
    return Math.round(5 / 9 * (temp - 32));
}

function changeTemp(element) {
    console.log(element.value);
    for(var i=1; i<9; i++) {
        var spanNum = document.querySelector("#temp" + i);
        var tempVal = parseInt(spanNum.innerText);
        if(element.value == "°C") {
            spanNum.innerText = f2c(tempVal);
        } else {
            spanNum.innerText = c2f(tempVal);
        }
    }
}