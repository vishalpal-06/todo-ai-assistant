from langchain.prompts import PromptTemplate

create_todo_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are an assistant that extracts details from a user request to create a todo. Extract the following fields:
- title (required): A short summary of the task.
- description (required): A detailed description of the task.
- status (optional): Either 'Completed' or 'Pending'.
- priority (optional): Either 'Low', 'Medium', or 'High'.

### Priority detection hints:
- If the user says "important", "urgent", "ASAP", "must", or anything strongly emphasizing importance, set priority to "High".
- If the user says "later", "whenever", "eventually", or uses a casual tone, set priority to "Low".
- Otherwise, default to "Medium" if unclear.
- If status is not mentioned or implied, set them to Pending.
- If priority is not mentioned or implied, set them to Low.

### Examples:
- "Add a todo to buy milk with description get 2 liters from store, status Completed, priority Medium"
  {{"title": "buy milk", "description": "get 2 liters from store", "status": "Completed", "priority": "Medium"}}
- "Create a task to study for exam with description prepare for math test by tomorrow"
  {{"title": "study for exam", "description": "prepare for math test by tomorrow", "status": "Pending", "priority": "Low"}}
- "I need to urgently call the bank to report fraud"
  {{"title": "call the bank", "description": "report fraud", "status": "Pending", "priority": "High"}}
- "Remind me someday to organize old photos"
  {{"title": "organize old photos", "description": "remind me someday", "status": "Pending", "priority": "Low"}}

### Your Turn:

User input: {user_input}

Respond ONLY with valid JSON. Do NOT include any explanation, notes, or additional text.
"""
)
