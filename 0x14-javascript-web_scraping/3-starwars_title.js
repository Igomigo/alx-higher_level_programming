#!/usr/bin/node
/**
 * Script that prints the title of a Star Wars movie where the episode
 * number matches a given integer.
 *
 * The first argument is the movie ID.
 */

const request = require('request');
const movieId = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${movieId[2]}`;

if (movieId.length < 3) {
  console.log('Usage: node <file_name.js> <int:id>');
} else {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    if (response.statusCode === 200) {
      body = JSON.parse(body);
      console.log(body.title);
    } else {
      console.log('Request failed');
    }
  });
}
