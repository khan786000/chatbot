from bottle import Bottle, request, static_file, run
import google.generativeai as ai

# Initialize Bottle app
app = Bottle()

# API Key
API_KEY = 'AIzaSyB8WK-KzwA3OV6VMZ8tJVCWi7FKAKcoYR4'
# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route('/')
def index():
    return static_file('index.html', root='./')

@app.route('/chatbot', method='POST')
def chatbot():
    user_input = request.json.get('message')
    response_body = chat.send_message(user_input)
    return {'response': response_body.text}

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
