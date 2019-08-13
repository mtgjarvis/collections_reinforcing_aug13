project = {
    "committee": ["Stella", "Salma", "Kai"],
    "title": "Very Important Project",
    "due_date": "December 14, 2019",
    "id": "3284",
    "steps": [
        {"description": "conduct interviews", "due_date": "August 1, 2018"},
        {"description": "code of conduct", "due_date": "January 1, 2018"},
        {"description": "compile results", "due_date": "November 10, 2018"},
        {"description": "version 1", "due_date": "January 15, 2019"},
        {"description": "revisions", "due_date": "March 30, 2019"},
        {"description": "version 2", "due_date": "July 12, 2019"},
        {"description": "final edit", "due_date": "October 1, 2019"},
        {"description": "final version", "due_date": "November 20, 2019"},
        {"description": "Wrap up", "due_date": "December 1, 2019"},
    ],
}

# Update this dict so that each step has the name of a committee member associated with it (i.e. by adding an additional person key in each step dict), and each committee member has an equal number of tasks. Avoid typing out the committee members' names elsewhere in your code.

i = 0
for step in project['steps']:
    step['person'] = project['committee'][i]
    i += 1
    if i == 3:
        i = 0

print(project['steps'])