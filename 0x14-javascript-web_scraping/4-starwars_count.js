#!/usr/bin/node
// This script shows the number of movies featuring Wedge Antilles
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
    for (let i = 0; i < data.count; i++) {
      if (data.results[i].characters.includes(wedge)) count++;
    }
    console.log(count);
  }
});
