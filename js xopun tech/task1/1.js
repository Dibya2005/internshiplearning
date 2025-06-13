
let num = parseInt(prompt("Enter a number:"));


function multiplicationTable(n) {
  for (let i = 1; i <= 10; i++) {
    console.log(`${n} x ${i} = ${n * i}`);
  }
}


multiplicationTable(num);