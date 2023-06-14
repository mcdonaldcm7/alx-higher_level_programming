#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
  }

  let fileContents = data1;

  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
    }
    fileContents += data2;

    fs.writeFile(process.argv[4], fileContents, 'utf8', (err, data) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
