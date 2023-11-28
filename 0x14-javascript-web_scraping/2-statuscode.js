#!/usr/bin/node
const request = require('request');
const path = process.argv[2];
request.get(path).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
