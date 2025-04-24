from langchain.prompts import PromptTemplate

# Define a prompt with examples
identify_task_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are an assistant that classifies user requests into one of the following tasks: 
- create_todo
- update_todo
- delete_todo
- other

Use the following guidelines:
- Choose 'create_todo' only if the user explicitly mentions creating or adding a todo (e.g., "create a todo", "add a task").
- Choose 'update_todo' only if the user explicitly mentions updating or changing an existing todo.
- Choose 'delete_todo' only if the user explicitly mentions deleting or removing a todo.
- Choose 'other' for any input that does not clearly fit the above categories.

Examples:
- "Add a todo to buy milk" → create_todo
- "Create a task for my meeting at 3 PM" → create_todo
- "Update my todo to buy eggs instead of milk" → update_todo
- "Delete my todo about buying milk" → delete_todo
- "I am going to a party tonight" → other
- "The weather is nice today" → other

Based on the user's input, determine the intended task and return the result in the following JSON format:
{{
    "task": "<task_name>"
}}

User input: {user_input}

Task:
"""
)

