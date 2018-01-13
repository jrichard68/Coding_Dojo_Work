var highest_num  = arr[0];
var arr= [];
var lowest_number = arr[0]

function low_high() {
    for(var=1; i<arr.length-1; i++) {
        if(arr [i] < lowest_number) {
            lowest_number=arr[i];
        }
        if(arr[i]>highest_num) {
            highest_num = arr[i];
        }
    }
    return highest_num;
    console.log(lowest_number);
}