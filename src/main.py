import os
import smtplib
from email.message import EmailMessage

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Replace this email with your own  email
USER_EMAIL = "jordan.jakisa@gmail.com"
# Replace this password with your own email password
# To learn how to get your app password, visit https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237
USER_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(recipient, subject, body):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as session:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = 'jordan.jakisa@gmail.com'
        msg['To'] = recipient
        session.starttls()
        session.login(user=USER_EMAIL, password=USER_PASSWORD)
        session.sendmail(from_addr="jordan.jakisa@gmail.com", to_addrs=recipient, msg=body)
        session.send_message(msg=msg)


def generate_email_body(name, description, sender_information, product_description):
    prompt_template = """
        Create a concise and professional sales cold email targeting potential leads and clients. 
        Details to Include: 
        Recipient's Name: {name}
        Pain Points and Brief Note: {description} 
        Product Pitch: Provide a concise pitch for the product described in {product_description}. 
        
        Sender's Information: Use the details provided in {sender_information} to personalize the sender's signature 
        or closing remark. Present them in a professional manner.
        
          
        Instructions: 
        Focus solely on composing the email body; omit the subject line. 
        Ensure the email is clear, professional, and formatted for easy reading. 
        Limit the email to 100 words to maintain brevity and directness.
        
        Objective:
        Craft a compelling email that addresses the recipient's needs, introduces the product effectively, and 
        encourages a response or further engagement. 
        Remember, the goal is to generate interest in the product while keeping the message succinct and targeted.
                
    """

    prompt = PromptTemplate.from_template(template=prompt_template)

    llm = ChatOpenAI()

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(input={"product_description": product_description, "name": name, "description": description,
                                   "sender_information": sender_information})
    return response
