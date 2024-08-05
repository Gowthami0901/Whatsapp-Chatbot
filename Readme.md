# HOW TO CREATE WHATSAPP CHATBOT

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
