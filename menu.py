import streamlit as st
from streamlit_option_menu import option_menu
import psutil
import pandas
from sklearn.linear_model import LinearRegression
import joblib
import qrcode
from io import BytesIO
from PIL import Image
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

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

# linux project 1

def why_linux():
    st.set_page_config(page_title="Why Companies Use Linux", layout="wide")


    st.title("Why Big Companies Are Switching to Linux – And What They're Getting Out of It")


    st.markdown("""
    In the digital-first era, the operating system used by an enterprise can have a profound impact on its performance, expense, and security. While Windows and macOS reign supreme on personal computers, **Linux has quietly dominated the corporate infrastructure**—most notably, in tech titans, banks, and cloud providers.

    So, why Linux for these firms? And, in particular, what are they getting out of it?

    Let us enter the realm of Linux and find out why some of the most influential organizations are committed to it.
    """)

    st.header("Why Are Companies Employing Linux?")

    st.markdown("""
    ### 1. Open Source & Affordable
    In contrast to commercial operating systems, Linux can be used, edited, and shared without cost. Companies can save huge sums of money on licensing, especially when growing (i.e., thousands of servers!).

    ### 2. Stability and Reliability
    Linux uptime is months or years. In mission-critical environments (web servers or banks), Linux's reliability ensures services stay online without constantly being rebooted.

    ### 3. Security
    The open-source feature of Linux allows global scrutiny of its code. With an effective permission and access control framework, the vulnerabilities are fixed instantly, and attack surfaces are minimized.

    ### 4. Performance and Personalization
    Linux is lightweight and modular. Businesses can trim out what they don't need, minimizing overhead and maximizing performance.

    ### 5. Developer-Friendly
    Linux is beloved for its command-line features, scripting, open-source utilities, and system-level access. Ideal for developers and DevOps teams.
    """)


    st.header("Which Companies Employ Linux — and How?")

    companies = {
        "Google": [
            "Use Case: Infrastructure backbone via custom 'gLinux'",
            "Why: Scalability, customization, tight integration",
            "Benefit: High data center efficiency, stack control"
        ],
        "Amazon (AWS)": [
            "Use Case: Internal + cloud services run Linux",
            "Why: Flexibility and secure virtualization",
            "Benefit: Reliable environments for millions"
        ],
        "Facebook (Meta)": [
            "Use Case: Backend servers",
            "Why: Efficiency at scale and custom network control",
            "Benefit: Cost optimization and speed"
        ],
        "IBM": [
            "Use Case: Powers mainframes and hybrid cloud",
            "Why: Enterprise-grade reliability and open standards",
            "Benefit: Stable, secure infrastructure"
        ],
        "Netflix": [
            "Use Case: Backend and content delivery network",
            "Why: Performance under heavy streaming",
            "Benefit: Fast deployment and minimal downtime"
        ],
        "NASA": [
            "Use Case: Servers, supercomputers, Mars rovers",
            "Why: Accuracy, precision, and critical mission reliability",
            "Benefit: Adaptable OS for scientific tasks"
        ],
        "Toyota": [
            "Use Case: Embedded systems, automotive software",
            "Why: Cost-efficient, customizable innovation (AGL)",
            "Benefit: Faster innovation, better vehicle software"
        ]
    }

    for company, details in companies.items():
        with st.expander(f"🔹 {company}"):
            for item in details:
                st.write(item)


    st.header("Benefits These Companies Receive")

    benefits_data = {
        "Benefit": [
            "Reduced Licensing Cost",
            "Improved Security",
            "Customizability",
            "Developer Agility",
            "Reliability",
            "Ecosystem Integration"
        ],
        "Impact": [
            "Saves millions annually in OS licensing",
            "Fewer attacks and rapid patching of vulnerabilities",
            "OS tailored to specific needs and hardware",
            "Quick development, deployment, and automation",
            "Systems run longer with fewer breakdowns",
            "Seamless integration with open-source tools and CI/CD pipelines"
        ]
    }

    df = pandas.DataFrame(benefits_data)
    st.dataframe(df, use_container_width=True)

    st.header("Future of Linux in Business")

    st.markdown("""
    With the momentum building towards **cloud-native**, **container-based**, and **AI-powered infrastructure**, the limelight is on Linux as the innovation leader.

    Technologies like **Kubernetes**, **Docker**, and **Edge Computing** are rooted in Linux. Even **Microsoft**, once a rival, now supports Linux in Azure and contributes to the kernel.

    **Linux isn't just surviving—it's thriving.**
    """)

    st.header("Final Thoughts")
    st.markdown("""
    Whether you have a **technology startup**, **run a data center**, or **develop software for autonomous systems**, Linux is increasingly the go-to platform for **elastic, secure, and agile systems**.
    """)

    st.markdown("---")







def linux_ai():
    key = "Enter your google gemini api key"
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
    
    st.set_page_config("Linux AI Terminal", layout="wide")

    st.markdown(
    """
    <style>
    @keyframes blink {
        0%   { opacity: 1; }
        50%  { opacity: 0.6; }
        100% { opacity: 1; }
    }
    .blink-icon {
        font-size: 30px; 
        font-weight: bold;
        color: lightgreen;
        vertical-align: middle;
        animation: blink 1s infinite;
    }
    </style>

    <h2 style='text-align: ; font-weight: bold;'>
        <i class="bi bi-terminal blink-icon"></i> Linux AI Terminal
    </h2>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
### Short Project Description:

This project creates an **AI-powered Linux terminal assistant** using the **Google Gemini API** via the **OpenAI-compatible interface**.  
It takes a user’s prompt and responds like a Linux terminal, providing solutions, commands, and explanations for technical queries.

This can be useful for:
- Simulating Linux terminal commands  
- AI-powered tech support  
- Learning and practicing Linux commands interactively
""")
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

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type a Linux command or question..."):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            with st.chat_message("assistant"):
                with st.spinner("Processing..."):
                    response = linux(prompt)
                    st.markdown(response)
       
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error occured due to : {e}")


# Python project 1
def memory_info():
    st.set_page_config(page_title="System Memory Info", layout="wide")
    st.title("System Memory Info",width=700)
    st.markdown("""
### Short Project Description:

This project is a simple Python script that uses the **`psutil`** library to monitor and display real-time **RAM statistics** of the system.  
It retrieves and prints the **total**, **available**, **used memory**, and **RAM usage percentage**, helping users understand their system's memory consumption.

This can be useful for:
-  Performance monitoring  
-  System diagnostics  
-  Building system management tools
""")
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
        st.info(f"Total RAM: {mem.total / (1024 ** 3):.2f} GB",width=190)
        st.info(f"Available RAM: {mem.available / (1024 ** 3):.2f} GB",width=190)
        st.info(f"Used RAM: {mem.used / (1024 ** 3):.2f} GB",width=190)
        st.info(f"RAM Usage: {mem.percent}%",width=190)

# Python project 2
def whatsapp_message():
    st.set_page_config(page_title="Whatsapp Automation", layout="wide")
    st.title("Whatsapp Message Automation",width=700)
    st.markdown("""
### Short Project Description:

This project is a Python-based automation tool that allows users to send WhatsApp messages instantly using the **`pywhatkit`** library.  
Users simply input the **receiver's mobile number** and their **message**, and the script sends it directly via WhatsApp Web with minimal delay.

This can be helpful for:
- Sending quick reminders or alerts  
- Broadcasting messages to contacts  
- Automating basic communication tasks
""")
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
    st.info("Try it out :-",width=104)
    phone_number = st.text_input("Enter receiver's mobile number with country code (e.g., +91xxxxxxxxxx):")
    message = st.text_input("Enter your message")
    if st.button("Send"):
        try:
            if not phone_number.strip():
                if not message.strip():
                    st.error("Fill required fields")
            else:
                import pywhatkit as kit
                kit.sendwhatmsg_instantly (phone_number, message, wait_time=15, tab_close=True)
                st.success("Message sent successfuly") 
        except ConnectionError as e:
            st.error(f"This require internet access : {e.reason}")

# Python project 3
def email_auto():
    st.set_page_config(page_title="Email Automation", layout="wide")
    st.title("Email Automation",width=700)
    st.markdown("""
### Short Project Description:

This project is a Python automation script that enables users to **send emails** directly using the **`smtplib`** and **`email`** libraries.  
Users input the **sender and receiver email addresses**, a message is composed, and it’s sent securely via **Gmail’s SMTP server**.

This can be useful for:
- Sending automated notifications or reports  
- Email-based alerts and reminders  
- Building custom communication tools
""")
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
    st.info("Try it out :-",width=104)
    try:
        import email
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        sender_email = st.text_input("Enter sender's email :")
        password = st.text_input("Enter your gmail app password :")
        receiver_email = st.text_input("Enter receiver's email :")
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
    st.markdown("""
### Short Project Description:

This project is a Python-based automation tool that uses the **`Twilio`** API to send WhatsApp messages programmatically.  
By providing the **Twilio Account SID**, **Auth Token**, sender's WhatsApp number, and recipient's number, the script sends a custom message instantly.

This can be useful for:
- Sending instant notifications via WhatsApp  
- Broadcasting messages to multiple users  
- Integrating WhatsApp alerts into applications
""")
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
    st.info("Try it out :-",width=104)
    from twilio.rest import Client
    account_sid = st.text_input("Enter your twilio account sid :")
    auth_token = st.text_input("Enter your twilio account token :")
    num =st.text_input("Enter twilio whatsapp number with country code :")
    twilio_whatsapp_number = "whatsapp:"+num

    number = st.text_input("Enter receiver's mobile number with country code :")
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
    st.markdown("""
### Short Project Description:

This project is a Python automation script that sends **SMS messages** using the **`Twilio`** API.  
By providing the **Twilio Account SID**, **Auth Token**, sender’s phone number, and recipient’s number, the script can deliver text messages instantly.

This can be useful for:
- Sending instant alerts or notifications  
- Broadcasting important updates to users  
- Integrating SMS features into applications
""")
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
    st.info("Try it out :-",width=104)
    from twilio.rest import Client
    account_sid = st.text_input("Enter your twilio account sid :")
    auth_token = st.text_input("Enter your twilio account token :")
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
            st.error(f"Falid to send : {e.args }")

# Python project 6
def call():
    st.set_page_config(page_title="Call Automation", layout="wide")
    st.title("Call Automation",width=400)
    st.markdown("""
### Short Project Description:

This project is a Python-based automation script that makes **voice calls** using the **`Twilio`** API.  
By providing the **Twilio Account SID**, **Auth Token**, caller number, and recipient number, the script can initiate automated phone calls with custom voice messages.

This can be useful for:
- Sending automated voice alerts  
- Delivering important updates via calls  
- Integrating voice call features into applications
""")
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
    st.info("Try it out :-",width=104)
    from twilio.rest import Client
    
    account_sid = st.text_input("Enter your twilio account sid :")
    auth_token = st.text_input("Enter your twilio account token :")

    client = Client(account_sid, auth_token)


    from_number = st.text_input("Enter twilio number with country code :") 
    to_number = st.text_input("Enter your mobile number with country code :")
    if st.button("Call"):
        try:
            call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml='<Response><Say>Hi! This is a test call from your Python script using Twilio. Have a nice day!</Say></Response>'
            )
            st.success(f"Call initiated. SID: {call.sid}")
    
        except Exception as e:
            st.error(f"Failed to call : {e.args}")

# Python project 7
def qr_gen():
    st.set_page_config(page_title="QR Code Generator", layout="wide")
    st.title("QR Code Generator")
    st.markdown("""
### Short Project Description:

This project is a Python script that generates **QR codes** for any given URL using the **`qrcode`** library.  
It creates a scannable QR code image, displays it, and saves it locally for future use.

This can be useful for:
- Sharing website links quickly  
- Event tickets, product info, or contact sharing  
- Printing QR codes for offline use
""")
    code = '''
import qrcode

url = "Enter url for which you want QR code "
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.show()
img.save("qr.png")
print(" QR code generated and saved as 'qr.png'")'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=550)
    st.info("Try it out :-",width=104)
    url = st.text_input("Enter the URL:", value="https://manojpf1.netlify.app/")
    gen = st.button("Generate")
    if gen:
        try:
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
            else:
                st.error("Enter valid URL")
        except Exception as e:
            st.error(f"Some Error Occured : {e}")

# Python project 8
def web_scraper():
    st.set_page_config("Web Scraper", layout="wide")
    st.title("Web Scraper")
    
    st.markdown("""
### Short Project Description:

This project is a **Streamlit-based web scraping tool** that extracts tutorial titles and links from websites like **GeeksforGeeks** or **TutorialsPoint**.  
It uses **`requests`** and **`BeautifulSoup`** to fetch and parse webpage content, and allows users to **download the extracted data as a CSV file**.

This can be useful for:
- Collecting tutorial resources for study  
- Creating structured learning material databases  
- Automating content extraction from educational websites
""")
    st.markdown("""
                Paste a tutorial page link (like from **GeeksforGeeks**, **TutorialsPoint**, etc.),  
                and this will extract all valid tutorial titles and links.
                Default: [GeeksforGeeks Python Page](https://www.geeksforgeeks.org/python-programming-language/)
                """)
    code = '''
import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://www.geeksforgeeks.org'
url = 'https://www.geeksforgeeks.org/python-programming-language/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
data_rows = []
links = soup.find_all('a', href=True)
for link in links:
    title = link.get_text(strip=True)
    href = link['href']
    if title and href.startswith('https://www.geeksforgeeks.org/python') and 'quiz' not in href:
        data_rows.append([title, href])
        print(f"Found: {title} -> {href}")
if data_rows:
    try:
        with open('geeksforgeeks_python_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Link'])
            writer.writerows(data_rows)
        print("Data successfully downloaded to geeksforgeeks_python_links.csv")
    except IOError as e:
        print(f"Error writing to file: {e}")
else:
    print("No data was found to write to the file.")'''
    check = st.checkbox("Show python code")
    if check:
        st.code(code,width=850)
    st.info("Try it out :-",width=104)
    input_url = st.text_input("Enter a tutorial page URL", value="https://www.geeksforgeeks.org/python-programming-language/")

    def scrape_from_url(url):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch page: {e}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        data_rows = []

        base_domain = '/'.join(url.split('/')[:3])

        links = soup.find_all('a', href=True)
        for link in links:
            title = link.get_text(strip=True)
            href = link['href']

            if href.startswith('/'):
                href = base_domain + href

            if title and href.startswith(base_domain) and 'quiz' not in href and 'javascript:void(0)' not in href:
                data_rows.append([title, href])

        return data_rows

    if st.button("Scrape Now"):
        try:
            if input_url.strip():
                with st.spinner("Scraping..."):
                    data = scrape_from_url(input_url.strip())

                if data:
                    df = pandas.DataFrame(data, columns=["Title", "Link"])
                    st.success(f"Found {len(df)} tutorial links!")
                    st.dataframe(df, use_container_width=True)

                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download as CSV",
                        data=csv,
                        file_name='scraped_tutorial_links.csv',
                        mime='text/csv'
                        )
                else:
                    st.warning("No valid links found on that page.")
            else:
                st.warning("Please enter a valid URL.")
        except Exception as e:
            st.error(f"Some error occured : {e}")


# Machine learning project 1
def marks_prediction():
    st.set_page_config(page_title="Student Marks Predictor ", layout="wide")
    st.title("Student Marks Predictor")
    st.markdown("""
### Short Project Description:

This project is a **machine learning app** built with **Streamlit** and **Scikit-learn** that predicts **student marks** based on the number of study hours.  
It uses a **Linear Regression** model trained on historical data from a CSV file to provide predictions.

This can be useful for:
- Understanding study time vs. performance correlation  
- Demonstrating basic machine learning concepts  
- Educational tools and learning analytics
""")
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
        m=mark[0]
        marks=int(m)
        st.success(f"This is your final marks : {marks}")

# Machine learning project 2
def result_predictor():

    model = joblib.load('marks_model.pkl')
    st.set_page_config(page_title="Student Result Predictor", layout="wide")
    st.title("Student Result Predictor")
    st.markdown("""
### Short Project Description:

This project trains a **Linear Regression** model using the **Scikit-learn** library to predict whether a student has **passed or failed** based on their marks.  
The trained model is saved as a **`.pkl` file** using the **Joblib** library for later use in prediction applications.

This can be useful for:
- Automating pass/fail predictions  
- Demonstrating model training and saving in ML  
- Creating educational machine learning projects
""")
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
    st.set_page_config(page_title="Salary Predictor", layout="wide")
    st.title("Salary Predictor")
    
    st.markdown("""
### Short Project Description:

This project uses **Logistic Regression** from **Scikit-learn** to predict an employee's salary category based on their years of experience.  
It reads data from a CSV file (`SalaryData.csv`), trains the model, and performs a sample prediction.

This can be useful for:
- Salary classification based on experience  
- Demonstrating classification algorithms in ML  
- Educational examples of Scikit-learn usage
""")
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
    model = joblib.load('Salary_pridictor.pkl')
    year = st.text_input("Enter your years of experience : ")
    if year !="":
        try:
            Experience = float(year)
        except Exception as e:
            st.error("Enter experience in float")
    if st.button("Predict"):
        salary = model.predict([[Experience]])
        int_salary = int(salary)
        st.success(f"Salary = {int_salary}")

# Machine learning project 4 
def sentiment():
    st.set_page_config(page_title="Sentiment Analyser", layout="wide")
    st.title("Sentiment Analyser")
    st.markdown("""
### Short Project Description:

This project performs **sentiment analysis** on user-provided text using the **`TextBlob`** library.  
It analyzes the input and returns **polarity** (how positive/negative the text is) and **subjectivity** (how opinionated the text is).

This can be useful for:
- Analyzing customer feedback  
- Understanding public sentiment in social media posts  
- Building AI-powered text analysis tools
""")
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
        options=["Home","Linux tasks", "Python projects", "Machine learning projects"],  
        icons=["bi-house", "bi-terminal", "bi-code-slash", "bi-cpu"],  
        menu_icon="cast",  
        default_index=0
    )


if selected =="Home":
    home_page()

if selected == "Linux tasks":
    linux_task = option_menu(
        menu_title="Linux Tasks",
        options=[
            "Task 1: Why Companies Use Linux",
            "Task 2: Linux AI Terminal"
            ], 
            icons=["bi-building", "bi-terminal"], 
                   menu_icon="bi-terminal", 
                   default_index=0, 
                   orientation="vertical"
                   )
    if linux_task == "Task 1: Why Companies Use Linux":
        why_linux()
    
    elif linux_task == "Task 2: Linux AI Terminal":
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
            "Project 7: QR Code Generator",
            "Project 8: Web Scraper"
            ], 
            icons=["bi-hdd", "bi-whatsapp", "bi-envelope", "bi-whatsapp", "bi-chat-left-text", 
            "bi-telephone", "bi-qr-code", "bi-globe"], 
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

    elif python_project == "Project 8: Web Scraper":
        web_scraper()

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
