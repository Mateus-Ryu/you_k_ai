# Write filtered TODOs to file.
with open("../to_do_list.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)
