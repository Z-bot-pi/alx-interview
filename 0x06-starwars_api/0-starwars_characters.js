#!/usr/bin/node

const request = require('request');
const MyArgs = process.argv.slice(2);

const url = `https://swapi-api.hbtn.io/api/films/${MyArgs}`;

request(url, async (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const res = JSON.parse(body).characters;
  for (let i = 0; i < res.length; i++) {
    await new Promise((resolve, reject) => {
      request(res[i], (e, resp, bod) => {
        if (e) {
          reject(e);
        }
        console.log(JSON.parse(bod).name);
        resolve();
      });
    });
  }
});