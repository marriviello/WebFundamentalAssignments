/*
var likesCount = [0, 0, 0]
var likesNow = [
    document.querySelector("#like-count1"),
    document.querySelector("#like-count2"),
    document.querySelector("#like-count3")
]

console.log(likesCount, likesNow);
*/


/*
var count = 1;
var countElement = document.querySelector("#like-count");

console.log(countElement);

function add1(){
    count++;
    countElement.innerText = count;
    console.log(count);
}
*/

var neil = 0
function likeNeil(){
    neil++
    document.querySelector('#like-count1').innerText = neil
}

var nichole = 0
function likeNichole(){
    nichole++
    document.querySelector('#like-count2').innerText = nichole
}

var jim = 0
function likeJim(){
    jim++
    document.querySelector('#like-count3').innerText = jim
}