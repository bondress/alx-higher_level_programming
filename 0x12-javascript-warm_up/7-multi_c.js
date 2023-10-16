#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));

if (!parseInt(x)) {
  console.log('Missing number of occurences');
} else {
  for (let n = 0; n < x; n++) {
    console.log('C is fun');
  }
}
