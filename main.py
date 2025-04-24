from fastapi import FastAPI
from pydantic import BaseModel

from chains.chains import (
    task_classification_chain,
    delete_todo_chain,
    create_todo_chain,
    update_todo_chain
)
from api_calls import call_api_post, call_api_put, call_api_delete

app = FastAPI()


def process_user_input( token: str, user_input: str) -> str:
    task_result = task_classification_chain.invoke({"user_input": user_input})
    task_type = task_result.task

    if task_type == "delete_todo":
        result = delete_todo_chain.invoke({"user_input": user_input})
        payload = result.dict()
        call_api_delete(access_token=token, payload=payload)
        return f"Deleted: {result}"

    elif task_type == "create_todo":
        result = create_todo_chain.invoke({"user_input": user_input})
        payload = result.dict()
        call_api_post(access_token=token, payload=payload)
        return f"Created: {result}"

    elif task_type == "update_todo":
        result = update_todo_chain.invoke({"user_input": user_input})
        payload = result.dict()
        clear_payload = {k: v for k, v in payload.items() if v is not None}
        call_api_put(access_token=token, payload=payload)
        return f"Updated: {clear_payload}"
    else:
        return "Unrecognized task type."


class TextInput(BaseModel):
    text: str
    token: str


@app.post("/process_text")
async def process_text(input_data: TextInput):
    input_text = input_data.text
    token = input_data.token
    result = process_user_input(token,input_text)
    return {"result": result}




