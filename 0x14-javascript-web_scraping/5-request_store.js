#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', (error, data) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
