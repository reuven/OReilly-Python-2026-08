def menu(options):
    while True:
        user_choice = input(f'Choose from {options}: ').strip()
    
        if user_choice in options:
            return user_choice
    
        print(f'Invalid choice {user_choice}; choose from {options}')
        