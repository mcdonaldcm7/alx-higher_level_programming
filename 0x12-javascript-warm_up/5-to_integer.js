#!/usr/bin/node
let num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  num = Math.floor(num);
  console.log('My number: ' + num);
}
