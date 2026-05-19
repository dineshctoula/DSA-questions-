function twoSum(arr, target) {
  for (let i = 0; i < arr.length; i++) {

    for (let j = i + 1; j < arr.length; j++) {

      if (arr[i] + arr[j] === target) {
        return [i, j];
      }

    }
  }
}

console.log(twoSum([1,2,3], 4));

// pahila first element line  
// j=i+1 bata start garne second element lai line
// if condition le check garne ki first element ra second element ko sum target sanga equal cha ki nai
// if condition true bhaye return garne index of first element and second element in array form     