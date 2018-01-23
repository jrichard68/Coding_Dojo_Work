function numbersOnly(arr){
    var new_array = [];
    for(var i = 0; i < arr.length; i++){
        if(typeof(arr[i]) == "number") {
            new_array.push(arr[i])
        }
    console.log(new_array);
    return new_array;
    }
}
numbersOnly([1, "apple", -3, "orange", 0.5]);