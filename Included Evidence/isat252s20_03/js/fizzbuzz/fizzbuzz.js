
const fizz = function (x) {
  // check to see if x is defined/exists
  if (typeof x !== 'undefined') {
    // yes, it exists, carry on
    return typeof x === 'number' && x % 3 === 0 ? 'Fizz' : x
  } else {
    // no, it does not exist, throw an error
    throw new Error('there is no input')
  }
}

const buzz = function (x) {
  // check to see if x is defined/exists
  if (typeof x !== 'undefined') {
    // yes, it exists, carry on
    return typeof x === 'number' && x % 5 === 0 ? 'Buzz' : x
  } else {
    // no, it does not exist, throw an error
    throw new Error('there is no input')
  }
}

const fibu = function (x) {
  // check to see if x is defined/exists
  if (typeof x !== 'undefined') {
    // yes, it exists, carry on
    return typeof x === 'number' && x % 15 === 0 ? 'FizzBuzz' : x
  } else {
    // no, it does not exist, throw an error
    throw new Error('there is no input')
  }
}

const play = function (start, end) {
  // declare an empty array variable to hold our output
  const output = []
  // loop through the numbers from start to end
  for (let x = start; x <= end; x++) {
    output.push(buzz(fizz(fibu(x))))
  }
  return output
}

module.exports = {
  fizz,
  buzz,
  fibu,
  play
}