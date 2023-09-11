#!/usr/bin/node
// Write a code to recieve arguments from the command line
if (process.argv.length === 1) {
  console.log('No argument');
} else if (process.argv.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
