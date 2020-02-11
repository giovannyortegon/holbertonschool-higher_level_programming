#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let nOccurs = 0;

  for (; i < list.length; i++) {
    if (list[i] === searchElement) {
      nOccurs += 1;
    }
  }
  return nOccurs;
};
