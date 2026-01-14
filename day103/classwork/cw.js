let age = 15; 
if (age < 10) {
    console.log("Child");
} else if (age < 18) {
    console.log("Teen");
} else {
    console.log("Adult");
}

let randomNum = Math.floor(Math.random() * 101); 
console.log("Generated number:", randomNum);

if (randomNum < 50) {
    console.log(false);
} else if (randomNum > 50) {
    console.log(true);
} else {
    console.log("Exactly 50");
}

let var1 = 10;
let var2 = "10";

console.log("var1 === var2:", var1 === var2);

let var3 = 20;
let var4 = 20;

console.log("var3 === var4:", var3 === var4);
