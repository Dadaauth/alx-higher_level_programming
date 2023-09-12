#!/usr/bin/node
str = process.argv[2];
if (isNaN(parseInt(str))) {
  console.log("Not a number");
} else {
  console.log(`My number: ${parseInt(str)}`);
}
