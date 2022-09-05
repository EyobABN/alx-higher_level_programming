#!/usr/bin/node
const process = require('process');
const av = process.argv;
const num = parseInt(av[2]);
if (num) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
