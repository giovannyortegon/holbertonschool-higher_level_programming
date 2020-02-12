#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');
const url = 'http://swapi.co/api/films/';

req(url + `${args[0]}`, function (err, resp, episode) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(episode).title);
  }
});
