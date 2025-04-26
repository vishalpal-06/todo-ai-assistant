from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chains.chains import (
    task_classification_chain,
    delete_todo_chain,
    create_todo_chain,
    update_todo_chain
)
from api_calls import call_api_post, call_api_put, call_api_delete




origins = [
    "http://localhost:3000",
    "http://localhost:8501"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


def process_user_input( token: str, user_input: str) -> str:
    task_result = task_classification_chain.invoke({"user_input": user_input})
    task_type = task_result.task

    if task_type == "delete_todo":
        result = delete_todo_chain.invoke({"user_input": user_input})
        payload = result.dict()
        response = call_api_delete(access_token=token, payload=payload)
        return response

    elif task_type == "create_todo":
        result = create_todo_chain.invoke({"user_input": user_input})
        payload = result.dict()
        response = call_api_post(access_token=token, payload=payload)
        return response

    elif task_type == "update_todo":
        result = update_todo_chain.invoke({"user_input": user_input})
        payload = result.dict()
        clear_payload = {k: v for k, v in payload.items() if v is not None}
        response = call_api_put(access_token=token, payload=payload)
        return response
    else:
        return "Unrecognized task type."


class TextInput(BaseModel):
    text: str
    token: str


@app.post("/process_text")
async def process_text(input_data: TextInput):
    input_text = input_data.text
    token = input_data.token
    result = process_user_input(token=token,user_input=input_text)
    return result




