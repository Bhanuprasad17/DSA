


const arr = [1,2,3,4,5]

let left = 0
let right = arr.length - 1

while(left < right){
    // arr[left],arr[right] = arr[right],arr[left]
    let temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left += 1
    right -= 1
}

console.log(arr)
console.log(left,right)