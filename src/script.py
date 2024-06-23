
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from main import send_email, generate_email_body
from sidebar import sidebar

load_dotenv()

sidebar()

st.title("📨 Cold email outreach generator")

uploaded_file = st.file_uploader(label="Choose your csv file", type=['csv'],help="Please upload a csv file with the following columns: name, email, person_descritption")

if not uploaded_file:
    st.info("Please upload a csv file with the following columns: name, email, person_descritption. You can download a template from below!")
else:
    df = pd.read_csv(uploaded_file)
    
    form = st.form(key='input fields')
    product_description = form.text_area("What is the product description?", placeholder="Example Wireless Earbuds 2.0, Premium sound in a wire-free design. Rich audio, 8-hour battery, touch controls, water-resistant. Charging case adds 24 hours. Perfect for workouts or daily use. Available in black, white, navy.")
    personal_information = form.text_input(label="Please provide a name, position and name of company to be used as the adressee?", placeholder="John Wokorach, Job Position, Company", help="Separate the information using commas e.g Jordan, Software Developer, Remote Squad")
            
    send_generate_emails = form.form_submit_button(label="Generate and send emails", use_container_width=True)
    
    if send_generate_emails:
        if not product_description:
            form.warning("Please provide a product description")
        elif not personal_information:
            form.warning("Please provide a name, position and name of company to be used as the adressee")
        else:    
            for index, row in df.iterrows():
                email = row['email']
                name = row['name']
                description = row['description']
                
                email_body = generate_email_body(name=name, description=description, sender_information=personal_information, product_description=product_description)
                send_email(email, email_body)
                st.write(f"Sent email to {name} with email at {email}")