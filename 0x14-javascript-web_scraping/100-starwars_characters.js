#!/usr/bin/node
// This script shows the number of movies featuring Wedge Antilles
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    console.log(characters.length);
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const name = JSON.parse(body);
          console.log(name.name);
        }
      });
    }
  }
});
