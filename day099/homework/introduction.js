// 2) მეთოდები გვჭირდება იმისთვის, რომ ობიექტებზე ან მონაცემებზე გარკვეული მოქმედებები მარტივად შევასრულოთ.
// toUpperCase(), toLowerCase(), startsWith(), endsWith(), trim(), concat(), Math.random(), Math.floor(), Math.round()

let word = "javascript";
console.log(word.toUpperCase());

let text = "HELLO WORLD";
console.log(text.toLowerCase());

let sunrise = "Sunrise";
console.log(sunrise.startsWith("Sun"));

let academy = "GOA Martial Arts";
console.log(academy.endsWith("S"));

console.log("Hello".endsWith("o"));      
console.log("document.pdf".endsWith("pdf"));
console.log("programming".endsWith("ing"));

let str1 = "     test";
let str2 = "test      ";

console.log(str1.trim());
console.log(str2.trim());

let a = "Hello";
let b = "World";

console.log(a.concat(" ", b));

let part1 = "Goal";
let part2 = "Oriented";
let part3 = "Academy";

console.log(part1.concat("-", part2, " ", part3));

let num1 = Math.random();
let num2 = Math.random();

console.log(num1 + num2);
console.log(num1 - num2);
console.log(num1 * num2);
console.log(num1 / num2);
console.log(num1 % num2);

Math.floor(4.9);
Math.floor(4.1);

let randomNum = Math.floor(Math.random() * 51);
console.log(randomNum);

let randomNum2 = Math.floor(Math.random() * 72);
console.log(randomNum2);

// მეთოდი - Math.round()