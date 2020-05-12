#!/usr/bin/node
// This script displays the status code of a GET request
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) console.log('code: ' + response.statusCode);
});
