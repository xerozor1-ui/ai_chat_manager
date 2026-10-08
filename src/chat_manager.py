# chat_manager.py
# A command-line application for managing AI chat sessions.

# Global list to hold all sessions
sessions = []


def add_session():
    """Add a new chat session."""
    print("\n--- Add New Session ---")

    name = input("Enter session name: ")
    if len(name) == 0:
        print("Session name cannot be empty.")
        return

    date = input("Enter date (YYYY-MM-DD): ")
    if len(date) == 0:
        print("Date cannot be empty.")
        return

    topics_input = input("Enter topics (comma-separated): ")
    topics = [t.strip() for t in topics_input.split(",")]

    new_session = {
        'session_name': name,
        'date': date,
        'topics': topics
    }

    sessions.append(new_session)
    print(f"\nSession '{name}' added successfully!")


def list_sessions():
    """Display all stored sessions."""
    if len(sessions) == 0:
        print("\nNo sessions found.")
        return

    print("\n--- All Sessions ---")
    for session in sessions:
        name = session['session_name']
        date = session['date']
        topics = ", ".join(session['topics'])
        print(f"{name} ({date})")
        print(f"   Topics: {topics}")
    print("--------------------")


def search_sessions():
    """Search sessions by keyword."""
    if len(sessions) == 0:
        print("\nNo sessions to search.")
        return

    keyword = input("\nEnter keyword to search: ").lower()
    results = []

    for session in sessions:
        if keyword in session['session_name'].lower():
            results.append(session)
        elif keyword in session['topics']:
            results.append(session)

    if len(results) == 0:
        print(f"No sessions found with keyword '{keyword}'.")
    else:
        print(f"\n--- Sessions matching '{keyword}' ---")
        for session in results:
            print(f"- {session['session_name']} ({session['date']})")
        print("--------------------------------------")


def main():
    """Run the main program loop."""
    print("Welcome to AI Chat Manager!")

    running = True
    while running:
        print("\n=== AI Chat Manager ===")
        print("1. Add Session")
        print("2. List Sessions")
        print("3. Search Sessions")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            add_session()
        elif choice == "2":
            list_sessions()
        elif choice == "3":
            search_sessions()
        elif choice == "4":
            print("\nGoodbye!")
            running = False
        else:
            print("\nInvalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
