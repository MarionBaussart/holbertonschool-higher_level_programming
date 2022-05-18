#!/usr/bin/node

/*
Script that computes the number of tasks completed by user id
*/

const axios = require('axios').default;

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((res) => {
    const usersDict = {};

    for (const task of res.data) {
      if (task.completed === true) {
        if (usersDict[task.userId] === undefined) {
          usersDict[task.userId] = 0;
        }
        usersDict[task.userId] += 1;
      }
    }
    console.log(usersDict);
  });
