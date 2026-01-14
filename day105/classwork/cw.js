// truthly :
// 1
// -1
// "hello"
// []
// {}
// true
// 42

// falesly :
// 0
// ""
// null
// undefined
// NaN
// false


let adminInput = prompt("Are you admin? (yes/no)");
let isAdmin = (adminInput.toLowerCase() === "yes") ? true : false;
console.log(isAdmin);

let greetMsg = isAdmin || false ? "Admin" : "user"; 
greetMsg = isAdmin ? "Admin" : "user";
console.log(`Hello, ${greetMsg}`);

