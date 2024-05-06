import os
import json
import yaml
from collections import defaultdict

def update_eventid_counts_from_dict(d, eventid_info, level, file_path):
    """
    Recursively search through the dictionary for 'EventID' keys and update counts, paths, and level segmentation.
    """
    if isinstance(d, dict):
        current_level = d.get('level', level)  # Update level if present
        for key, value in d.items():
            if key == "EventID":
                if not isinstance(value, list):  # Make single values into a list
                    value = [value]
                for event_id in value:
                    if current_level not in eventid_info[event_id]['level']:
                        eventid_info[event_id]['level'][current_level] = 0
                    eventid_info[event_id]['level'][current_level] += 1
                    # Initialize the path segment if it doesn't exist
                    if current_level not in eventid_info[event_id]['path']:
                        eventid_info[event_id]['path'][current_level] = []
                    if file_path not in eventid_info[event_id]['path'][current_level]:
                        eventid_info[event_id]['path'][current_level].append(file_path)
            else:
                update_eventid_counts_from_dict(value, eventid_info, current_level, file_path)
    elif isinstance(d, list):
        for item in d:
            update_eventid_counts_from_dict(item, eventid_info, level, file_path)

def update_eventid_info(filepath, eventid_info):
    with open(filepath, 'r') as file:
        try:
            content = yaml.safe_load(file)
            # Use the full file path
            update_eventid_counts_from_dict(content, eventid_info, level=None, file_path=filepath)
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {filepath}: {exc}")

def count_eventids_in_directory(directory):
    # Adjusted structure to support path segmentation by level
    eventid_info = defaultdict(lambda: {'level': defaultdict(int), 'path': defaultdict(list)})
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                filepath = os.path.join(root, file)
                update_eventid_info(filepath, eventid_info)
    return eventid_info

# Specify the directory to search
directory_path = 'rules/sigma/'  # Adjust this path as necessary
eventid_info = count_eventids_in_directory(directory_path)

# Specify the output filename
output_filename = 'eventid_info.json'

# Write the info to the file in JSON format
with open(output_filename, 'w') as file:
    # Converting defaultdict to a regular dict for JSON serialization
    eventid_info_regular = {k: {kk: vv if kk != 'path' else dict(vv) for kk, vv in v.items()} for k, v in eventid_info.items()}
    json.dump(eventid_info_regular, file, indent=4, sort_keys=True)

print(f"EventID info with full paths and level-segmented paths has been saved to {output_filename}")
