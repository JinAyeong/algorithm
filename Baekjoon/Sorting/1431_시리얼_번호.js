const getSum = (str) => {
  return str
    .split("")
    .filter((char) => char >= "0" && char <= "9")
    .reduce((sum, char) => sum + Number(char), 0);
};

const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);

const serialNumber = [];

for (let i = 1; i < N + 1; i++) {
  serialNumber.push(input[i]);
}

serialNumber.sort((a, b) => {
  // 조건1
  if (a.length !== b.length) {
    return a.length - b.length;
  }

  // 조건2
  const sumA = getSum(a);
  const sumB = getSum(b);
  if (sumA !== sumB) {
    return sumA - sumB;
  }

  // 조건3
  return a.localeCompare(b);
});

console.log(serialNumber.join("\n"));
