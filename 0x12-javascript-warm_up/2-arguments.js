#!/usr/bin/node
const process = require('process');
const argc = process.argv.length - 2;
if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else if (argc > 1) {
  console.log('Arguments found');
}
