#!/usr/bin/node
// Write a code to recieve arguments from the command line
console.log(process.argv);
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
