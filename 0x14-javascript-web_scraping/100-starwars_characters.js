#!/usr/bin/node

const request = require('request');

const movId = process.argv[2];
const url = `https://swapi.dev/api/films/${movId}/`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
