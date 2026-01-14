let score = Number(prompt("შეიყვანეთ ქულა (0-100):"));

switch (true) {
    case (score >= 90 && score <= 100):
        console.log("A");
        break;
    case (score >= 80 && score <= 89):
        console.log("B");
        break;
    case (score >= 70 && score <= 79):
        console.log("C");
        break;
    case (score >= 60 && score <= 69):
        console.log("D");
        break;
    case (score >= 0 && score <= 59):
        console.log("F");
        break;
    default:
        console.log("invalid score");
}

for (let i = 1; i <= 10; i++) {
    console.log(i);
}

for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}

for (let i = 1; i <= 5; i++) {
    console.log(i * i);
}

for (let i = 35; i >= 15; i--) {
    console.log(i);
}

// Loop-ის გამოყენების დადებითი მხარეები:
//გამარტივება: ერთი და იგივე ოპერაციის გამეორება მარტივად.
//ნაკლები კოდი: არ გვიწევს ყოველი ნაბიჯის ინდივიდუალური წერება
//შეცდომების შემცირება.


// for Init; Condition; Increment/Decrement

for (let i = 1; i <= 150; i++) {
    console.log("Group 71 is the best");
}

let firstName = prompt("enter your name:");
let lastName = prompt("enter your surname:");

for (let i = 1; i <= 10; i++) {
    console.log(`User info: ${firstName} ${lastName}`);
}
