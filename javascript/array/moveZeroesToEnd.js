

function moveZeroesToEnd(arr){
    let position = 0

    for(let current = 0 ; current < arr.length ; current++){
        if(arr[current] != 0){
            arr[position] = arr[current]
            position ++
        }
    }


    while (position < arr.length){
        arr[position] = 0
        position ++
    } 

    return arr
}

console.log(moveZeroesToEnd([0, 1, 0, 3, 12]))