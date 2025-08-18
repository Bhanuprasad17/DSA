


function peakElement(arr){
    // console.log(arr)
    n = arr.length

    let peaks = []

    for(let i=0;i<n;i++){
        // console.log(arr[i])
        left = i > 0 ? arr[i - 1] : -Infinity
        right = i < n - 1 ? arr[i+1] : -Infinity
        // console.log(`${left} ${right} and current ${arr[i]}`)

        if(arr[i] >= left && arr[i] >= right){
            peaks.push(arr[i])
        }
    }

    return peaks
}


console.log(peakElement([1, 3, 20, 4, 1, 0]))
console.log(peakElement([5, 10, 5, 20, 15, 25, 10]))