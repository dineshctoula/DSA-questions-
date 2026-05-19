function findLargest(arr){
    let max=arr[0];
    for(let i=1; i<arr.length; i++){
        if(arr[i]>max)
        {
            max=arr[i];
        }
    }
    return max;
}
console.log("The largest number in the array is:", findLargest([3, 5, 7, 2, 8]));