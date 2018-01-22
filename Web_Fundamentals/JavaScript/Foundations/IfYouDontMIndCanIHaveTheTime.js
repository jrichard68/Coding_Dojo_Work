var hour = 8;
var minute = 50;
var period = "AM";

if(hour < 9 && minute >= 50 && period == "AM"){
    console.log("It's almost 9 in the morning.");
}
var hour = 7;
var minute = 15;
var period = "PM";

if(hour == 7 && minute <= 15 && period == "PM"){
    console.log("It's just after 7 in the evening.");
}
if(minute < 30){
    console.log("It's just after the hour.");
}
if(minute > 30){
    console.log("It's almost the next hour.");
}
if(period == "AM"){
    console.log("It's in the morning.")
}
if(period == "PM"){
    console.log("It's in the evening.")
}