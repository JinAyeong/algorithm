const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [n, k, t] = input[0].split(" ").map(Number);
const sharks = input[1].split(" ").map(Number);

sharks.sort((a, b) => a - b);
sharks.push(Infinity);

const stack = [];

for (let i = 0; i < n; i++) {
  if (k === 0) break;

  if (sharks[i] >= t) {
    while (stack.length > 0 && sharks[i] >= t && k !== 0) {
      t += stack.pop();
      k -= 1;
    }

    if (k !== 0 && sharks[i] < t) {
      t += sharks[i];
      k -= 1;
    } else {
      break;
    }
  } else if (sharks[i + 1] < t) {
    stack.push(sharks[i]);
  } else {
    t += sharks[i];
    k -= 1;
  }
}

while (k > 0 && stack.length > 0) {
  t += stack.pop();
  k -= 1;
}

console.log(t);
