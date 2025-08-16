


// const user = {
//     name : 'Bhanu',
//     age : 24,
//     "i like this" : true
// }

// console.log(user)
// console.log(user.name)
// console.log(user.age)

// user.name = 'kohli'
// console.log(user)

// delete user.name

// console.log(user)
// console.log(user['i like this'])

// delete user['i like this']
// console.log(user)

// const func1 = (function (a){
//     delete a
//     return a
// })(5)

// console.log(func1)

// const property = 'firstName'
// const name = 'Bhanuprasad'

// const user2 = {
//      [property] : name
// }

// console.log(user2)
// console.log(user2.firstName)


const user3 = {
    name : 'Bhanuprasad',
    age : 24,
    isMale : true
}

// console.log(user)


for(key in user3){
    console.log(user3[key])
}


const obj = {
    a : 'one',
    b : 'two',
    a : 'three'
}

console.log(obj)



const nums = {
    a : 100,
    b : 200,
    title : "My name"
}

multiplyByTwo(nums)

function multiplyByTwo(obj){

    for(key in obj){
        if(typeof obj[key] == 'number'){
            obj[key] = obj[key] * 2
        }
    }

}

console.log(nums)


// ------------------------------------------------------------------------


// const a = {}
// const b = {key : 'b'}
// const c = {key : 'c'}

// a[b] = 123
// a[c] = 465

// // a["[Object Object]"] = 123

// console.log(a)
// console.log(a[b])


const user = {
    name : "Bhanu",
    age : 24
}

// console.log(user)

const strObj = JSON.stringify(user)
// console.log(JSON.stringify(user))
console.log(strObj)
// console.log(JSON.parse(strObj))

// const strObj = JSON.stringify(user)

// localStorage.setItem('test',strObj)

console.log([...'Bhanu'])


