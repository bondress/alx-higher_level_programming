#!/usr/bin/node
const request = require('request');
const path = 'https://swapi.dev/api/films/' + process.argv[2];
request(path, function (err, response, body) {
  if (!err) {
    let chars = JSON.parse(body).characters;
    printCharacters(chars, 0);
  }
});

function printCharacters (chars, index) {
  request(chars[index], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printCharacters(chars, index + 1);
      }
    }
  });
}
