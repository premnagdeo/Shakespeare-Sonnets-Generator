from generate_sonnets import generate_sonnet
from flask import Flask, render_template, make_response, request, jsonify
from werkzeug.serving import WSGIRequestHandler


app = Flask(__name__)

#background process to generate sonnets without any refreshing
@app.route('/initiate_generate_sonnets', methods=['GET', 'POST'])
def initiate_generate_sonnets():

    print ("\n\nInitiated Generation")
    generated_sonnet = generate_sonnet()
    #print("\n\n\nGENERATED SONNET", generated_sonnet)
    return jsonify(sonnet=generated_sonnet)


@app.route('/')
def index():
    return render_template('index.html')
    #return generate_sonnet()

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0',debug=True)

