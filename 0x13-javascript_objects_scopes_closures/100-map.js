#!/usr/bin/node
const list = require('./100-data').list;

const mapList = list.map(function (x, idx) {
  return x * idx;
});

console.log(list);
console.log(mapList);
