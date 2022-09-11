#!/usr/bin/node
const dict = require('./101-data').dict;

const myDict = Object.entries(dict).reduce((acc, [key, value]) => {
  acc[value] = acc[value] ? [...acc[value], key] : [key];
  return acc;
}, {});

console.log(dict);
console.log(myDict);
