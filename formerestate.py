def display_menu():
    """Display the main menu for Former Estate."""
    print("\n" + "="*50)
    print("FORMER ESTATE".center(50))
    print("="*50)
    print("\n1. New Game")
    print("2. Load Game")
    print("3. About")
    print("4. Quit")
    print("\n" + "="*50)


def get_menu_choice():
    """Get and validate the player's menu choice."""
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 4.")


def handle_menu_choice(choice):
    """Handle the player's menu selection."""
    if choice == '1':
        start_new_game()
    elif choice == '2':
        load_game()
    elif choice == '3':
        about()
    elif choice == '4':
        quit_game()


def start_new_game():
    """Start a new game."""
    print("\nStarting new game...")
    # Send user to game.py
    import game
    game.start_game()



def load_game():
    """Load a saved game."""
    print("\nLoading game...")
    # logic to select and load a saved game
    print("Game loaded successfully!")

def about():
    """Display information about the game."""
    print("\nAbout Former Estate")
    print("A text-based adventure game")
    print("Developed by Liligirthlord 2025")
    print("Type 'help' during the game for assistance.")
    print("Enjoy your adventure!")


def quit_game():
    """Quit the game."""
    print("\nSee you another time")
    exit()


def main():
    """Main game loop."""
    while True:
        display_menu()
        choice = get_menu_choice()
        handle_menu_choice(choice)


if __name__ == "__main__":
    main()
