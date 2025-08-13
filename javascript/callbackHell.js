



function f1(callback){
    setTimeout(()=>{
        console.log('f1')
        callback()
    },1000)
}


function f2(callback){
    setTimeout(()=> {
        console.log('f2')
        callback()
    },1000)
}

function f3(callback){
    setTimeout(()=>{
        console.log('f3')
        callback()
    },1000)
}

function callbackHell(){
    f1(()=>{
        f2(()=>{
            f3(()=>{
                console.log("Done")
            })
        })
    })
}

callbackHell()