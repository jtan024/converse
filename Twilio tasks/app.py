import json
from flask import send_file
from flask import jsonify, request
from flask import Flask
from test import push_data
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'


@app.route('/dynamicsay_requests', methods=['POST'])
def dynamic_say_requests():
    memory = json.loads(request.form.get('Memory'))
    print(memory)
    return send_file('dynamicsay_requests.json')


@app.route('/collect_requests',  methods=['POST'])
def collect_requests():

    memory = json.loads(request.form.get('Memory'))
    print(memory)
    answers = memory['twilio']['collected_data']['collect_clothes_order']['answers']

    first_name = answers['first_name']['answer']
    num_clothes = answers['num_clothes']['answer']
    push_data(first_name)
    message = (
        f'Okayy, {first_name}. Your order for {num_clothes} is now confirmed.'
        f' Thank you for ordering with us'
    )

    return jsonify(actions=[{'say': {'speech': message}}])
