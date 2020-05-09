from generate_sonnets import generate_sonnet
from flask import Flask, render_template, make_response, request, jsonify, Response
from flask_compress import Compress

app = Flask(__name__)
Compress(app)
#background process to generate sonnets without any refreshing
@app.route('/initiate_generate_sonnets', methods=['GET', 'POST'])


def initiate_generate_sonnets():

    generated_sonnet = generate_sonnet()
    return jsonify(sonnet=generated_sonnet)


@app.route('/')
def index():
    return render_template('index.html')
    #return generate_sonnet()

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0',debug=True, threaded=True)

