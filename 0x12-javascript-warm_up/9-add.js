#!/usr/bin/node
const process = require('process');
const av = process.argv;
const num1 = parseInt(av[2]);
const num2 = parseInt(av[3]);
function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
