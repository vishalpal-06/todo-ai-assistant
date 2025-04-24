from langchain.prompts import PromptTemplate

update_todo_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are an assistant that extracts details from a user request to update a todo. Extract the following fields:
- title (required): The title of the todo to update (1-100 characters).
- description (optional): The new description of the todo (1-500 characters).
- status (optional): The new status of the todo, either 'Completed' or 'Pending'.
- priority (optional): The new priority of the todo, either 'Low', 'Medium', or 'High'.

### Rules:
- Include ONLY the fields explicitly mentioned in the user input in the output JSON.
- If an optional field (description, status, priority) is not specified, do NOT include it in the output JSON.
- At least one of description, status, or priority must be provided.
- If the input is empty or invalid, return a default with title "Untitled task" and description "No details provided".
- For priority, use keyword detection:
  - "important", "urgent", "ASAP", "must" → "High"
  - "later", "whenever", "eventually" → "Low"
  - Otherwise, default to "Medium" if unclear.

### Examples:
- "Update my todo to buy milk with description get 1 liter instead, status Completed"
  {{"title": "buy milk", "description": "get 1 liter instead", "status": "Completed"}}
- "Update my task visit riya shop for buying laptop status to Completed"
  {{"title": "visit riya shop for buying laptop", "status": "Completed"}}
- "Update my todo for meeting at 3 PM with priority high"
  {{"title": "meeting at 3 PM", "priority": "High"}}
- "update priority to High for my task go office for daily office work"
  {{"title": "go office for daily office work", "priority": "High"}}

### Your Turn:

User input: {user_input}

Respond ONLY with valid JSON containing only the fields explicitly mentioned in the input (always include title, and at least one of description, status, or priority).
"""
)