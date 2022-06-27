
setTimeout(function(){
    alert("The Ninjas have won!");
    },
    13000);

var ninjaScore = 314;

function clickNinja(){
    ninjaScore++
    document.querySelector('.ninja-score').innerText = ninjaScore
}

var pirateScore = 159;

function clickPirate(){
    pirateScore++
    document.querySelector('.pirate-score').innerText = pirateScore
}

function removeSubscribe() {
    var subBox = document.getElementById('subscribeBox');
    subBox.parentNode.removeChild(subBox);
}