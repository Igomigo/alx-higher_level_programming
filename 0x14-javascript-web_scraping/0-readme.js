#!/usr/bin/node
/**
 * Script that reads and prints the content of a file.
 * File content is read in utf-8.
 * Return: File content or error object if an error occurred.
 */

const fs = require('fs');
const args = process.argv;

if (args.length < 3) {
  console.log('Usage: node <file_name> <file>');
} else {
  fs.readFile(`${args[2]}`, 'utf-8', (error, data) => {
    if (error) {
      console.error(error);
    } else {
      console.log(data.trim());
    }
  });
}
