


// console.log(this)


const person = {
    name : "Bhanu",
    greet : function(){
        console.log(this.name)
    }
}

person.greet()

let name = 'outerobj'
function show(){
//    console.log(this)
}
show()


let obj = {
    name : "dell",
    getName : () =>{
        console.log(this.name)
    }
}

obj.getName()


// constructor function

function Person(name){
    this.name = name
}

let objPerson = new Person('Kohli') 
console.log(objPerson.name)
