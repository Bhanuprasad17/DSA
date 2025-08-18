

let arr = [1, 2, 2, 3, 4, 4, 5]


function findUniqueElements(arr){
    dict = {}

    for(let num of arr){
        if(dict[num]){
            dict[num] = dict[num] + 1
        }else{
            dict[num] = 1
        }
    }

    let result = []

    for(let key in dict){
        if(dict[key] == 1){
            result.push(Number(key))
        }
    }

    // return dict
    return result
}

console.log(findUniqueElements([1, 2, 2, 3, 4, 4, 5]))

