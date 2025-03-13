# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def isPalindrome(text):
        if len(text) < 2:
            return True
        h, t = 0, len(text) - 1
        while h < t:
            if not text[h].isalnum():
                h+=1
            elif not text[t].isalnum():
                t-=1
            else:
                 if text[h].lower() != text[t].lower():
                      return False
                 h+=1
                 t-=1
        return True


text = "A man, a plan, a canal: Panama"
output = isPalindrome(text)
print(output)