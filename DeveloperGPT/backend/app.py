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

# Function to generate AI responses based on user input
def generate_response(user_message):
    # Basic keyword detection for different types of questions
    if 'how to test' in user_message.lower():
        return "To test effectively, define clear test cases and use automated testing tools."
    elif 'what is unit testing' in user_message.lower():
        return "Unit testing is a type of testing where individual units or components of a software are tested in isolation."
    elif 'why do we test software' in user_message.lower():
        return "Software testing helps identify bugs and errors early in the development lifecycle, ensuring better quality."
    else:
        # If no specific condition is met, query Ollama for a response
        messages = [{'role': 'user', 'content': user_message}]
        chat_output = run_chat(messages)
        chat_output = ' '.join(chat_output)
        return chat_output


# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get user input message
    user_message = request.form['user_message']
    
    # Generate AI response based on user input
    ai_response = generate_response(user_message)
    
    # Prepare messages to send to ollama (you can adjust this logic based on your needs)
    messages = [{'role': 'user', 'content': user_message},
                {'role': 'assistant', 'content': ai_response}]
    
    # Optionally, you can still use Ollama for more sophisticated responses
    # chat_output = run_chat(messages)
    chat_output = [ai_response]  # For now, using simple response
    return render_template('index.html',  chat_output=chat_output, user_message=user_message)

if __name__ == '__main__':
    app.run(debug=True)
