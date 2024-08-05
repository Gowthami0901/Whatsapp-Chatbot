from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    msg = request.form.get('Body').lower()
    resp = MessagingResponse()

    if 'hi' in msg:
        resp.message('Hi there! How can I assist you today?')
    elif 'job' in msg:
        resp.message('Available jobs: Software Engineer, Data Scientist')
    else:
        resp.message('I didn’t understand that. Please type "hi" to see the menu.')

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
