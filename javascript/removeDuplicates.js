function removeDuplicates(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] == arr[j]) {
        arr.splice(j, 1);
        j--;
      }
    }
  }
  return arr;
}

console.log(removeDuplicates([1, 2, 3, 2, 4, 1, 5]));

// O(n)

let array = [1, 2, 3, 2, 4, 1, 5];
let seen = {};
let i = 0;

while (i < array.length) {
  if (seen[array[i]]) {
    array.splice(i, 1); // remove duplicate
  } else {
    seen[array[i]] = true;
    i++;
  }
}

console.log(array); // Output: [1, 2, 3, 4, 5]
