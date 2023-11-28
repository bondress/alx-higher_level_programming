#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
request(path, function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let done = {};
    todos.forEach((todo) => {
      if (todo.done && done[todo.userId] === undefined) {
        done[todo.userId] = 1;
      } else if (todo.done) {
        done[todo.userId] += 1;
      }
    });
    console.log(done);
  }
});
