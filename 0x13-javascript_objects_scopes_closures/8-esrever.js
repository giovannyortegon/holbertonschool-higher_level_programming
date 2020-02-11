#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let i = list.length - 1;

  for (; i >= 0; i--) {
    revList.push(list[i]);
  }
  return revList;
};
