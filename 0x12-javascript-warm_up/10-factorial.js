#!/usr/bin/node
/*
script that computes and prints a factorial
*/

const number = parseInt(process.argv[2]);

function factorial (number) {
  let i = 1;
  let factoriel = 1;

  while (i <= number) {
    factoriel = factoriel * i;
    i++;
  }
  return factoriel;
}

console.log(factorial(number));
