#!/usr/bin/node
const str = parseInt(process.argv[2]);
let print = '';
if (isNaN(str)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < str; i++) {
    for (let y = 0; y < str; y++) {
      print += 'X';
    }
    console.log(print);
    print = '';
  }
}
