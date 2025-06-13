function no_of_vowel(str){
  let count=0
  vowels="aeiouAEIOU"

  for(let char of str){
    if(vowels.includes(char)){
      count++
    }
  }
  return count
}
let input=prompt("enter a string")
k=no_of_vowel(input)
console.log(`no of vowel ${k}`)