import smtplib 
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

session = None

def send_email(receipient, body):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as session:  
        session.starttls()
        session.login(user="jordan.jakisa@gmail.com", password=os.getenv("EMAIL_PASSWORD"))
        session.sendmail(from_addr="jordan.jakisa@gmail.com", to_addrs=receipient, msg=body)

def generate_email_body(name, description, sender_information, product_description):
    prompt_template = """
    
    You are a sales cold email generator that writes personalized emails to potential clients.
    
    The client we are writing to is called {name} and this is a bried note about them: {description}
    
    Write a cold outreach email about the following product : {product_description}
    
    This is information of the addresse who is sending the emails {sender_information}
        
    Instructions:
    Only write the body of the email, do not include the subject line.
    Do not include anything else in the output besides the email body.
    Format the email clearly and make it look professional.
    Make the email sound like it is coming from a real person.
    Make the email engaging logical, and persuasive.
    Make the email professional and respectful.
        
    """
    
    prompt = PromptTemplate.from_template(template=prompt_template)
    
    llm = ChatOpenAI()
    
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(input={"product_description": product_description, "name": name, "description": description, "sender_information": sender_information})
    return response
    
    
    
    