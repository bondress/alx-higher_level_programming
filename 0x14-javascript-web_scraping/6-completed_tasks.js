#!/usr/bin/node

const request = require('request');
const path = process.argv[2];

request.get(path, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksDone = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksDone[todo.userId]) {
        tasksDone[todo.userId] = 1;
      } else {
        tasksDone[todo.userId] += 1;
      }
    }
  });
  console.log(tasksDone);
});
