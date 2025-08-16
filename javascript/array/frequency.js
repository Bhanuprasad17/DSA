

function findFrequency(arr){
    let dict = {}
    for(let num of arr){
        if(dict[num]){
            dict[num] = dict[num] + 1
        }else{
            dict[num] = 1
        }
    }
    return dict
}

console.log(findFrequency([1, 2, 2, 3, 4, 4, 5]))