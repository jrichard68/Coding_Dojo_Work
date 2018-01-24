
function slots(numQuarters) {
    var winningNum = Math.floor(Math.random() * 100);
    var winNumCoins = Math.floor(Math.random() * 50)+50;
    while(numQuarters > 0){
        if(winningNum === 1) {
            return winNumCoins + numQuarters;
        }
        numQuarters = numQuarters - 1;
    }
    return 0;
}

console.log(slots(45));