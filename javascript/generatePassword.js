// let num = Math.random()  // 0(inclusive) to 1(exclusive)
// let num2 = Math.random() * 10
// let num3 = Math.floor(Math.random() * 10)

// console.log(num)
// console.log(num2)
// console.log(num3)

// const passwordSet ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";

// const n = passwordSet.length;
// const randomNum = Math.floor(Math.random() * n);
// console.log(randomNum);
// console.log(passwordSet[randomNum]);

// let generatedPassword = ''

// for (let i = 0; i < 10; i++) {
//     const randomNum = Math.floor(Math.random() * n);
//     generatedPassword += passwordSet[randomNum]
// }

// console.log(generatedPassword)

// 1️⃣ Random Number in a Range

function getRandomInt(min,max){
    // console.log(min,max)
    // console.log(Math.floor(Math.random() * (max - min + 1))) // it will give 1 - 5 random num
    console.log(Math.floor(Math.random() * (max - min+ 1 )) + min)
}

getRandomInt(5,10)

// 4️⃣ OTP Generator

// function generateOpt(length) {
//   let opt = "";
//   for (let i = 0; i < length; i++) {
//     opt += Math.floor(Math.random() * 10)
//   }
//   return opt
// }

// console.log(generateOpt(6))


// 6️⃣ Dice Roll Simulator

// function rollDice(){
//     return Math.floor(Math.random() * 6) + 1
// }

// console.log(rollDice())


// 🔟 Random Password with Specific Rules

// function securePassword(length){
//   const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
//   const lower = "abcdefghijklmnopqrstuvwxyz";
//   const nums = "0123456789";
//   const symbols = "!@#$%^&*()_+";


// //   console.log(upper,lower,nums,symbols)
//   const allChars = upper + lower + nums + symbols
//   const password = [
//     upper[Math.floor(Math.random() * upper.length)],
//     lower[Math.floor(Math.random() * lower.length)],
//     nums[Math.floor(Math.random() * nums.length)],
//     symbols[Math.floor(Math.random() * symbols.length)]
//   ]

// // console.log(length - password.length)
 
//   for(let i = length - password.length ; i > 0 ;i--){
//     password.push(allChars[Math.floor(Math.random() * allChars.length)])
//   }

//   return password.join('')

// }

// console.log(securePassword(10))

