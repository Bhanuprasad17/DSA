
// First Largest Num

// function largestNums(arr){

//     if(arr.length == 0){
//         return null
//     }

//     let largest_num = -Infinity
//     for(let i of arr){
//         if(largest_num < i){
//             largest_num = i
//         }
//     }

//     return largest_num
// }


// console.log(largestNums([3,1,4,5,9]))


// function secondLargest(arr){
//     if(arr.length < 2){
//         return null
//     }

//     first = -Infinity
//     second = -Infinity
    
//     for(let num of arr){
//         if(first < num){
//             second = first
//             first = num
//         }else if(second < num && second < first){
//             second = num
//         }
//     }

//     return {first,second}
// }

// console.log(secondLargest([3,1,4,5,9]))

function thirdLargestNum(arr) {
    if (arr.length < 3) {
        return null; // Not enough elements
    }

    let first = -Infinity;
    let second = -Infinity;
    let third = -Infinity;

    for (let num of arr) {
        if (num > first) {
            // Shift all down
            third = second;
            second = first;
            first = num;
        } else if (num > second && num < first) {
            // Shift second and third
            third = second;
            second = num;
        } else if (num > third && num < second) {
            // Update only third
            third = num;
        }
    }

    return { first, second, third };
}

console.log(thirdLargestNum([3, 1, 4, 5, 9]));
console.log(thirdLargestNum([10, 20, 30, 40, 50]));