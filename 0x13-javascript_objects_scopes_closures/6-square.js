#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    let letter = '';

    if (c === undefined) {
      c = 'X';
    }

    let i, j;

    for (i = 0; i < this.width; i++) {
      letter += c;
    }
    for (j = 0; j < this.height; j++) {
      console.log(letter);
    }
  }
};
