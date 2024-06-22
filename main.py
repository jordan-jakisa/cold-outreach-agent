import smtplib 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

session = None

user_email = "jordan.jakisa@gmail.com"
receipients = "jordan.jakisa@gmail.com"
product_description = "An enahnced IoT device that is empowering the text of the future. It enabled small scale developers to build and deploy their softwares to the cloud."


with smtplib.SMTP(host='smtp.gmail.com', port=587) as session:  
    session.starttls()
    session.login(user="jordan.jakisa@gmail.com", password='rkwa xmmf qwuq tdyi')
    session.sendmail(from_addr="dev.jordanempire@gmail.com", to_addrs="jordan.jakisa@gmail.com", msg="Hello, this is a test email to test my sample email client")

def send_email(receipient, subject, body):
    session.sendmail(from_addr=user_email, to_addrs=receipient, msg=body)

def generate_email_body(subject, body, user_information):
    prompt_template = """
    You are a sales cold email generator that writes personalized emails to potential clients.
    
    Using the following information about a client {user_information}
    
    Write a cold outreach email about the following product : {product_description}
    
    Instructions:
    Please include very clear prompts for the user to take action in response to the email.
    Only write the body of the email, do not include the subject line.
        
    """
    
    prompt = PromptTemplate.from_template(template=prompt_template)
    
    llm = ChatOpenAI()
    
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(input={"user_information": user_information, "product_description": product_description})
    print(response)
    
       
generate_email_body(subject="Test", body="Test", user_information="Jordan Mungujakisa, jordan.jakisa@gmail.com, he is a seasoned software developer in the space of AI and mobile app developenment")
    
    
    
    