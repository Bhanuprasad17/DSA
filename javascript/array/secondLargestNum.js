let arr = [3, 1, 4, 1, 5, 9];

function largestNum(arr) {
  let largest = arr[0]

  for (let i = 0; i < arr.length; i++) {

    if(arr.length == 0){
        return 
    }

    if(arr[i] > largest){
        largest = arr[i]
    }
  }

  return largest
}


console.log(largestNum(arr))
console.log(largestNum([]))



