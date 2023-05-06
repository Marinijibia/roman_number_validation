import re

def is_valid_roman_numeral(s):
    # Regular expression pattern for valid Roman numerals
    pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    
    # Match the pattern against the input string
    match = re.match(pattern, s)
    
    # If there is a match and the matched string is equal to the input string, it is valid
    if match and match.group() == s:
        return "YES"
    else:
        return "NO"

def main():
    N = int(input())
    
    for _ in range(N):
        s = input()
        result = is_valid_roman_numeral(s)
        print(result)

    return 0

if __name__ == '__main__':
    main()
