#!/usr/bin/node
function factorial (num) {
  const x = Number(num);
  if (isNaN(x) || x === 1 || x === 0) return (1);
  return (x * factorial(x - 1));
}

console.log(factorial(process.argv[2]));
