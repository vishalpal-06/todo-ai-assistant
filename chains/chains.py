from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import JsonOutputParser
import sys
sys.path.append(".")
from parsers.parser import (
    TaskIdentification, 
    DeleteTodoDetails, 
    CreateTodoDetails, 
    UpdateTodoDetails
)
from prompts.identify_task import identify_task_prompt
from prompts.delete_todo import delete_todo_prompt
from prompts.create_todo import create_todo_prompt
from prompts.update_todo import update_todo_prompt
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()


model = ChatAnthropic(model='claude-3-5-sonnet-20241022')


task_classification_chain = RunnableSequence(
    identify_task_prompt,
    model,
    JsonOutputParser(),
    lambda x: TaskIdentification(**x)
)


delete_todo_chain = RunnableSequence(
    delete_todo_prompt,
    model,
    JsonOutputParser(),
    lambda x: DeleteTodoDetails(**x)
)


create_todo_chain = RunnableSequence(
    create_todo_prompt,
    model,
    JsonOutputParser(),
    lambda x: CreateTodoDetails(**x)
)


update_todo_chain = RunnableSequence(
    update_todo_prompt,
    model,
    JsonOutputParser(),
    lambda x: UpdateTodoDetails(**x)
)