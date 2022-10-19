#!/usr/bin/node
const fs = require('fs');
const request = require('request');

if (process.argv.length > 3) {
  request(`${process.argv[2]}`, (err, res, body) => {
    if (err) {
      console.log(err);
    } else if (body) {
      const contents = body.toString('utf-8');
      fs.writeFile(process.argv[3], contents, err => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
