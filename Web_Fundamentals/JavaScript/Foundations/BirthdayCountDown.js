var daysUntilMyBirthday = 60;

while (daysUntilMyBirthday <= 0) {
    if(daysUntilMyBirthday > 30) {
        console.log(daysUntilMyBirthday + " days until my birthday. Such a long time... :(");
    }
    else if (daysUntilMyBirthday <= 30 && daysUntilMyBirthday >= 5) { 
        console.log(daysUntilMyBirthday + " days until my birthday. I'm getting excited!");
    } 
    else if (daysUntilMyBirthday < 5 && daysUntilMyBirthday > 0) {
        console.log(daysUntilMyBirthday + " days until my birthday. Scream it!");
    }
    else if (daysUntilMyBirthday === 0) {
        console.log("My birth is today.  Let's party!");
    }
    daysUntilMyBirthday = daysUntilMyBirthday - 1;
}