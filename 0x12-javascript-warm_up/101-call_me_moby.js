#!/usr/bin/node
// Write a function that executes x times a function.
let i = 0;
exports.callMeMoby = function (a, b) {
  for (; i < a; i++) {
    b();
  }
};
