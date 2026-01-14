const languages = ["JavaScript", "Python", "HTML", "CSS", "C++"];
console.log(languages[0]);
console.log(languages[1]);
console.log(languages[2]);
console.log(languages[3]);
console.log(languages[4]);
for (let i = 0; i < languages.length; i++) {
  console.log(languages[i]);
}

const numbers = [-5, 10, -3, 7, 0, 15, -1];
let positiveSum = 0;
for (let num of numbers) {
  if (num > 0) {
    positiveSum += num;
  }
}
console.log("Positive numbers sum:", positiveSum);

const list1 = [1, 5, 8, 10, 3];
const list2 = [8, 3, 12, 5, 7];
const mutualNums = [];
for (let num of list1) {
  if (list2.includes(num)) {
    mutualNums.push(num);
  }
}
console.log(mutualNums);
