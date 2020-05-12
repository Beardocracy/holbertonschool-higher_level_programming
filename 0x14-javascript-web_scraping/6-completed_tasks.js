#!/usr/bin/node
// This script counts the number of tasks completed by user id
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const tasks = {};
    for (let i = 0; i < data.length; i++) {
      const userId = data[i].userId;
      if (data[i].completed) {
        if (!tasks[userId]) tasks[userId] = 1;
        else tasks[userId] += 1;
      }
    }
    console.log(tasks);
  }
});
