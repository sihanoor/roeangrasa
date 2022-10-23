import streamlit as st
import pandas as pd 
import numpy as np 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,ssl

st.title("BD Triggers-Lead Generator Mail")
#uploaded_file = st.file_uploader("Choose a file")
temp_file = st.file_uploader("Enter file here!")
if temp_file: 
	temp_file_contents = temp_file.read()

if st.button("Save as working file"):
    with open("ON_DISK_FILE.extension","wb") as file_handle:
        file_handle.write(temp_file_contents)


result= st.button('Click To Send Mail')
st.write(result)
if result:

	my_email= "example@gmail.com"
	password= "********"



	server = smtplib.SMTP_SSL('smtp.gmail.com' ,465)
	server.ehlo()
	server.login(my_email, password)
	email_list = pd.read_excel("ON_DISK_FILE.extension") 
	st.write(email_list)
 

 
	#defining objects
	names = email_list['Lead Generated']
	emails = email_list['Lead generator Email']
	subjects = email_list["Subject"]    
	ccs=email_list['CCs']

	for i in range(len(emails)):
		name=names[i]
		email=emails[i]
		subject=subjects[i]
		cc=ccs[i]

		msg=MIMEMultipart()
		msg['Subject']=subject
		msg['From']=my_email
		msg["To"]=email
		msg["Cc"]=cc
		text="Hi"

		part1 = MIMEText(text, "plain")
		msg.attach(part1)
		
		server.sendmail(msg["From"], msg["To"].split(",") + msg["Cc"].split(","), msg.as_string())
	
	server.close()
