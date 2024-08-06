* [Venom Bot](#Venom-Bot)
* [Using Python, Selenium, and a Free NLP Service](#Using-Selenium)
* [Yowsup](#Yowsup)
<br>

# Venom-Bot

To create a WhatsApp chatbot you can use free and open-source solutions or services that offer free tiers. Here's a method using **WhatsApp Web automation with the `venom-bot` library**, which is a popular tool for interacting with WhatsApp without needing a paid API.


## **Using Venom-Bot for a Free WhatsApp Chatbot**

**Venom-Bot** allows you to create a WhatsApp bot by automating WhatsApp Web. It's suitable for personal or small-scale projects.


Here's a detailed guide on how to create a WhatsApp chatbot using **Venom-Bot** for free. This method involves using WhatsApp Web automation with Node.js and Venom-Bot. 

## **Step-by-Step Guide to Create a WhatsApp Chatbot Using Venom-Bot**

## **1. Prerequisites**

- **Node.js:** Make sure Node.js is installed on your machine.
  
- **WhatsApp Account:** A WhatsApp account to scan the QR code for connection.
  
- **Browser:** A modern browser like Google Chrome.
<br>

## **2. Install Node.js**

1. **Download and Install Node.js:**
   - Go to [Node.js official website](https://nodejs.org/).
     
   - Download the latest LTS version and follow the installation instructions.
<br>

## **3. Set Up Your Project**

1. **Create a New Directory for Your Project:**
   ```bash
   mkdir whatsapp-bot
   cd whatsapp-bot
   ```


2. **Initialize a New Node.js Project:**
   ```bash
   npm init -y
   ```


3. **Install Venom-Bot:**
   ```bash
   npm install venom-bot
   ```
<br>

## **4. Write Your Bot Code**

1. **Create a File Named `bot.js`:**

   In your project directory, create a file named `bot.js` and add the following code:

   ```javascript
   const venom = require('venom-bot');

   venom.create()
     .then((client) => start(client))
     .catch((error) => console.error('Error initializing venom-bot:', error));

   function start(client) {
     client.onMessage((message) => {
       const response = handleMessage(message.body);

       if (response) {
         client.sendText(message.from, response)
           .then((result) => {
             console.log('Message sent:', result);
           })
           .catch((error) => {
             console.error('Error sending message:', error);
           });
       }
     });
   }

   function handleMessage(message) {
     message = message.toLowerCase();

     if (message.includes('hi') || message.includes('hello')) {
       return 'Hi there! Welcome to the HR Bot. How can I assist you today?'
              + '\nType "job" to see available jobs.'
              + '\nType "apply" to apply for a job.'
              + '\nType "interview" to schedule an interview.'
              + '\nType "status" to check your application status.'
              + '\nType "faq" for frequently asked questions.';
     } else if (message.includes('job')) {
       return 'Available jobs:\n1. Software Engineer\n2. Data Scientist\n3. HR Manager';
     } else if (message.includes('apply')) {
       return 'To apply for a position, please send your resume to hr@example.com.';
     } else if (message.includes('interview')) {
       return 'Our interview process includes:\n1. Initial Screening\n2. Technical Interview\n3. HR Interview';
     } else if (message.includes('status')) {
       return 'Your application status is: Pending';
     } else if (message.includes('faq')) {
       return 'Frequently Asked Questions:\n1. How to apply?\n2. What are the interview steps?\n3. What are the job requirements?';
     } else {
       return 'I didn’t understand that. Please type "hi" to see the menu.';
     }
   }
   ```
<br>

## **5. Run Your Bot**

1. **Start the Bot:**
   ```bash
   node bot.js
   ```


2. **Scan the QR Code:**
   
   - When you run the bot for the first time, it will open a browser window.
     
   - Scan the QR code displayed with your WhatsApp mobile app to connect.


3. **Monitor the Console:**
   
   - Check the console for any logs or errors.
     
   - Ensure that the bot is receiving and sending messages as expected.
<br>

## **5. Test Your Bot**

1. **Send a Message to Your WhatsApp Number:**
   
   - Open WhatsApp on your phone.
     
   - Send a message to the number you used to connect with Venom-Bot.
     
   - Verify that the bot responds correctly based on the message you send.
<br>

## **6. Optional: Deployment**

If you want to run the bot continuously or make it publicly accessible:

- **Cloud Hosting:** Deploy to a cloud provider like [Heroku](https://www.heroku.com/) (free tier available) or other cloud services.

- **ngrok:** Use [ngrok](https://ngrok.com/) to tunnel your local server to a public URL if you want to expose your bot locally for testing.

By following these steps, you’ll have a basic WhatsApp chatbot running for free using Venom-Bot and Node.js.
<br>

Using Venom-Bot and WhatsApp Web automation is generally free of charge.

Summary of the costs involved:

## **1. Venom-Bot:**

- **Cost:** Free.
  
- **Usage:** Venom-Bot is an open-source library that automates WhatsApp Web, and it doesn’t have any associated costs.
<br>

## **2. WhatsApp Web:**

- **Cost:** Free.
  
- **Usage:** Using WhatsApp Web for personal automation doesn’t incur any costs.
<br>

## **3. Node.js and npm:**

- **Cost:** Free.
  
- **Usage:** Node.js and npm are open-source and free to use.
<br>

## **4. Hosting and Running the Bot:**

- **Local Development:** Free if you run the bot on your local machine.
  
- **Public Access:** If you want to make your bot accessible from the internet (e.g., using a cloud server), you might need to use a hosting provider. Many hosting services offer free tiers, but they may have limitations.
<br>

## **5. Compliance and Usage Considerations:**

- **Legal and Compliance Issues:** While Venom-Bot itself is free, you should be aware of WhatsApp’s terms of service. Automating WhatsApp Web could potentially violate their terms, especially for commercial use. Always ensure that your use case complies with WhatsApp’s policies.
<br>

**NOTE:** The tools and libraries mentioned are free, but you should consider compliance and any potential costs associated with hosting if you need to run the bot continuously and make it publicly accessible.



# Using-Selenium

Another fully free alternative for creating a WhatsApp chatbot involves using **Python and Selenium** for WhatsApp Web automation, combined with a Python library to handle natural language processing. Here’s how you can set this up:

## **Using Python, Selenium, and a Free NLP Service**

**Overview:**

- **Selenium** is a browser automation tool that can be used to interact with WhatsApp Web.
  
- **ChatGPT API** or other free NLP services can handle the chatbot logic.
  
- This method involves coding and running a local script.
<br>

## **Steps to Create a Free WhatsApp Chatbot Using Selenium**

## **1. Set Up Your Environment**

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Packages:**
   - Install `selenium` and `webdriver-manager` packages for browser automation.
     
   - Install an NLP library or use an open-source model for processing messages.
   ```bash
   pip install selenium webdriver-manager
   ```

3. **Download WebDriver:**
   - For Chrome, download the ChromeDriver from [ChromeDriver](https://sites.google.com/chromium.org/driver/). Place it in your PATH or specify the path in your script.
<br>

## **2. Write Your Chatbot Code**

1. **Create a Python Script Named `whatsapp_bot.py`:**

   Here’s an example of how you can set up a basic chatbot using Selenium and a free NLP service:

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.chrome.service import Service
   from selenium.webdriver.chrome.options import Options
   from webdriver_manager.chrome import ChromeDriverManager
   import time
   import requests

   # Set up Selenium WebDriver
   chrome_options = Options()
   chrome_options.add_argument("--user-data-dir=./User_Data")  # Keep session
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

   # Navigate to WhatsApp Web
   driver.get('https://web.whatsapp.com/')
   print("Please scan the QR code to log in.")

   time.sleep(20)  # Wait for user to scan QR code

   def get_chat_messages():
       messages = driver.find_elements(By.CSS_SELECTOR, "div._1pJ9J")
       return [msg.text for msg in messages]

   def send_message(contact_name, message):
       search_box = driver.find_element(By.CSS_SELECTOR, "div._2_1wd.copyable-text.selectable-text")
       search_box.click()
       search_box.send_keys(contact_name)
       time.sleep(2)  # Wait for search results

       contact = driver.find_element(By.XPATH, f"//span[@title='{contact_name}']")
       contact.click()

       message_box = driver.find_element(By.CSS_SELECTOR, "div._2A8P4.copyable-text.selectable-text")
       message_box.click()
       message_box.send_keys(message)
       message_box.send_keys("\n")  # Send message

   def process_message(message):
       # Replace this with your NLP logic or API call
       response = requests.post('https://api.openai.com/v1/engines/davinci/completions',
                                headers={
                                    'Authorization': 'Bearer YOUR_OPENAI_API_KEY',
                                    'Content-Type': 'application/json'
                                },
                                json={
                                    'prompt': message,
                                    'max_tokens': 50
                                }).json()
       return response['choices'][0]['text'].strip()

   while True:
       messages = get_chat_messages()
       for msg in messages:
           response = process_message(msg)
           send_message('Contact Name', response)  # Replace 'Contact Name' with actual contact

       time.sleep(10)  # Wait before checking for new messages
   ```


   **Notes:**
   - Replace `'YOUR_OPENAI_API_KEY'` with your OpenAI API key or use another NLP service.
     
   - Update `Contact Name` with the name of the contact or group you want to send responses to.
<br>

## **3. Run Your Chatbot**

1. **Execute the Script:**
   - Run your script using Python:
     ```bash
     python whatsapp_bot.py
     ```

2. **Monitor and Test:**
   - Monitor the script’s output and test the chatbot by sending messages to the WhatsApp contact or group.
<br>

## **4. Deployment (Optional)**

- **Local Server:** Keep the script running on your local machine.
  
- **Cloud Hosting:** For continuous operation, consider deploying the script on a cloud server like AWS, Heroku, or Google Cloud.
<br>

## **Advantages of Using Selenium:**

- **Free:** Selenium and Python are free to use.
  
- **Customizable:** Full control over the WhatsApp Web interface and automation logic.

By following these steps, you can create a fully free WhatsApp chatbot using Selenium for automation and a free NLP service for processing messages. This method offers flexibility and customization while avoiding paid services.



# Yowsup

To create a WhatsApp chatbot using **Python, Flask, and the yowsup library**. Yowsup is a Python library that allows you to build applications that communicate with WhatsApp. This method does not rely on Twilio or any paid service, making it a cost-effective solution.

## **Steps to Create a Free WhatsApp Chatbot Using Yowsup**

## **1. Set Up Your Environment**

1. **Install Python:**
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Yowsup:**
   - Yowsup is an open-source library for Python that allows you to connect to WhatsApp.
   - Install it by following the instructions below.

3. **Install Flask:**
   - Flask is a lightweight WSGI web application framework in Python.
   ```bash
   pip install Flask
   ```


## **2. Install Yowsup**

1. **Clone the Yowsup Repository:**
   ```bash
   git clone https://github.com/tgalal/yowsup.git
   cd yowsup
   ```

2. **Install Yowsup Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## **3. Configure Yowsup**

1. **Set Up Yowsup:**
   - You will need to register a WhatsApp account with Yowsup. Follow the [Yowsup documentation](https://github.com/tgalal/yowsup/wiki/yowsup-cli-2.0) to register your phone number and get the necessary credentials.


## **4. Write Your Chatbot Code**

1. **Create a Python Script Named `whatsapp_bot.py`:**

   ```python
   from flask import Flask, request, jsonify
   import subprocess

   app = Flask(__name__)

   # Endpoint to handle incoming messages from WhatsApp
   @app.route('/webhook', methods=['POST'])
   def webhook():
       incoming_message = request.json['Body']
       sender = request.json['From']

       response_message = process_message(incoming_message)
       send_message(sender, response_message)

       return jsonify({'status': 'success'})

   def process_message(message):
       # Process the incoming message and generate a response
       message = message.lower()
       if 'hi' in message or 'hello' in message:
           return ('Hi there! Welcome to the HR Bot. How can I assist you today?'
                   '\nType "job" to see available jobs.'
                   '\nType "apply" to apply for a job.'
                   '\nType "interview" to schedule an interview.'
                   '\nType "status" to check your application status.'
                   '\nType "faq" for frequently asked questions.')
       elif 'job' in message:
           return 'Available jobs: Software Engineer, Data Scientist, HR Manager.'
       elif 'apply' in message:
           return 'To apply for a position, please visit our careers page or send your resume to hr@example.com.'
       elif 'interview' in message:
           return 'To schedule an interview, please provide your availability.'
       elif 'status' in message:
           return 'Your application status: under review.'
       elif 'faq' in message:
           return ('Here are some frequently asked questions:\n'
                   '1. How to apply?\n'
                   '2. What are the interview steps?\n'
                   '3. What are the job requirements?')
       else:
           return 'Sorry, I did not understand that. Please type "hi" to see the menu.'

   def send_message(to, message):
       # Use Yowsup to send the message
       subprocess.call(['yowsup-cli', 'demos', '--login', 'phone:password', '--send', f'{to} "{message}"'])

   if __name__ == '__main__':
       app.run(debug=True)
   ```

   **Notes:**
   - Replace `phone:password` with your registered phone number and password obtained during Yowsup setup.
   - Customize the `process_message` function as needed.


### **5. Run Your Chatbot**

1. **Start the Flask App:**
   ```bash
   python whatsapp_bot.py
   ```

2. **Monitor and Test:**
   - Test the chatbot by sending messages to your registered WhatsApp number.


## **6. Deployment (Optional)**

- **Local Server:** Keep the script running on your local machine.
  
- **Cloud Hosting:** For continuous operation, consider deploying the script on a cloud server like AWS, Heroku, or Google Cloud.



## **Advantages of Using Yowsup:**

- **Free:** Yowsup is open-source and free to use.
  
- **Customizable:** Full control over the WhatsApp interface and automation logic.


