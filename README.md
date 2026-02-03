# 📨 Cold email outreach AI agent

This is a simple cold outreach email agent designed for sales people to generate sales emails based on a particular product 
and a particular user profile, pain points and description, it uses GPT-3.5 to generate custom emails for the product, tailored 
to each particular target, and then sends them to the people listed in a csv file.

## Here is an explanation of how it works and a demo 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/7t_dvpafawg/0.jpg)](https://www.youtube.com/watch?v=7t_dvpafawg)
## Tech used
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/docs/models)
- [Streamlit](https://streamlit.io/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)

## How to use
1. Create a `.env` file in the root directory and add the following values in it. 

```bash
USER_EMAIL=""
EMAIL_PASSWORD=""
```

Visit the followiing link to learn how to obtain an `app password` for your email. [How to create app passwords](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237)

2. Run the following command to run the app.

```bash
streamlit run src/main.py
```
