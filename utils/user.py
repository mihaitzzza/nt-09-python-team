def get_user_choice(user_choices):
    while True:
        user_input = input("input: ")
        if user_input in user_choices:
            continue

        if len(user_input) != 1 or not user_input.isalpha():
            continue
        
        return user_input


