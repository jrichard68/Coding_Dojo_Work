function printRange(startPoint, endPoint, skipAmount){
    for(var i = startPoint; i < endPoint; i+=skipAmount) {
        console.log(i);
    }
}

printRange(2, 10, 2);



function printRangeBonus(startPoint, endPoint, skipAmount){
    if(!skipAmount){
        skipAmount = 1;
    }
    if(!endPoint){
        endPoint = startPoint;
        startPoint = 0;
    }
    for(var i = startPoint; i < endPoint; i+=skipAmount) {
        console.log(i);
    }
}

printRangeBonus(4, 8);
printRangeBonus(4);