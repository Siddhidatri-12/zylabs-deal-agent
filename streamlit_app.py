import streamlit as st
import requests
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Deal Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Deal Intelligence Agent")
st.caption(
    "RAG + Long-Term Memory + Deal Intelligence"
)

# =====================================
# CHAT HISTORY
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================
# USER INPUT
# =====================================

user_input = st.chat_input(
    "Ask a question..."
)

if user_input:

    # Show user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "message": user_input
            }
        )

        if response.status_code == 200:

            answer = response.json()["response"]

        else:

            answer = (
                f"Backend Error:\n\n"
                f"{response.text}"
            )

    except Exception as e:

        answer = f"Request Failed: {e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.header("🧠 Memory Dashboard")

    try:

        memory_response = requests.get(
            "http://127.0.0.1:8000/memories"
        )

        memories = memory_response.json()["memories"]

        if memories:

            df = pd.DataFrame(
                memories,
                columns=[
                    "ID",
                    "Type",
                    "Value",
                    "Importance",
                    "Reason",
                    "Created At",
                    "Updated At"
                ]
            )

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No memories stored."
            )

    except Exception as e:

        st.error(
            f"Could not load memories: {e}"
        )

    st.divider()

    # =====================================
    # MEMORY SEARCH
    # =====================================

    st.subheader("🔍 Search Memory")

    memory_type = st.selectbox(
        "Memory Type",
        [
            "account",
            "stakeholder",
            "pain_point",
            "buying_signal",
            "deal_context",
            "preference"
        ]
    )

    if st.button("Search"):

        try:

            response = requests.get(
                f"http://127.0.0.1:8000/memory/search/{memory_type}"
            )

            st.json(
                response.json()
            )

        except Exception as e:

            st.error(
                f"Search failed: {e}"
            )

    st.divider()

    # =====================================
    # DELETE MEMORY
    # =====================================

    st.subheader("🗑 Delete Memory")

    memory_to_delete = st.text_input(
        "Memory Value"
    )

    if st.button("Delete"):

        try:

            response = requests.delete(
                f"http://127.0.0.1:8000/memory/{memory_to_delete}"
            )

            if response.status_code == 200:

                st.success(
                    "Memory Deleted"
                )

                st.rerun()

            else:

                st.error(
                    response.text
                )

        except Exception as e:

            st.error(
                f"Delete failed: {e}"
            )