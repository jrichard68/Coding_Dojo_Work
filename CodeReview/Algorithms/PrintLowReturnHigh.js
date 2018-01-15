function lowHigh(arr) {
    var highestNum  = arr[0];
    var lowestNumber = arr[0];

    for(var i = 1; i < arr.length; i++) {
        if(arr[i] < lowestNumber) {
            lowestNumber = arr[i];
        }
        if(arr[i] > highestNum) {
            highestNum = arr[i];
        }
    }

    console.log("lowNum:", lowestNumber);
    return highestNum;
}

// var returned = lowHigh([2, 3, 5, 1, 3]); // print 1, return 5
// console.log("returned:", returned);
var myArr = [1, 2, 3, 5, 6, 2, 7]; // print 1, return 7
console.log("returned highNum:", lowHigh(myArr));