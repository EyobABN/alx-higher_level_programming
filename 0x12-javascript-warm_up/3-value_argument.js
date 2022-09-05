#!/usr/bin/node
const process = require('process');
const av = process.argv;
if (!av[2]) {
  console.log('No argument');
} else {
  console.log(av[2]);
}
