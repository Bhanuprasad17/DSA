
// First Largest Num

function largestNums(arr){

    if(arr.length == 0){
        return null
    }

    let largest_num = -Infinity
    for(let i of arr){
        if(largest_num < i){
            largest_num = i
        }
    }

    return largest_num
}


console.log(largestNums([3,1,4,5,9]))