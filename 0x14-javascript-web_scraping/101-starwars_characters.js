#!/usr/bin/node
// Use the character list to get the URL for each person the send a GET request
// to fetch their name(s) :)
const request = require('request');
const url = (
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + ' /'
);
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const result = JSON.parse(body);
    for (const characters of result.characters) {
      request(characters, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const charResult = JSON.parse(body);
          console.log(charResult.name);
        }
      });
    }
  }
});
