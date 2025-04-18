const input = require("fs").readFileSync("/dev/stdin").toString().trim();
const [A, B] = input.split(" ").map(Number);

const sequence = [];
let num = 1;

while (sequence.length < B) {
  for (let i = 0; i < num; i++) {
    sequence.push(num);
  }
  num++;
}

let sum = 0;
for (let i = A - 1; i < B; i++) {
  sum += sequence[i];
}

console.log(sum);
