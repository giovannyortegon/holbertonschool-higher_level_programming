#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');
const fs = require('fs');
const url = args[0];

req(url, function (errs, resp, contents) {
  if (errs) {
    console.log(errs);
  } else {
    const content = contents;
    try {
      fs.writeFileSync(args[1], content, 'utf-8');
    } catch (err) {
      console.error(err);
    }
  }
});
