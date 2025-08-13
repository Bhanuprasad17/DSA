


const user = {
    name : 'Bhanu',
    greet : function (age,country){
        console.log(`Hi I'm ${this.name}, age ${age} years old from ${country}`)
    }
}

const anotherUser = {
    name : 'Ravi'
}

// user.greet.call(anotherUser,25,"india")
// user.greet.apply(anotherUser, [26, "India"]);

const boundGreet = user.greet.bind(anotherUser,41,"India")
boundGreet()
