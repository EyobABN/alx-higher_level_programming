#!/usr/bin/node
const fs = require('fs');
const process = require('process');

const fileA = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const fileB = fs.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });

const sum = fileA.concat(fileB);

fs.writeFile(process.argv[4], sum, 'utf8', function (err, result) { if (err) console.log('error', err); });
