stack = ["A man a plan a canal Panama"] 
stack2 =["Hello"]

def is_palindrome(s):
    s = "".join([c for c in s if c.isalpha()]).lower()
    return s == s[::-1]


if __name__ == "__main__":
      for s in stack:
          print(is_palindrome(s))
      for s in stack2:
          print(is_palindrome(s))