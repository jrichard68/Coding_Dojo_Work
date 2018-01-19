function evensOdds (arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 != 0){
            if(arr[i+1] % 2 != 0){
                if(arr[i+2] % 2 != 0){
                    console.log("That's odd.");
                }
            }
        }
        if(arr[i] % 2 == 0){
            if(arr[i+1] % 2 == 0){
                if(arr[i+2] % 2 == 0){
                    console.log("Even more so!");
                }
            }
        }
        else {
            console.log("neither 3 sequential odd values nor 3 sequential even values exist in this array")
        }
    }
}

evensOdds([1, 9, 10, 5, 2, 5, 6]);