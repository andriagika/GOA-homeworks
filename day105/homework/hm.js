console.log(Boolean(0));          // false
console.log(Boolean(''));         // false
console.log(Boolean('Hello'));    // true
console.log(Boolean(null));       // false
console.log(Boolean(undefined));  // false
console.log(Boolean([]));         // true
console.log(Boolean({}));         // true
console.log(Boolean('0'));        // true
console.log(Boolean(NaN));        // false
console.log(Boolean(false));      // false

let age = Number(prompt("enter your age:"));
let ageGroup = (age >= 18) ? "Adult" 
              : (age >= 13 && age <= 17) ? "Teen" 
              : "Child";
console.log(ageGroup);

let number = Number(prompt("enter number:"));
let parity = (number % 2 === 0) ? "Even" : "Odd";
console.log(parity);

let loginInput = prompt("Are you logged in? (yes/no)");
let isLoggedIn = (loginInput.toLowerCase() === "yes") ? true : false;
console.log(`Is the user logged in? ${isLoggedIn}`);

const a = 298;
const b = 330;
let comparison = (a > b) ? "a is bigger" 
                 : (b > a) ? "b is bigger" 
                 : "equal";
console.log(comparison);

let mode = prompt("Enter mode (Dark/Light):").toLowerCase();
let modeMsg = (mode === "dark" && "Dark Mode On") 
            || (mode === "light" && "Light Mode On") 
            || "Unknown mode";
console.log(modeMsg);
