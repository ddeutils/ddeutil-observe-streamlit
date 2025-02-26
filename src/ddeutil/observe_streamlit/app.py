from pathlib import Path

import streamlit as st

this_path = Path(__file__).parent


pg = st.navigation(
    [
        st.Page(this_path / "pages/logs.py", title="Logs"),
        st.Page(this_path / "pages/workflows.py", title="Workflows"),
    ],
)
pg.run()
