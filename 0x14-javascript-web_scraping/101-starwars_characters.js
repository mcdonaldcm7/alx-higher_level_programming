#!/usr/bin/node
// Use the character list to get the URL for each person the send a GET request
// to fetch their name(s) :)
const request = require('request');
const url = (
  'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + ' /'
);

const fetchCharacterName = async (url) => {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        const charResult = JSON.parse(body);
        resolve(charResult.name);
      }
    });
  });
};

request(url, async function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const result = JSON.parse(body);
    const characterNames = [];

    for (const characterUrl of result.characters) {
      try {
        const name = await fetchCharacterName(characterUrl);
        characterNames.push(name);
      } catch (error) {
        console.error(error);
      }
    }
    for (const c of characterNames) {
      console.log(c);
    }
  }
});
