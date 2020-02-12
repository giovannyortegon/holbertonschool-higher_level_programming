#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request
  .get(args[0])
  .on('response', function (response) {
    console.log(`code: ${response.statusCode}`);
  });
