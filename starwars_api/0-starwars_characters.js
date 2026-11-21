#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function getJSON (u) {
  return new Promise((resolve, reject) => {
    request(u, (err, res, body) => {
      if (err) return reject(err);
      resolve(JSON.parse(body));
    });
  });
}

getJSON(url)
  .then((film) => Promise.all(film.characters.map(getJSON)))
  .then((people) => people.forEach((p) => console.log(p.name)))
  .catch((err) => console.error(err));