function slots(numQuarters) {
     while(numQuarters > 0){
        var winningNum = Math.floor(Math.random() * 100);
        if(winningNum == 1) {
            var winNumCoins = Math.floor(Math.random() * 50)+50;
            return winNumCoins + numQuarters;
        }
        else {
            numQuarters = numQuarters - 1;
        }
    }
    return 0;
}

slots(45);