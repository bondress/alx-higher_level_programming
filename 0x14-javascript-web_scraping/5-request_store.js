#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const path = process.argv[2];
request(path).pipe(fs.createWriteStream(process.argv[3]));
