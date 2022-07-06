//Always Hungry

function alwaysHungry(arr) {
    var foodCount = 0;
    for (i=0; i<arr.length; i++){
        if (arr[i] == "food"){
            console.log("yummy");
            foodCount++;
            }
        }
        if (foodCount == 0){
            console.log("I'm hungry!");
        }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);

//High Pass Filter

function highPass(arr, cutoff) {
    var filteredArr = [];
        for(i=0; i<arr.length; i++){
            if (arr[i]> cutoff){
                filteredArr.push(arr[i]);
            }
        }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);

// Better than Average

function betterThanAverage(arr) {
    var sum = 0;

    for (i=0; i<arr.length; i++){
        sum = sum + arr[i];
    }

    var average = sum/arr.length; 

    var count = 0;

    for (i=0; i<arr.length; i++){
        if (arr[i]>average){
            count++;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); 


//Array Reverse

function reverse(arr) {
    var left = 0;
    var right = arr.length -1;

    while (left<right){
        var temp = arr[left];
        arr[left]=arr[right];
        arr[right]=temp;
        left++;
        right--;
    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);

//Fibonacci Array

function fibonacciArray(n) {

    var fibArr = [0, 1];
        while(fibArr.length < n){
            var prev=fibArr[fibArr.length-1];
            var prevprev=fibArr[fibArr.length-2];
            fibArr.push(prev + prevprev);
        }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result);



