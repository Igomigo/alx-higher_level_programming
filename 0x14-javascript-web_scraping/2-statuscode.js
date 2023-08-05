#!/usr/bin/node
/**
 * Script that display the status code of a GET request.
 * Args: first args is the URL to request.
 * Return: Status code of the request using the requst module.
 */

const request = require('request');
const args = process.argv;
const url = args[2];

if (args.length < 3) {
  console.log('Usage: node <file_name.js> <url>');
} else {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}
