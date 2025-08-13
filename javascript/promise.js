


const promise = new Promise((resolve,reject) =>{
    // resolve('done')
    reject('failed')
})


promise
.then(()=>{
    console.log('successfully resolved')
})
.catch(()=>{
    console.log('rejected')
})