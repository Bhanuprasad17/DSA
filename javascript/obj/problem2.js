

// function countProperties(obj){
//     return Object.keys(obj).length
// }

// console.log(countProperties({ a: 1, b: 2, c: 3 }))


// function isEmpty(obj){
//     return Object.keys(obj).length == 0
// }

// console.log(isEmpty({ a: 1, b: 2, c: 3 }))
// console.log(isEmpty({}))


// function listAllKeys(obj){
//     Object.keys(obj).forEach((item,index) =>{
//         console.log(item)
//     })
// }

// listAllKeys({ a: 1, b: 2, c: 3 })


// { a: 10, b: 20, c: 5 }


// function sumofNums(obj){
//    return Object.values(obj).reduce((sum,num) =>{
//         return sum + num
//     })
// }

// console.log(sumofNums({ a: 10, b: 20, c: 5 }))


const obj = { a: 1, b: 2, c: 3 }
const inverted = {}

Object.entries(obj).forEach(([key,value],index) =>{
    inverted[value] = key
    console.log(index)
})

console.log(inverted)

const salaries = { John: 500, Mary: 700, Sam: 400 };

const filtered = Object.fromEntries(Object.entries(salaries).filter(([name,value]) =>{
    return value > 500
}))

console.log(filtered)




