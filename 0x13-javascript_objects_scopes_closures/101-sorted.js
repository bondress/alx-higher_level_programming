#!/usr/bin/node
const dict = require('./101-data.js').dict;
const nDict = {};
for (const key in dict) {
  if (nDict[dict[key]] === undefined) {
    nDict[dict[key]] = [key];
  } else {
    nDict[dict[key]].push(key);
  }
}
console.log(nDict);
