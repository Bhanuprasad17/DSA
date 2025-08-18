function isPalindrome(str) {
    // Convert to lowercase to ignore case sensitivity (optional)
    str = str.toLowerCase();

    let left = 0;                // Start pointer
    let right = str.length - 1;  // End pointer

    while (left < right) {
        if (str[left] !== str[right]) {
            return false; // If mismatch found, not a palindrome
        }
        left++;   // Move left pointer forward
        right--;  // Move right pointer backward
    }

    return true; // If no mismatch, it's a palindrome
}

// Test cases
console.log(isPalindrome("madam"));   // true
console.log(isPalindrome("racecar")); // true
console.log(isPalindrome("hello"));   // false
