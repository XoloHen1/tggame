from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранение данных пользователей (примитивный вариант)
user_scores = {}

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    user_id = data['user_id']
    score = data['score']
    
    # Сохраняем счет для пользователя
    user_scores[user_id] = score
    return jsonify(success=True)

@app.route('/get_score/<user_id>', methods=['GET'])
def get_score(user_id):
    score = user_scores.get(user_id, 0)
    return jsonify(score=score)

if __name__ == '__main__':
    app.run()
