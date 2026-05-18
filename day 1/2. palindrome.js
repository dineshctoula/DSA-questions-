function checkPalindrome(str){
    let result = "";

    for(let i = str.length-1; i >= 0; i--){
        result = result + str[i];
    }

    return result == str;
}

console.log("The checked palindrome is:", checkPalindrome("madam"));