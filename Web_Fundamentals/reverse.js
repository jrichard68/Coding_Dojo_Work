function FirstReverse(str) { 

    var newStr = "";
    
    for(var i=str.length-1; i>=0; i--);{
        newStr = newStr + str.charAt(i);
    }
    
  // code goes here  
  return newStr; 
         
}
FirstReverse("love");
console.log(FirstReverse("love"));
