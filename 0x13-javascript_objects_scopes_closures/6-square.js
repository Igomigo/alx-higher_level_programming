#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += 'X';
        }
        console.log(row);
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
