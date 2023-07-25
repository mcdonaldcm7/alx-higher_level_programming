#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const info = JSON.parse(body);
    const films = info.results;
    let count = 0;
    for (const f of films) {
      for (const c of f.characters) {
        if (c === character) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
