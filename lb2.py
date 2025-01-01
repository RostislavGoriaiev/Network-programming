from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# [Easy] Завдання 1: Запуск веб-сервера на порту 8000
@app.route('/')
def home():
    return "Веб-сервер працює!"

# [Easy] Завдання 2: Обробка GET-запиту, повернення "Hello World!"
@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello World!"

# [Easy-Medium] Завдання 3: Обробка GET-запиту зі шляхом та параметрами
@app.route('/currency', methods=['GET'])
def get_currency():
    key = request.args.get('key', 'default')  # Отримання параметра "key"
    today = request.args.get('today', False)  # Перевірка параметра "today"
    if today:
        return "USD - 41.5"
    return f"Запит із параметром key={key}"

# [Medium] Завдання 4: Обробка заголовків запиту (Content-Type)
@app.route('/headers', methods=['GET'])
def handle_headers():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        return jsonify({"message": "Це JSON-відповідь"})
    elif content_type == 'application/xml':
        response = make_response("<message>Це XML-відповідь</message>")
        response.headers['Content-Type'] = 'application/xml'
        return response
    else:
        return "Звичайний текстовий контент"

if __name__ == '__main__':
    app.run(port=8000)