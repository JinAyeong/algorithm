const str = require("fs").readFileSync("/dev/stdin").toString().trim();
const aCnt = [...str].filter((c) => c === "a").length;
const strDouble = str + str;

let result = Number(Infinity);

for (let i = 0; i < str.length; i++) {
  const window = strDouble.slice(i, i + aCnt);
  const change = [...window].filter((c) => c === "b").length;
  result = Math.min(result, change);
}

console.log(result);
