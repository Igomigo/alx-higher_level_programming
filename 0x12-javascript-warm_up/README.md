# JavaScript Basics

This repository contains a collection of JavaScript code snippets and examples that cover the fundamentals of JavaScript programming.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Variables](#variables)
- [Data Types](#data-types)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Functions](#functions)
- [Objects](#objects)
- [Arrays](#arrays)
- [Classes](#classes)
- [Modules](#modules)
- [Error Handling](#error-handling)

## Introduction

JavaScript is a versatile programming language primarily used for building interactive websites. It is a high-level, interpreted language that runs on the client-side (in the browser) as well as on the server-side (with the help of platforms like Node.js). JavaScript enables dynamic content, interactivity, and enhances the user experience on the web.

This repository aims to provide a foundational understanding of JavaScript by covering key concepts and demonstrating practical examples.

## Getting Started

To run the JavaScript code examples in this repository, follow these steps:

1. Ensure you have a JavaScript runtime installed. You can use Node.js, which can be downloaded from the official Node.js website (https://nodejs.org).

2. Clone this repository to your local machine using the following command:
git clone https://github.com/your-username/javascript-basics.git

3. Navigate to the cloned repository:
cd javascript-basics

4. Open the code files in your preferred code editor.

5. Run the JavaScript files using the appropriate command for your JavaScript runtime. For example, with Node.js, you can execute a JavaScript file like this:
node filename.js

## Variables

JavaScript variables are used to store data values. They can hold various types of data, including numbers, strings, booleans, objects, and more. In JavaScript, variables are declared using the `let`, `const`, or `var` keywords. The `let` and `const` keywords were introduced in newer versions of JavaScript (ES6) and are recommended for variable declarations.

Example:

```javascript
let message = "Hello, JavaScript!";
const pi = 3.14159;
var count = 10;

console.log(message);
console.log(pi);
console.log(count);

## Data Types
JavaScript has several built-in data types, including:

Number: represents numeric values.
String: represents a sequence of characters.
Boolean: represents either true or false.
Object: represents a collection of key-value pairs.
Array: represents an ordered list of elements.
Null: represents the intentional absence of any object value.
Undefined: represents an uninitialized variable.
Example:

let age = 25;
let name = "Alice";
let isStudent = true;
let person = { name: "Bob", age: 30 };
let numbers = [1, 2, 3, 4, 5];
let nullValue = null;
let undefinedValue;

console.log(age);
console.log(name);
console.log(isStudent);
console.log(person);
console.log(numbers);
console.log(nullValue);
console.log(undefinedValue);

## Operators
JavaScript provides various operators for performing operations on data. Some common operators include:

Arithmetic Operators: used for basic mathematical operations.
Assignment Operators: used to assign values to variables.
Comparison Operators: used to compare values.
Logical Operators: used to combine or negate conditions.
