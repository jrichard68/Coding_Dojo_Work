
function slots(numQuarters) {
   
    
    
    while(numQuarters > 0){
        var winningNum = Math.floor(Math.random() * 100);
        if(winningNum === 1) {
            var winNumCoins = Math.floor(Math.random() * 50)+50;
            console.log("You have", numQuarters, "quarters left");
            return winNumCoins + numQuarters;
        }
        numQuarters = numQuarters - 1;
    }
    return 0;
}

console.log(slots(45));