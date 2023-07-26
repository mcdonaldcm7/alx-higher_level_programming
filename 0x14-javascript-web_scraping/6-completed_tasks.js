#!/usr/bin/node
const request = require('request')
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body);
    let tasks_stat = {}
    for (const todo of result) {
      tasks_stat[todo.userId] = 0;
    }
    for (const todo of result) {
      tasks_stat[todo.userId] += Number(todo.completed);
    }
    for (const i in tasks_stat) {
      if (tasks_stat[i] === 0) {
        delete tasks_stat[i];
      }
    }
    console.log(tasks_stat);
  }
});
