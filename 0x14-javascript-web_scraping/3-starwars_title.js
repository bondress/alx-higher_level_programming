#!/usr/bin/node

const request = require('request');
const movId= process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
