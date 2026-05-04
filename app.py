from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "LUMINA - Biblioteca"

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify({"msg": "Lista de livros"})

@app.route("/livros", methods=["POST"])
def criar_livro():
    dados = request.json
    return jsonify({"msg": "Livro criado", "dados": dados})

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify({"msg": "Lista de usuários"})


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.json
    return jsonify({"msg": "Usuário criado", "dados": dados})

@app.route("/emprestimos", methods=["GET"])
def listar_emprestimos():
    return jsonify({"msg": "Lista de empréstimos"})


@app.route("/emprestimos", methods=["POST"])
def criar_emprestimo():
    dados = request.json
    return jsonify({"msg": "Empréstimo criado", "dados": dados})

if __name__ == "__main__":
    app.run(debug=True)