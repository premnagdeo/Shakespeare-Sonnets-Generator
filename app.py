from generate_sonnets import generate_sonnet
from flask import Flask, render_template, make_response, request, jsonify, Response

app = Flask(__name__)

@app.route('/return_response', methods=['GET', 'POST'])
def return_response():
    print('heel')
    return '''Generating Sonnet Please Wait'''
    #return jsonify({'status': 'Generating Sonnet Please Wait'})

#background process to generate sonnets without any refreshing
@app.route('/initiate_generate_sonnets', methods=['GET', 'POST'])
def initiate_generate_sonnets():
    generated_sonnet = generate_sonnet()
    return jsonify(sonnet=generated_sonnet)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, threaded=True)