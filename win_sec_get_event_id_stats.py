import json

def read_eventid_info(filename):
    """
    Reads the eventid_info from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def display_eventid_info(eventid_info, event_id):
    """
    Displays the paths and levels for a given EventID, including each path segmented by level.
    """
    info = eventid_info.get(event_id)
    if info:
        print("\nLevels and Paths:")
        for level, paths in info['path'].items():
            print(f"\nLevel {level}:")
            for path in paths:
                print(f"  - {path}")
        print("\nCounts by Level:")
        for level, count in info['level'].items():
            print(f"{level}: {count}")
    else:
        print(f"No information found for EventID {event_id}.")

def main():
    filename = 'eventid_info.json'  # Make sure this path is correct
    eventid_info = read_eventid_info(filename)

    # Get EventID input from the user
    event_id = input("Enter EventID: ").strip()
    display_eventid_info(eventid_info, event_id)

if __name__ == "__main__":
    main()
