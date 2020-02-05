#!/usr/bin/node
// Write a function that increments and calls a function.
exports.addMeMaybe = function (number, theFunction) {
  return theFunction(number + 1);
};
