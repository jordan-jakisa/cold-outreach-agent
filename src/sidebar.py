import os

import streamlit as st


def sidebar():
    with st.sidebar:
        st.write("""
                 ## 📨 Cold email outreach AI agent"                 
                 """
                 )

        openai_api_key = st.text_input(
            label="OpenAI API Key",
            type="password"
        )

        os.environ['OPENAI_API_KEY'] = openai_api_key

        st.divider()

        st.write("""
        
        Made with ❤️ from Uganda by [jordan-jakisa](https://github.com/jordan-jakisa)
        """
                 )
