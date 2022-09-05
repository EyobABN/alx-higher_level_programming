#!/usr/bin/node
const process = require('process');
const av = process.argv;
const size = parseInt(av[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
