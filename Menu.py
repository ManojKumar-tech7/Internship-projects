import streamlit as st
from streamlit_option_menu import option_menu
import psutil
import pandas
from sklearn.linear_model import LinearRegression
import joblib
import qrcode
from io import BytesIO
from PIL import Image

def home_page():
    st.title("Internship Projects Dashboard")
    st.markdown("---")

    st.subheader("About this Dashboard")
    st.write("""
    This dashboard contains projects created as part of my internship journey.
    It covers **Linux scripting**, **Python automation**, and **Machine Learning applications**.
    Use the sidebar to navigate between categories.
    """)

    st.subheader("Project Categories")
    st.markdown("""
    - **Linux Projects**:  
      AI Linux Terminal Assistant

    - **Python Projects**:  
      Automation tools including:
        - WhatsApp & Email automation  
        - SMS & Call services using Twilio  
        - QR Code Generator    

    - **Machine Learning Projects**:  
      Practical ML models like:
        - Student Marks Predictor  
        - Student Result Classifier  
        - Salary Prediction
        - Sentiment Analyser
    """)

    st.markdown("---")
    st.subheader("About Me")
    st.write("**Name:** Manoj Kumar")

    # Responsive buttons
    st.markdown(
        """
        <style>
        .button-container {
            display: flex; 
            justify-content: center; 
            gap: 80px; 
            margin-top: 10px;
            margin-bottom: 40px; /* <-- Added spacing below buttons */
            flex-wrap: wrap;
        }
        .social-btn {
            padding:14px 28px; 
            border:1px solid #999; 
            border-radius:8px; 
            background-color:#fff; 
            cursor:pointer; 
            display:flex; 
            align-items:center; 
            gap:10px;
            font-weight:600;
            font-size:16px;
            color:#000;
            transition: all 0.2s ease;
            min-width: 180px;
            justify-content: center;
        }
        .social-btn:hover {
            box-shadow:0px 4px 8px rgba(0,0,0,0.2);
            transform: scale(1.05);
        }
        .social-btn img {
            background: white;
            border-radius: 50%;
            padding: 3px;
            width: 24px;
            height: 24px;
        }
        @media (prefers-color-scheme: dark) {
            .social-btn { background-color:#222; color:#fff; border:1px solid #666; }
            .social-btn:hover { background-color:#333; }
        }
        @media (max-width: 768px) {
            .button-container { 
                flex-direction: column; 
                align-items: center; 
                gap: 20px; 
            }
        }
        </style>

        <div class="button-container">
            <a href="https://www.linkedin.com/in/manoj-kumar-82850a326" target="_blank">
                <button class="social-btn">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png"> LinkedIn
                </button>
            </a>
            <a href="https://github.com/ManojKumar-tech7" target="_blank">
                <button class="social-btn">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png"> GitHub
                </button>
            </a>
            <a href="https://manojpf1.netlify.app/" target="_blank">
                <button class="social-btn">
                    <img src="https://cdn-icons-png.flaticon.com/512/1828/1828673.png"> Portfolio
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.info("Use the sidebar to start exploring the projects!")

# linux project
def linux_ai():
    key = "Enter your google gemini api key"
    from openai import OpenAI
    OpenAI(api_key=key , base_url= "https://generativelanguage.googleapis.com/v1beta/openai/")
    gemini_model = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    def linux(prompt):
        msg =[
            {"role":"system", "content": "you are AI assistant work like a linux terminal solve doubts "},
            {"role":"user","content":prompt}
            ]
        response = gemini_model.chat.completions.create(model= "gemini-2.5-flash" , messages= msg)
        return response.choices[0].message.content
    
    st.set_page_config("Linux AI Terminal", layout="centered")
    st.title("AI Linux Assistant")
    code = '''
from openai import OpenAI
OpenAI(api_key=key , base_url= "https://generativelanguage.googleapis.com/v1beta/openai/")
gemini_model = OpenAI(
api_key=key,
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
def linux(prompt):
     msg =[
         {"role":"system", "content": "you are AI assistant work like a linux terminal solve doubts "},
        {"role":"user","content":prompt}
        ]
    response = gemini_model.chat.completions.create(model= "gemini-2.5-flash" , messages= msg)
    return response.choices[0].message.content'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code)
    st.write("Ask me anything like you would in a Linux terminal!")

    # Session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type a Linux command or question..."):
        # Save user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response
        try:
            with st.chat_message("assistant"):
                with st.spinner("Processing..."):
                    response = linux(prompt)
                    st.markdown(response)
        # Save assistant message
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error occured due to : {e}")


# Python project 1
def memory_info():
    st.set_page_config(page_title="System Memory Info", layout="wide")
    st.title("System Memory Info",width=700)
    code = '''
    import psutil
    mem = psutil.virtual_memory()
    print(f"Total RAM: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {mem.used / (1024 ** 3):.2f} GB")
    print(f"RAM Usage: {mem.percent}%")'''
    check = st.checkbox("Show python code",value=True)
        
    if check:
        st.code(code,width=600)
        
    mem = psutil.virtual_memory()
    if st.button("Run"):
        st.success(f"Total RAM: {mem.total / (1024 ** 3):.2f} GB",width=190)
        st.success(f"Available RAM: {mem.available / (1024 ** 3):.2f} GB",width=190)
        st.success(f"Used RAM: {mem.used / (1024 ** 3):.2f} GB",width=190)
        st.success(f"RAM Usage: {mem.percent}%",width=190)

# Python project 2
def whatsapp_message():
    st.set_page_config(page_title="Whatsapp Automation", layout="wide")
    st.title("Whatsapp Message Automation",width=700)
    code = '''
    import pywhatkit as kit 
    phone_number = input("Enter receiver's mobile number with country code (e.g., +91xxxxxxxxxx):")
    message = input("Enter your message")
    kit.sendwhatmsg_instantly (
                            phone_number,
                            message,
                            wait_time=15,
                            tab_close=True
                            )'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code, language= "python",width=600)
    phone_number = st.text_input("Enter receiver's mobile number with country code (e.g., +91xxxxxxxxxx):")
    message = st.text_input("Enter your message")
    try:    
        if st.button("Send"):
            import pywhatkit as kit 
            kit.sendwhatmsg_instantly (phone_number, message, wait_time=15, tab_close=True)
            st.success("Message sent successfuly")
                
    except ConnectionError as e:
        st.error(f"This require internet access : {e.reason}")

# Python project 3
def email_auto():
    st.set_page_config(page_title="Email Automation", layout="wide")
    st.title("Email Automation",width=700)
    code = '''
        import email
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        
        sender_email = input("Enter sender's email")
        receiver_email = input("Enter receiver's email")
        password = input("Enter sender's gmail password")
        
        subject = "Test Email from Python"
        body = "Hi there, This is a test email sent using Python!"
        
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            print(" Email sent successfully!")
        except Exception as e:
            print(f" Failed to send email: {e}")'''
    check = st.checkbox("Show python code")
    if check:
            st.code(code,width=700)
    try:
        import email
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        sender_email = st.text_input("Enter sender's email :")
        receiver_email = st.text_input("Enter receiver's email :")
        password = st.text_input("Enter your gmail app password :")
        subject = st.text_input("Enter subject :")
        body = st.text_input("Enter body")
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        try:
            if st.button("Send"):
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()  
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()
                st.success(" Email sent successfully!")
        except Exception as e:
            st.error(f" Failed to send email: {e}")
    except ConnectionError as e:
        st.error(f"This require internet access : {e.reason}")

# Python project 4
def whatsapp_twilio():
    st.set_page_config(page_title="Whatsapp Message Automation Via Twilio", layout="wide")
    st.title("Whatsapp Message Automation Via Twilio",width=900)
    code = '''
        from twilio.rest import Client
        
        account_sid = 'Enter your twilio account sid'
        auth_token = 'Enter your twilio account token'
        
        twilio_whatsapp_number = 'whatsapp:twilio whatsapp number with country code'
        
        to_number = 'whatsapp:your whatsapp number with countery code'
        
        client = Client(account_sid, auth_token)
        try:
            message = client.messages.create(
            from_=twilio_whatsapp_number,
            body='Hello from Twilio WhatsApp API via Python!',
            to=to_number
            )
            print(" Message sent! SID:", message.sid)
        except Exception as e:
            print(f"Failed to send message :{e}")'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=800)

    from twilio.rest import Client
    account_sid = st.text_input("Enter your twilio account sid :")
    auth_token = st.text_input("Enter your twilio Account token :")
    num = st.text_input("Enter twilio whatsapp number with country code :")
    twilio_whatsapp_number = 'whatsapp:'+num 

    number = st.text_input("Enter receiver's mobile number with country code")
    to_number = "whatsapp:"+number
    message = st.text_input("Enter your message :")
    client = Client(account_sid, auth_token)
    if st.button("Send"):
        try:
            message = client.messages.create(
                from_=twilio_whatsapp_number,
                body=message,
                to=to_number
                )
            st.success(f" Message sent! SID: {message.sid}")
        except Exception as e:
            st.error(f"Failed to send message :{e}")

# Python project 5
def sms():
    st.set_page_config(page_title="SMS Automation", layout="wide")
    st.title("SMS Automation",width=400)
    code = '''
    from twilio.rest import Client
        
    account_sid = 'Enter your twilio account sid'
    auth_token = 'Enter your twilio account token'
    twilio_number = 'twilio phone number with country code'  
    target_number = 'receiver's mobile number wiyh country code'  
        
    client = Client(account_sid, auth_token)
        
    try:
        message = client.messages.create(
        body="Hello! This is a test SMS sent from Python using Twilio.",
        from_=twilio_number,
        to=target_number
            )
        print(" SMS sent! SID:", message.sid)
    except Exception as e:
        print(f"Failed to send sms :{e})'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=650)

    from twilio.rest import Client
    account_sid = st.text_input("Enter your twilio account sid :")
    auth_token = st.text_input("Enter your twilio Account token :")
    twilio_number = st.text_input("Enter twilio number with country code :")  
    target_number = st.text_input("Enter your mobile number with countery code :")  
    your_message = st.text_input("Enter your message :")
    client = Client(account_sid, auth_token)
    if st.button("Send"):
        try:
            message = client.messages.create(
                body=your_message,
                from_=twilio_number,
                to=target_number
                )
            st.success(f" SMS sent! SID: {message.sid}")
        except Exception as e:
            st.error(f"Falid to send : {e}")

# Python project 6
def call():
    st.set_page_config(page_title="Call Automation", layout="wide")
    st.title("Call Automation",width=400)
    code = '''
    from twilio.rest import Client
    
    account_sid = 'Enter your twilio account sid'
    auth_token = 'Enter your twilio account token'
    twilio_number = 'twilio phone number with country code'  
    to_number = 'receiver's mobile number wiyh country code'  

    client = Client(account_sid, auth_token)  
    try:
        call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        twiml='<Response><Say>Hi!
                This is a test call from your Python script using Twilio. 
                Have a nice day!</Say></Response>'
        )
        print("Call initiated. SID:", call.sid)
    except Exception as e:
        print(f"Failed to call :{e}")'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=700)
    from twilio.rest import Client
    
    account_sid = st.text_input("Enter your twilio account sid :")
    auth_token = st.text_input("Enter your twilio Account token :")

    client = Client(account_sid, auth_token)


    from_number = st.text_input("Enter twilio number with country code :")  
    to_number = st.text_input("Enter your mobile number with country code")
    if st.button("Call"):
        try:
            call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml='<Response><Say>Hi! This is a test call from your Python script using Twilio. Have a nice day!</Say></Response>'
            )
            st.success(f"Call initiated. SID: {call.sid}")
    
        except Exception as e:
            st.error(f"Failed to call : {e}")

# Python project 7
def qr_gen():
    st.set_page_config(page_title="QR Code Generator", layout="wide")
    st.title("QR Code Generator")
    url = st.text_input("Enter the URL:", value="https://manojpf1.netlify.app/")
    gen = st.button("Generate")
    if gen:
        if url.strip():
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            img = qr_img.convert("RGB")
            
            st.image(img, caption="Scan this QR Code")

            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
            )

# Machine learning project 1
def marks_prediction():
    st.set_page_config(page_title="Student Marks Predictor ", layout="wide")
    st.title("Student Marks Predictor")
    code = '''
import streamlit as st
import pandas
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Student Marks Predictor", layout="wide")
st.title("Student Marks Predictor")

hours = st.slider("Select the number of study hours",min_value= 1 ,max_value= 10)


dataset = pandas.read_csv("marks.csv")

marks = dataset['marks'].values.reshape(-1,1)
hrs = dataset['hrs'].values.reshape(-1,1)
model = LinearRegression()
model.fit(hrs,marks)

if st.button("Predict"):
	mark = model.predict([[hours]])
	st.write(f"This is final marks {mark}")'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,language="python",width=600)
    
    hours = st.slider("Select the number of study hours",min_value= 0 ,max_value= 10)

    dataset = pandas.read_csv("marks.csv")

    marks = dataset['marks'].values.reshape(-1,1)
    hrs = dataset['hrs'].values.reshape(-1,1)
    model = LinearRegression()
    model.fit(hrs,marks)

    if st.button("Predict"):
        mark = model.predict([[hours]])
        marks=int(mark)
        st.success(f"This is your final marks : {marks}")

# Machine learning project 2
def result_predictor():

    model = joblib.load('marks_model.pkl')
    st.set_page_config(page_title="Student Result Predictor", layout="wide")
    st.title("Student Result Predictor")
    code = '''
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    'marks':[10,20,30,40,50,60,70,80],
    'result':[0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)

x = df[['marks']]
y = df[['result']]

model = LinearRegression()

model.fit(x,y)

model.predict([[40]])

joblib.dump(model , 'marks_model.pkl')'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=500)
    marks = st.number_input("Enter your marks : ", min_value = 0 , max_value = 100)

    if st.button("Predict"):
        result = model.predict([[marks]])
        if result[0] > 0.5:
            st.success("You are pass 🎉")
        else:
	        st.error("Sorry, you are fail 😥")

# Machine learning project 3
def salary_predictor():
    model = joblib.load('Salary_pridictor.pkl')
    st.set_page_config(page_title="Salary Predictor", layout="wide")
    st.title("Salary Predictor")
    code = '''
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

df=pd.read_csv("SalaryData.csv")

x= df[['YearsExperience']]
y=df[['Salary']]

model = LogisticRegression()
model.fit(x,y)

model.predict([[1.5]])'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=600)
    year = st.text_input("Enter your years of experience : ")
    if year !="":
        try:
            Experience = float(year)
        except Exception as e:
            st.error("Enter experience in float")
    if st.button("Predict"):
        salary = model.predict([[Experience]])
        int_salary = int(salary)
        st.write(f"Salary = {int_salary}")

# Machine learning project 4 
def sentiment():
    code = '''
from textblob import TextBlob

def Sentim():
    text = input("Enter any string : ")
    statement = TextBlob(text)
    senti = statement.sentiment
    return senti
    
Sentim()
'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=400)
    from textblob import TextBlob
    text = st.text_input("Enter any string : ")
    try:
        if st.button("Analyse"):
            if not text.strip(): 
                st.error("Please enter some text before analysis!")
            else:
                statement = TextBlob(text)
                senti = statement.sentiment
                st.success(senti)
    except Exception as e:
        st.error(f"Some Error Occured : {e}")

st.markdown(
    """
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
    """,
    unsafe_allow_html=True
)
st.set_page_config("Intership projects",layout="wide")
with st.sidebar:
    selected = option_menu(
        menu_title="Internship Projects",  
        options=["Home","Linux projects", "Python projects", "Machine learning projects"],  
        icons=["bi-house", "bi-terminal", "bi-code-slash", "bi-cpu"],  
        menu_icon="cast",  
        default_index=0
    )


if selected =="Home":
    home_page()

if selected == "Linux projects":
    linux_ai()

if selected == "Python projects":
    python_project = option_menu(
        menu_title="Python Projects",
        options=[
            "Project 1: System Memory Information",
            "Project 2: Whatsapp Message Automation",
            "Project 3: Email Automation",
            "Project 4: Whatsapp Message Automation Via Twilio",
            "Project 5: SMS Automation",
            "Project 6: Call Automation",
            "Project 7: QR Code Generator"
            ], 
            icons=["bi-hdd", "bi-whatsapp", "bi-envelope", "bi-whatsapp", "bi-chat-left-text", 
            "bi-telephone", "bi-qr-code"], 
                   menu_icon="bi-code-slash", 
                   default_index=0, 
                   orientation="vertical"
                   )
    if python_project == "Project 1: System Memory Information":
        memory_info()

    elif python_project == "Project 2: Whatsapp Message Automation" :
        whatsapp_message()

    elif python_project == "Project 3: Email Automation" :
        email_auto()

    elif python_project == "Project 4: Whatsapp Message Automation Via Twilio":
        whatsapp_twilio()

    elif python_project == "Project 5: SMS Automation":
        sms()

    elif python_project == "Project 6: Call Automation":
        call()

    elif python_project == "Project 7: QR Code Generator":
        qr_gen()

elif selected == "Machine learning projects":
    ml_project = option_menu(
        menu_title="Machine Learning Projects",
        options=[
            "Project 1: Student Marks Prediction",
            "Project 2: Student Result Prediction",
            "Project 3: Salary Predictor",
            "Project 4: Sentiment Analyser"
        ],
        icons=["bi-graph-up", "bi-check-circle", "bi-cash-stack", "bi-chat-square-text"],
        menu_icon="bi-cpu",
        default_index=0,
        orientation="vertical"
    )

    if ml_project == "Project 1: Student Marks Prediction":
        marks_prediction()
    
    elif ml_project == "Project 2: Student Result Prediction":
        result_predictor()

    elif ml_project == "Project 3: Salary Predictor":
        salary_predictor()
    
    elif ml_project == "Project 4: Sentiment Analyser":
        sentiment()