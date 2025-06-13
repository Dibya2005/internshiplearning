
function calculator(a,b,d){
  let c
  if(d=="+"){
    c=a+b
    console.log(`${a}+${b}=${a+b}`)
  }
  else if(d=="-")
  {
        c=a-b
    console.log(`${a}-${b}=${a-b}`)

  }
    else if(d=="*")
  {    c=a*b
    console.log(`${a}*${b}=${a*b}`)
    
  }
    else if(d=="/")
  {    c=a/b
    console.log(`${a}/${b}=${a/b}`)
    
  }
  else{
    Print("enter a valid operator")
  }

}
let a=parseInt(prompt("enter the first operand"))
let b=parseInt(prompt("enter the second operand"))
let c=prompt("enter the operator")
calculator(a,b,c)