def password_entry(password):
    """A function that checks if a string is at least 6 characters, and contains a number and any one of !#?£

    Args:
        password (string)

    Returns:
        boolean: True if the password fits the requirements, False if else
    """
    if len(password) < 6:
        return False
    
    has_symbol = False
    has_number = False
    for character in password:
        if character in ['!','#','?','£']:
            has_symbol = True
        if character in ['1','2','3','4','5','6','7','8','9','0']:
            has_number = True
    if has_symbol == False or has_number == False:
        return False
    
    return True

if __name__ == "__main__":
    assert password_entry('wjadiowadwa41!')
    assert not password_entry('wjadiowadwa41')
    assert not password_entry("2!grt")
    assert not password_entry('123456')
    assert password_entry("PA££W0RD")