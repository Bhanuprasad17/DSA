
for(let i=0;i<5;i++){
    let star = ""
    
    for(let k=0;k<5-i;k++){
        star = star + " "
    }
    
    for(let j=0;j<i+1;j++){
        star += "* "
    }
    console.log(star)
}

for(let i =0;i<4;i++){
    let star = ""
    
    for(let k=0;k<i+2;k++){
        star = star + " "
    }
    
    for(let j=0;j<4-i;j++){
        star = star + "* "
    }
    console.log(star)
}