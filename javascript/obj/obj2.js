

const user = {
    name : 'Bhanuprasad',
    age : 21
}

const admin = {
    admin : true,...user
}

console.log(admin)

const setting = {
    username : 'Bhanu',
    level : 19,
    health : 90
}

const data = JSON.stringify(setting, ['level','health'])

console.log(data)


// ---------------------------------------------------------------------------

const shape = {
    radius : 10,
    diameter() {
        return this.radius * 2
    },
    perimeter : () => 2 * Math.PI * this.radius
}

console.log(shape.diameter())
console.log(shape.perimeter())


// ------------------------------------------------------------------------


const user4 = {
    name : 'Bhanu',
    age : 24,
    fullName : {
        first : 'Bhanu',
        last : 'Agarwal'
    }
};

// const name = 'jai'
// const {name : myName} = user4
// console.log(name)
// console.log(myName)

const {fullName : first} = user4

console.log(first)