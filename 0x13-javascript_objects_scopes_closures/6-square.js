#!/usr/bin/node
const SquareBase = require('./5-square');
module.exports = class Square extends SquareBase {
  charPrint (c) {
    let printChar = 'X';
    if (c !== undefined) {
      printChar = c;
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(printChar);
      }
      console.log('');
    }
  }
};
