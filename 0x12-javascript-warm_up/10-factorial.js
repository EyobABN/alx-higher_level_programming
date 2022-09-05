#!/usr/bin/node
const process = require('process');
const av = process.argv;
const num = parseInt(av[2]);
function factorial (num) {
  if (!num) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(num));
