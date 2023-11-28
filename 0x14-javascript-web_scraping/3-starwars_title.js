#!/usr/bin/node
const request = require('request');
let path = 'http://swapi.co/api/films/' + process.argv[2];
request(path, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
