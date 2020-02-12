#!/usr/bin/node

const args = process.argv.slice(2);
const req = require('request');
const url = args[0];

req(url, function (errs, resp, contents) {
  if (errs) {
    console.log(errs);
  } else {
    const completedTasks = {};
    const tasks = JSON.parse(contents);
    for (const task of tasks) {
      if (task.completed === true) {
        if (task.userId in completedTasks) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
