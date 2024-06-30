import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from main import send_email, generate_email_body
from sidebar import sidebar

load_dotenv()

sidebar()

st.title("📨 Cold email outreach AI agent")

uploaded_file = st.file_uploader(
    label="Choose your csv file",
    type=['csv'],
    help="Please upload a csv file with the following columns: name, email, description")

if not uploaded_file:
    st.info(
        """
        Please upload a csv file with the following columns: name, email, description. You can download a template
        from [here](templates/mailing_list_template.csv)!
        """
    )
else:
    df = pd.read_csv(uploaded_file)

    form = st.form(key='input fields')
    product_description = form.text_area(label="What is the product description?",
                                         placeholder="Example Wireless Earbuds 2.0, Premium sound in a wire-free "
                                                     "design. Rich audio, 8-hour battery, touch controls, "
                                                     "water-resistant. Charging case adds 24 hours. Perfect for "
                                                     "workouts or daily use. Available in black, white, navy.")
    personal_information = form.text_input(
        label="Please provide a name, position and name of company to be used as the addressed?",
        placeholder="John Wokorach, Job Position, Company",
        help="Separate the information using commas e.g Jordan, Software Developer, Remote Squad")

    subject_line = form.text_input(label="Enter a subject line for the email", )

    send_generate_emails = form.form_submit_button(label="Generate and send emails", use_container_width=True)

    if send_generate_emails:
        if not product_description:
            form.warning("Please provide a product description")
        elif not personal_information:
            form.warning("Please provide a name, position and name of company to be used as the addressed")
        elif not subject_line:
            form.warning("Please provide a subject line for the email")
        else:
            for index, row in df.iterrows():
                email = row['email']
                name = row['name']
                description = row['description']
                pain_points = row['pain_points']

                email_body = generate_email_body(name=name, description=description.join(pain_points),
                                                 sender_information=personal_information,
                                                 product_description=product_description)

                send_email(email, subject_line, email_body)

                st.write(f"""
                    Email sent to {name} with email at {email}
                    
                    ---
                    
                    Email body:
                    {email_body}
                """)
