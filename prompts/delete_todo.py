from langchain.prompts import PromptTemplate

delete_todo_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are an assistant that extracts details from a user request to delete a todo. Extract the title of the todo to delete.

Examples:
- "Delete my todo about buying milk" → {{"title": "buying milk"}}
- "Remove my todo for meeting at 3 PM" → {{"title": "meeting at 3 PM"}}

Based on the user's input, extract the title and return the result in the following JSON format:
{{
    "title": "<title>"
}}

User input: {user_input}

Task:
"""
)