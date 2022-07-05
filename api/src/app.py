from flask import Flask
from rest.ticket import ticket

app = Flask(__name__)
app.register_blueprint(ticket, url_prefix='/ticket')


if __name__ == "__main__":
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
