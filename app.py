import streamlit as st
from dotenv import load_dotenv
from api_calls import call_api_post,call_api_put,call_api_delete
# Load environment variables
load_dotenv()

# Import chains
from chains.chains import (
    task_classification_chain,
    delete_todo_chain,
    create_todo_chain,
    update_todo_chain
)

# Streamlit App
st.set_page_config(page_title="Todo Assistant", page_icon="📝")

st.title("📝 Todo Task Assistant")

# User input
user_input = st.text_input("Enter a todo command:")

# Action
if st.button("Run"):
    if user_input.strip() == "":
        st.warning("Please enter a command.")
    else:
        with st.spinner("Classifying task..."):
            task_result = task_classification_chain.invoke({"user_input": user_input})
        
        st.success(f"Identified Task: `{task_result.task}`")

        # Handle task type
        if task_result.task == "delete_todo":
            with st.spinner("Running delete chain..."):
                result = delete_todo_chain.invoke({"user_input": user_input})
                payload = result.dict()
                call_api_delete(payload=payload)
            st.write("🔴 Delete Result:", result)

        elif task_result.task == "create_todo":
            with st.spinner("Running create chain..."):
                result = create_todo_chain.invoke({"user_input": user_input})
                payload = result.dict()
                call_api_post(payload=payload)
            st.write("🟢 Create Result:", result)
    
        elif task_result.task == "update_todo":
            with st.spinner("Running update chain..."):
                result = update_todo_chain.invoke({"user_input": user_input})
                payload = result.dict()
                clear_payload = {}
                for key,value in payload.items():
                    if value != None:
                        clear_payload[key]=value
                call_api_put(payload=payload)
            st.write("🟡 Update Result:", clear_payload)

        else:
            st.error("Unrecognized task type.")
