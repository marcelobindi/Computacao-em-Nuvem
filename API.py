from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/attendance', methods=['GET'])
def get_attendance():
    # Código para buscar e retornar os registros de presença
    pass

@app.route('/attendance', methods=['POST'])
def post_attendance():
    data = request.json
    # Código para armazenar um novo registro de presença
    pass

if _name_ == '_main_':
    app.run(debug=True)