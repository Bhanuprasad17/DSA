

function is_prime(num){
    if (num <= 1 ){
        return false
    }
    for(let i=2;i<num;i++){
        if(num % i == 0){
            return false
        }
    }
    return true
}


console.log(is_prime(5))
console.log(is_prime(1))