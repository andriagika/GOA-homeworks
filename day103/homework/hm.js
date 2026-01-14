let a = 10;
let b = 20;

console.log(a > b);   // false
console.log(a < b);   // true
console.log(a >= b);  // false
console.log(a <= b);  // true
console.log(a == b);  // false
console.log(a === b); // false  
console.log(a != b);  // true
console.log(a !== b); // true

let age = 17;

if (age < 18) {
    console.log("You are underaged");
} else {
    console.log("You are adult");
}


let isStudent = true;
let hasAccess = false;

console.log(isStudent && hasAccess);
console.log(isStudent || hasAccess);
console.log(!isStudent);          

let testCases = [
    {isStudent:true, hasAccess:true},
    {isStudent:true, hasAccess:false},
    {isStudent:false, hasAccess:true},
    {isStudent:false, hasAccess:false}
];

for (let caseItem of testCases){
    console.log(`isStudent: ${caseItem.isStudent}, hasAccess: ${caseItem.hasAccess} Can enter? ${caseItem.isStudent && caseItem.hasAccess}`);
}

let score = 85;

if (score >= 90) {
    console.log("A");
} else if (score >= 70) {
    console.log("B");
} else if (score >= 50) {
    console.log("C");
} else {
    console.log("F");
}

let password = "MyPass123";
let confirmPassword = "MyPass123";

if (password === confirmPassword && password.length >= 8) {
    console.log("Password accepted");
} else if (password !== confirmPassword) {
    console.log("Passwords do not match");
} else if (password.length < 8) {
    console.log("Password too short");
}

let num1 = 15;
let num2 = 5;

console.log(num1 > 10 && num2 > 10); // false
console.log(num1 > 10 || num2 > 10); // true

let dayNumber = 3;

if (dayNumber === 1) console.log("monday");
else if (dayNumber === 2) console.log("thuesday");
else if (dayNumber === 3) console.log("wensday");
else if (dayNumber === 4) console.log("thurthday");
else if (dayNumber === 5) console.log("friday");
else if (dayNumber === 6) console.log("saturday");
else if (dayNumber === 7) console.log("sunday");
else console.log("Invalid day");

let username = "Tom";
if (!username) {
    console.log("Username is required");
} else if (username.length < 4) {
    console.log("Username is too short");
} else {
    console.log("Username accepted");
}

let isLoggedIn = false;

if (!isLoggedIn) {
    console.log("Please log in");
}

console.log(5 == "5");   // true

console.log(5 === "5");  // false

console.log(true && false); // false

console.log(true || false); // true

let temp = 25;

if (temp < 0) {
    console.log("Freezing");
} else if (temp <= 20) {
    console.log("Cold");
} else if (temp <= 30) {
    console.log("Warm");
} else {
    console.log("Hot");
}
