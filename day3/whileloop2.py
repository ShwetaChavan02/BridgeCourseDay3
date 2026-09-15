correct_pass = "some_pass"
not_found = True
while not_found:
    passw = input("Enter the password: ")
    if passw == correct_pass:
        not_found = False
        print("Password Matched!")
    