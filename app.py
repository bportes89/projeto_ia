from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure sua chave da API OpenAI
openai.api_key = 'sua-chave-api'

# Lista para armazenar o histórico de conversas
conversations = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    # Adiciona a mensagem do usuário ao histórico
    conversations.append({'user': user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    
    bot_response = response['choices'][0]['message']['content']
    # Adiciona a resposta do bot ao histórico
    conversations.append({'bot': bot_response})
    
    return jsonify({'response': bot_response, 'history': conversations})

if __name__ == '__main__':
    app.run(debug=True)