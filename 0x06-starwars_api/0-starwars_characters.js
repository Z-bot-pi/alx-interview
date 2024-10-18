#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];  // Get the movie ID from the command line argument

// Check if a movie ID is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL for fetching movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const movie = JSON.parse(body);  // Parse the JSON response

  // Check if the movie ID exists in the API
  if (!movie.characters) {
    console.error('Movie not found');
    return;
  }

  // Fetch and print character names in order
  movie.characters.forEach(characterUrl => {
    request(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }

      const character = JSON.parse(charBody);  // Parse the JSON response for the character
      console.log(character.name);  // Print the character's name
    });
  });
});
