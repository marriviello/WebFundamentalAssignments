//City Alert
function cityAlert(){
    alert("Loading weather report...");
}

//Accept Cookies
function acceptCookies(){
    var cookieBox = document.getElementById('alert');
    cookieBox.parentNode.removeChild(cookieBox);
}

// Temperature Change

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
        var tempVal = parseFloat(spanNum.innerText);
        console.log(spanNum);
        console.log(tempVal);
        if(element.value == "celcius") {
            spanNum.innerText = f2c(tempVal) + "°";
        } else {
            spanNum.innerText = c2f(tempVal) + "°";
        }
    }
}