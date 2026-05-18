// reverse of a string 


function reverseString(str)
{
    // parenthesis ko str chae hamro input string ho 
    let result="";
    for (let i=str.length-1;i>=0; i--){
        result=result+str[i];
    }
    return result;
}
console.log(reverseString("dinesh"));

// yo mathi ko chae value pass gareko  
// time complexity chae yesma o n square bho  
// space complexity channe o n bhayo  

