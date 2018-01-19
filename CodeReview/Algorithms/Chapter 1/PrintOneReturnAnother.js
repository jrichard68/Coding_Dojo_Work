function printReturn (arr) {
    for(var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 != 0) {
            console.log (arr[arr.length-1]);
            return arr[i];
        }
    }
}

var myArr = [1,2,3,4,5,6,7,8];
console.log("returned first odd value:", arr[i], "second-to-last value:", arr[arr.length-1]);
