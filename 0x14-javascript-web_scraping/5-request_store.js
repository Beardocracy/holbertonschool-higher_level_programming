#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
