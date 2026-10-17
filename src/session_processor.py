# session_processor.py
# Processes raw AI chat exports into clean, normalized JSON.

import json


class ChatSession:
    """Represents a single AI chat session."""

    def __init__(self, session_name, date, topics):
        self.session_name = session_name
        self.date = date
        self.topics = topics

    def to_dict(self):
        """Convert the object to a dictionary."""
        return {
            'session_name': self.session_name,
            'date': self.date,
            'topics': self.topics
        }

    def display(self):
        """Return a formatted string for display."""
        topics_str = ", ".join(self.topics)
        return f"{self.session_name} ({self.date}) - Topics: {topics_str}"


def process_chat_export(input_file, output_file):
    """Read raw chat export, validate entries, and write clean JSON."""

    # Read the raw JSON file
    print(f"Reading raw data from {input_file}...")
    with open(input_file, 'r') as file:
        raw_data = json.load(file)

    # List to hold valid ChatSession objects
    sessions = []

    # Process each entry
    for entry in raw_data:
        try:
            # Extract required fields
            session_name = entry['session_name']
            date = entry['date']
            topics = entry['topics']

            # Validate that topics is a list
            if not isinstance(topics, list):
                raise TypeError("topics must be a list")

            # Create a ChatSession object
            session = ChatSession(session_name, date, topics)
            sessions.append(session)
            print(f"  Processed: {session.display()}")

        except KeyError as e:
            print(f"  Skipping entry with missing field: {e}")
        except TypeError as e:
            print(f"  Skipping entry with invalid data: {e}")

    # Convert ChatSession objects to dictionaries
    clean_data = [session.to_dict() for session in sessions]

    # Write the clean JSON file
    print(f"\nWriting clean data to {output_file}...")
    with open(output_file, 'w') as file:
        json.dump(clean_data, file, indent=4)

    # Summary
    print(f"Processing complete: {len(sessions)} valid sessions saved.")
    print(f"Entries skipped: {len(raw_data) - len(sessions)}")


if __name__ == "__main__":
    process_chat_export('../data/raw_chat_export.json', '../data/sessions.json')
