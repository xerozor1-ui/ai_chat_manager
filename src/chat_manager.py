# chat_manager.py
# This file contains the data structures for the AI Chat Manager.

# A list to hold all chat session dictionaries
sessions = []

# Our first session - a dictionary with three fields
session_1 = {
    'session_name': 'Python Decorators Deep Dive',
    'date': '2025-01-20',
    'topics': ['python', 'decorators', 'functions']
}

# Add the session to our list
sessions.append(session_1)
print("Session added successfully!")

# Print all current chat sessions
print("--- Current Chat Sessions ---")
for session in sessions:
    print(session)
print("-----------------------------")

# Create a second session
session_2 = {
    'session_name': 'Docker Setup for Flask',
    'date': '2025-01-21',
    'topics': ['docker', 'flask', 'devops']
}

# Add the second session to our list
sessions.append(session_2)
print("\nSecond session added successfully!")

# Print all chat sessions again to show the change
print("\n--- All Chat Sessions (Updated) ---")
for session in sessions:
    print(session)
print("-----------------------------------")
