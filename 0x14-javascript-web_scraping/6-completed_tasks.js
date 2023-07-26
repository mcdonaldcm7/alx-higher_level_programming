#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body);
    const taskStat = {};
    for (const todo of result) {
      taskStat[todo.userId] = 0;
    }
    for (const todo of result) {
      taskStat[todo.userId] += Number(todo.completed);
    }
    for (const i in taskStat) {
      if (taskStat[i] === 0) {
        delete taskStat[i];
      }
    }
    console.log(taskStat);
  }
});
