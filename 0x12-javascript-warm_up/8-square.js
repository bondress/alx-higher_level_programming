#!/usr/bin/node
const a = process.argv[2];

if (!parseInt(a)) {
  console.log('Missing size');
} else {
  for (let n = 0; n < a; n++) {
    let b = 0;
    let mySquare = '';

    while (b < a) {
      mySquare = mySquare + 'X';
      b++;
    }
    console.log(mySquare);
  }
}
