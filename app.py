from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para obter resultados da FURIA
@app.route('/get_furia_results')
def get_furia_results():
    furia_matches = get_furia_match_results()
    return jsonify(furia_matches)


# Rota de recebimento e envio de mensagens
@socketio.on('message')
def handle_message(msg):
    print('Mensagem recebida: ' + msg)
    send(msg, broadcast=True)

# Evento de conexão
@socketio.on('connect')
def handle_connect():
    print("Novo usuário conectado!")
    send("Novo usuário conectado!", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

## @VERSION: 1.0.0
## @AUTHOR: DIOGOLEITE
## @YEAR: 2025
## @DESCRIPTION: Aplicação Flask com SocketIO para chat de comunicação em tempo real.
## @GITHUB: https://github.com/Diogordo08
## @PORTFOLIO: https://diogordo08.github.io