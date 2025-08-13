


// for(let i=0;i<)

let count = 1
for(let i=0;i<5;i++){
    let star = ""
    for(let j=0;j<1+i;j++){
        if((i+1)%2 == 0){
          star =   String(count) + " " + star 
        }
        else{
          star =  star + String(count) + " "   
        }
      let temp = count+1
      while(is_prime(temp)){
          temp = temp + 1
      }
      count = temp
    }
    console.log(star)
}

function is_prime(num){
    for(let i=2;i<num;i++){
        if(num % i == 0 ){
            return false
        }
    }
    return true
}

// console.log(is_prime(5))
// console.log(is_prime(2))