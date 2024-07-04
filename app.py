from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

# Define your chat function
def run_chat(messages):
    stream = ollama.chat(
        model='llama2',
        messages=messages,
        stream=True,
    )
    chat_output = []
    for chunk in stream:
        chat_output.append(chunk['message']['content'])
    return chat_output

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get user input message
    user_message = request.form['user_message']
    
    # Prepare messages to send to ollama
    messages = [{'role': 'user', 'content': user_message}]
    
    # Run the chat function
    chat_output = run_chat(messages)
    return render_template('index.html', chat_output=''.join(chat_output), user_message=user_message)

   # return render_template('index.html', chat_output=chat_output, user_message=user_message)

if __name__ == '__main__':
    app.run(debug=True)
