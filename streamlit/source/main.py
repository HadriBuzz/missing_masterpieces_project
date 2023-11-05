import streamlit as st
import requests
import json

x = st.slider("Please select input x:", 0, 100, 20)
y = st.slider("Please select input y:", 0, 100, 20)

if st.button("Calculate"):
    inputs = {"x": x, "y": y}

    res = requests.post(
        url="http://backend-sqlite-fastapi:8702/return_sum", data=json.dumps(inputs)
    )

    st.write(f"Sum is: {res.text}")
