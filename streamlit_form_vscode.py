import streamlit as st
import re
from pymongo import MongoClient
import datetime

uri = "mongodb+srv://pranjal:pranjal@database1.lcv8h5t.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client["pranbha2"]
collection = db["Form_Details"]

num = False
num2 = False
num3 = False
num4 = False
submit = False
st.header("User Registration")
st.write("<h1 style = 'text-align: center;'>Form-1 </h1>", unsafe_allow_html = True)
with st.form("Form-1", clear_on_submit = True):
    col1, col2 = st.columns(2)
    fname = col1.text_input("First Name", key = "fname")
    sname = col2.text_input("Second Name", key = "sname")
    email = st.text_input("E-mail", key = "email")
    password = st.text_input("Password", key = "pass")
    con_password = st.text_input("Confirm Password", key = "conpass")
    date = st.date_input("Today's date", key = "date")
    # Assuming you have a datetime.date object 'my_date'
    #my_date = datetime.date(2023, 7, 20)

    # Convert datetime.date to datetime.datetime
    date = datetime.datetime.combine(date, datetime.datetime.min.time())
    print(date)
    state = st.form_submit_button("Submit")

    if state:
        if fname == "" or sname == "" or email == "" or password == "" or con_password == "":
            st.warning("Please fill all the mandatory fields")
        else:
            num = True
        if email:
            if "@" not in email and "." not in email:
                st.warning("Please include . and @ and write correct e-mail")
            elif "@" not in email:
                st.warning("Include @ and write correct e-mail")
            elif "." not in email:
                st.warning("Include . and write correct e-mail")
            else:
                num2 = True
        if password:
            if not re.search("[a-z]", password):
                st.warning("There should be atleast 1 lowercase letter")
            if not re.search("[A-Z]", password):
                st.warning("There should be atleast 1 uppercase letter")
            if not re.search("[0-9]", password):
                st.warning("There should be atlest 1 number")
            if not re.search("[!@#$^&*]", password):
                st.warning("There should be atleast 1 special character")
            else:
                num3 = True
        if password != con_password:
            st.warning("Password and Confirm Password should be equal")
        else:
            num4 = True
        if num == True and num2 == True and num3 == True and num4 == True:
            submit  = True
        
        if submit is True:
            data = {"First Name" : st.session_state["fname"], 
                    "Second namae" : st.session_state["sname"], 
                    "Email-Id" : st.session_state["email"], 
                    "Password" : st.session_state["pass"], 
                    "Confirm Passwod" : st.session_state["conpass"], 
                    "Today's Date" : st.session_state["date"]}
            collection.insert_one(data)
            st.success("Submitted Successfully")