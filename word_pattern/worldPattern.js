var wordPattern = function(pattern, str) {
    let arr = str.split(" "),
        keysPattern = {},
        valuesPattern = {};
        hasPattern = true;
    
    if (arr.length !== pattern.length)
        return false;
    
    for (let index = 0; index < pattern.length; ++index) {
        if (keysPattern.hasOwnProperty(pattern[index]) || valuesPattern.hasOwnProperty(arr[index])) {
            if (keysPattern[pattern[index]] !== arr[index]) {
                hasPattern = false;
                break;
            }
            
            if (valuesPattern[arr[index]] != pattern[index]) {
                hasPattern = false;
                break;
            }
        }
        else {
            keysPattern[pattern[index]] = arr[index];
            valuesPattern[arr[index]] = pattern[index];
        }
    }
    
    return hasPattern;
};