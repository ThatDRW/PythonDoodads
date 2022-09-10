def recRange_10(n:int):
    print('recRange_10 Value:', n)

    # Base Case aka. Halting Condition.
    if n == 10: return

    # Return ourself after doing the smallest amount of work.
    return recRange_10(n+1)

def reverseString(s:str):
    # Base Case: End of the string.
    if s == '': return ''

    # Smallest amount of work: 
    # Take the first letter and put it at the end.
    return reverseString(s[1:]) + s[0]

def isPalindrome(s:str):
    # Base Case: Return True if the string passed 
    # is empty or 1 character long.
    if len(s) <= 1: return True

    # If the first and last char match, return self with 
    # the input string s without those first and last chars.
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])

    # 2nd Base Case: The first and last char did not match,
    # thus we can conclude the string is not a palindrome.
    return False

def justify(text, width):
    """Justify text to max width."""
    # Use rfind to find the last word end index respecting max width.
    length = text.rfind(' ', 0, width+1)

    # Base Case: If no spaces found or this will become the last string.
    if length == -1 or len(text) <= width: return text

    # Pull the first line off the text.
    line = text[:length]

    # Count the total number of spaces in this line.
    spaces = line.count(' ')

    # If there is at least one space, we will justify this line.
    if spaces != 0:
        # All spaces will be replaced by expand-number of spaces.
        expand = (width - length) // spaces + 1

        # Using modulo, find the remainder of spaces that cant
        # be divided equally amongst the others.
        extra = (width - length) % spaces
        
        # Replace all spaces with their expanded version.
        line = line.replace(' ', ' '*expand)

        # Now replace the first extra-number of spaces, with an addidional one.
        line = line.replace(' '*expand, ' '*(expand+1), extra)

    # Return our justified line + a newline. Send the remaining text through.
    return line + '\n' + justify(text[length+1:], width)

if __name__ == '__main__':
    ### Print out a range up to 10, starting from the passed argument.
    # recRange_10(0)

    ### Reverse a given string.
    # regular_str = 'Hello, world!'
    # reverse_str = reverseString(regular_str)
    # print(regular_str, '->', reverse_str)

    ### Check if the given string is a palidrome.
    # possible_palindromes = ['banana','anana','Hello, world!  !dlrow ,olleH']
    # for ppal in possible_palindromes:
    #     if isPalindrome(ppal):
    #         print(ppal, 'is indeed a palindrome!')
    #     else:
    #         print(ppal, 'is not a palindrome.')

    pass