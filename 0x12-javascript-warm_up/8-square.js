#!/usr/bin/node
const iter = Math.floor(process.argv[2]);
if (isNaN(iter)) console.log('Missing size');
else if (iter > 0) {
  let str = '';
  for (let y = 0; y < iter; y++) {
    for (let x = 0; x < iter; x++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
}
