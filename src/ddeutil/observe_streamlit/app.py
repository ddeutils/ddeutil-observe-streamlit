# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Requester", "Responder", "Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page(
    "./settings.py", title="Settings", icon=":material/settings:"
)


if __name__ == "__main__":
    st.set_page_config(page_title="Lets observe", page_icon="💻")
    st.markdown(
        "[![Observe Logo](app/static/img/logo.png)](http://localhost:8501)"
    )
    st.title("Lets observe with a Website")
