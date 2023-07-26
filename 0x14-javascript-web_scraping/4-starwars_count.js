#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/?search=wedge';
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const info = JSON.parse(body);
    const results = info.results;
    console.log(results[0].films.length);
  }
});
