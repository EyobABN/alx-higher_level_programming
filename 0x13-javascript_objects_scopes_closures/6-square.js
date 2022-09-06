#!/usr/bin/node
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      let line = '';
      for (let j = 0; j < this.size; j++) {
        line += c;
      }
      console.log(line);
    }
  }
};
