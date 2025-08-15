
const user = {
    name : 'bhanu',
    age : 24,
    isMale : true
}

Object.keys(user).forEach(key =>{
    console.log(key)
})


Object.values(user).forEach(value =>{
    console.log(value)
})


Object.entries(user).forEach(([key,value] )=>{
    console.log(`${key} : ${value} `)
})


