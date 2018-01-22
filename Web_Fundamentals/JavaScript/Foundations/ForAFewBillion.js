
var rewardTotal = 0.01;
var dailyAmount = 0.01;
for(var i = 2; i < 31; i++){
    dailyAmount = dailyAmount * 2;
    rewardTotal = rewardTotal + dailyAmount;
}
console.log("The reward after 30 days was $", rewardTotal);

while (i < 100000000) {
    dailyAmount = dailyAmount * 2;
    rewardTotal = rewardTotal + dailyAmount;
        if(rewardTotal >= 10000) {
            console.log("It took the servant", i, "days to make $10,000.");
            break;
        }
    i++;
}
while (i < 100000000) {
    dailyAmount = dailyAmount * 2;
    rewardTotal = rewardTotal + dailyAmount;
        if(rewardTotal >= 1000000000) {
            console.log("It took the servant", i, "days to make $1,000,000,000.");
            break;
        }
    i++;
}
while (i < 100000000) {
    dailyAmount = dailyAmount * 2;
    rewardTotal = rewardTotal + dailyAmount;
        if(rewardTotal == Infinity) {
            console.log("It took the servant", i, "days to make infinity dollars.");
            break;
        }
    i++;
}
