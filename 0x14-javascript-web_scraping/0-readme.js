#!/usr/bin/node
// Script that reads and prints the content of a file.
const args = process.argv.slice(2);
const fs = require('fs');

fs.readFile(args[0], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
