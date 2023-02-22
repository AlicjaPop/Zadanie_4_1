def is_palindrom(word):
    """
        Function checks if a given word is a palindrom,
        i. e. if read from left to right is the same
        as from right to left. 
        Returns True, if is a palindrom.
        Returns False, if is not.
    """
    if word==word[::-1]:
        return True
    else:
        return False