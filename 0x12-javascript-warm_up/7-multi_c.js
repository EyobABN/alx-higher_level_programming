#!/usr/bin/node
const process = require('process');
const av = process.argv;
const num = parseInt(av[2]);
if (num) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
