import streamlit as st
import requests
import pandas as pd

st.title("Deal Intelligence Agent")

# =====================
# CHAT SECTION
# =====================

user_input = st.text_input(
    "Ask a question"
)

if st.button("Submit"):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "message": user_input
            }
        )

        if response.status_code == 200:

            st.write(
                response.json()["response"]
            )

        else:

            st.error(
                f"Backend Error: {response.text}"
            )

    except Exception as e:

        st.error(
            f"Request failed: {e}"
        )

st.divider()

# =====================
# MEMORY SEARCH
# =====================

st.header("Search Memories")

memory_type = st.selectbox(
    "Select Memory Type",
    [
        "account",
        "stakeholder",
        "pain_point",
        "buying_signal",
        "deal_context",
        "preference"
    ]
)

if st.button("Search Memory"):

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

# =====================
# DELETE MEMORY
# =====================

st.header("Delete Memory")

memory_to_delete = st.text_input(
    "Enter memory value to delete"
)

if st.button("Delete Memory"):

    try:

        response = requests.delete(
            f"http://127.0.0.1:8000/memory/{memory_to_delete}"
        )

        st.success(
            response.json()
        )

    except Exception as e:

        st.error(
            f"Delete failed: {e}"
        )

st.divider()

# =====================
# MEMORY DASHBOARD
# =====================

st.header("Memory Dashboard")

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
            "No memories stored yet."
        )

except Exception as e:

    st.error(
        f"Could not load memories: {e}"
    )