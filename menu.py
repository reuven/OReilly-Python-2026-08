def menu(options):
    while True:
        user_choice = input(f'Choose from {options}: ').strip()
    
        if user_choice in options:
            return user_choice
    
        print(f'Invalid choice {user_choice}; choose from {options}')

if __name__ == '__main__':
    # below here will only run when the program is invoked standalone
    # this stuff will be ignored when we import menu
    c = menu(['a', 'b', 'c', 'd'])
    print(f'User chose {c}')