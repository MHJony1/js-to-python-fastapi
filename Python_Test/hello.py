print("Hello, Python! How are you today?")

term = "variable"

print(f"The term is: {term}")

learned = False
definition = None

print(learned, definition)

if learned:
    print("Already learned")
  
else:
    print("Still learning")

if term == "variable" and not learned:
    print("Time to learn python variable")

    tags = ["python", "basics"]
    tags.append("api")
    print(len(tags))


    note = {"term": "variable",
            "definition": "A name that stores a value."}
    print(note["term"])



    notes = [
        {
            "id": 1,
            "term": "variable",
            "definition": "A name that stores a value.",
            "js_equivalent": "let/const/var",
            "tags": ["python", "basics", "api"],
            "learned": True
        },
        {
            "id": 2,
            "term": "function",
            "definition": "A block of code that performs a specific task.",
            "js_equivalent": "function",
            "tags": ["python", "basics"],
            "learned": False
        },
        {
            "id": 3,
            "term": "list",
            "definition": "A collection of items in a particular order.",
            "js_equivalent": "array",
            "tags": ["python", "basics"],
            "learned": False
        },
        {
            "id": 4,
            "term": "dictionary",
            "definition": "A collection of key-value pairs.",
            "js_equivalent": "object",
            "tags": ["python", "basics"],
            "learned": False
        },
    ]

for note in notes: 
    print(note["term"])

query = "LI"
for note in notes:
    if query.lower() in note["term"].lower():
       print("Found:", note["term"])


def find_term(notes, name):
    for note in notes:
        if note["term"] == name:
            return note 


print(find_term(notes, "dict"))   
print(find_term(notes, "class"))
print(find_term(notes, 42))         