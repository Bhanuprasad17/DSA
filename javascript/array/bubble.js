

let arr = [5, 3, 8, 4, 2]

n = arr.length

for(let i=0;i<arr.length;i++){
    let swape = false
    for(let j=0;j<arr.length-i-1;j++){
        if(arr[j] > arr[j+1]){
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            swape = true
        }
    }
    if(!swape){
        break
    }
}

console.log(arr)


