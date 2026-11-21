from fastapi import FastAPI  # type: ignore[import-not-found]
from pydantic import BaseModel  # type: ignore[import-not-found]

app = FastAPI()


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

class Note(BaseModel):
   term: str
   definition: str
   js_equivalent: str | None = None
   tags: list[str] = []
   learned: bool = False

class NoteUpdate(BaseModel):
   term: str | None = None
   definition: str | None = None
   js_equivalent: str | None = None
   tags: list[str] | None = None
   learned: bool | None = None

@app.get("/")
def root():
  return {"message": "Learning Notebook API is running!"}

@app.get("/terms")
def get_terms(tag: str | None = None, q: str | None = None):
  result = []
  for note in notes:
    if tag and tag not in note["tags"]:
        continue
    if q and q.lower() not in note["term"].lower():
        continue
    result.append(note)
  return result
 


@app.get("/terms/{term_id}")
def get_term(term_id: int):
  for note in notes:
    if note["id"] == term_id:
      return note
  return{"error": "Term not found"}



@app.post("/terms", status_code=201)
def add_term(note: Note):
   new_note = {"id" : len(notes) + 1}
   new_note.update(note.model_dump())
   notes.append(new_note)
   return new_note


@app.patch("/terms/{term_id}")
def update_term(term_id: int, changes: NoteUpdate):
   for note in notes:
      if note["id"] == term_id:
         note.update(changes.model_dump(exclude_unset = True))
         return note
   return {"message": "Term not found"}