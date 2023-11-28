#!/usr/bin/node

const request = require('request');

const movId = process.argv[2];
const path = `https://swapi.dev/api/films/${movId}/`;

request.get(path, (err, response, body) => {
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
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
