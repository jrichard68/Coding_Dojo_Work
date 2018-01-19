function countPositives(arr) {
    var counter = 0;
    for(var i = 0; i < arr.length; i ++){
        if(arr[i] > 0) {
            counter ++;
        }
        arr[(arr.length-1)] = counter;
    }
    return arr;
}

function isEqual(arr1, arr2) {

    if (arr1.length !== arr2.length) {
        return false;
    }
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }

    return true;
}

console.log("has expected result:", isEqual(countPositives([0, -1, 1, -1, 1]), [0, -1, 1, -1, 2]));
