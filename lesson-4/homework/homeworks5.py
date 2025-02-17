while True:
    p = input("Enter a password: ")
    if len(p) < 8:
        print("Password is too short.")
    elif p.lower() == p:
        print("Password must contain an upper case letter.")
    else:
        print("Password is strong.")
        break