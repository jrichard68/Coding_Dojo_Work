function doubleVision(arr) {
    var newArr = []

    for(var i = 0; i < arr.length; i ++) {
        newArr.push(arr[i] *2);
    }
    console.log(newArr);
    return newArr;
}

console.log(doubleVision([1,2,3]))