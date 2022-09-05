#!/usr/bin/node
const process = require('process');
const av = process.argv;
if (!av[2] || av.length === 3) {
  console.log(0);
} else {
  const sortedNums = av.map(x => parseInt(x)).sort((a, b) => a - b);
  console.log(sortedNums[av.length - 2]);
}
