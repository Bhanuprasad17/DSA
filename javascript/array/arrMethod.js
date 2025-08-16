
// slice method

let fruits = ["apple","banana","cherry","date","fig"]

let newSlice = fruits.slice(1,4)

console.log(newSlice)
console.log(fruits)

// splice method

let newSplice = fruits.splice(3,1,"bhanu","parasad")

console.log(newSplice)
console.log(fruits)

// map method

let numbers = [10, 20, 30]

// const result = numbers.map((element,index,array)=>{
//     console.log(`element ${element}, index : ${index} and array : ${array}`)
// })

const result2 = numbers.map((ele,index,array) =>{
    return ele * index
})
console.log(result2,"jai")

// filter method 

const arr2 = [1,2,3,4,5,6]

const evenNums = arr2.filter((ele,index,array) =>{
    return ele % 2 == 0
})

console.log(evenNums)


// reducer 

const arr3 = [1,2,3,4]

const sum = arr3.reduce((sum,num) =>{
    return sum + num
},0)

console.log(sum)

// find method

const users = [
    {id : 1, name : "dell"},
    {id : 2, name : "bhanu"},
    {id : 3, name : "prasad"},
]


const foundUser = users.find((user,index) => {
    return user.name == 'bhanu'
})

console.log(foundUser)


const nums = [1,10,2,30] 


const value = nums.find((ele,index) =>{
    return ele >= 10
})

console.log(value)


// foreach

const arr = [1,2,3]

arr.forEach((ele,index,array) =>{
    console.log(ele)
})




