#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);
if (isNaN(a) || isNaN(b)) console.log('NaN');
else console.log(a + b);
