#!/usr/bin/node
const newArg = process.argv.slice(2);
for (idx in newArg) {
  newArg[idx] = parseInt(newArg[idx]);
}
if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  newArg.sort(function (a, b) {
    return a - b;
  });
  console.log(newArg[newArg.length - 2]);
}
