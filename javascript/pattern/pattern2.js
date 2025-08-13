for (let i = 0; i < 5; i++) {
    let star = "";
    
    for (let k = 0; k < i; k++) {
        star = star + " ";
    }
    
    for (let j = 0; j < 5 - i; j++) {
        star = star + "* ";
    }

    console.log(star);
}
