#!/usr/bin/node
const len = process.argv.length - 2;
if (len <= 0) console.log(0);
else {
  let max = process.argv[len];
  let secMax = 0;
  for (let i = 0; i < len; i++) {
    const num = Number(process.argv[2 + i]);
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num > secMax && num < max) secMax = num;
  }
  console.log(secMax);
}
