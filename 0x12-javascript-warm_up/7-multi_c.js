#!/usr/bin/node
const iter = Math.floor(process.argv[2]);
if (isNaN(iter)) console.log('Missing number of occurences');
else if (iter > 0) {
  for (let i = 0; i < iter; i++) {
    console.log('C is fun');
  }
}
