#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');
const url = args[0];
let count = 0;
let i;
let j;

req(url, function (err, resp, numMov) {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(numMov).results;
    for (i of movies) {
      for (j of i.characters) {
        if (j.search('/18/') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
