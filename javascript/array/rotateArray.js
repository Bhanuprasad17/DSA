function rotateArr(arr, k) {
  let n = arr.length;

  k = k % n
  console.log(k)

  for (let j = 0; j < k; j++) {
   let lastNum = arr[n - 1];

    for (let i = n - 1; i >= 0; i--) {
      arr[i] = arr[i - 1];
    }

    arr[0] = lastNum;
  }
  return arr;
}

console.log(rotateArr([1, 2, 3, 4, 5],4));
