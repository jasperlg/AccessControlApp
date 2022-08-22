from flask import Flask
from rest.auth import authBP
from rest.ticket import ticketBP
from rest.bankAccount import bankAccountBP
from rest.member import memberBP
from rest.payment import paymentBP

app = Flask(__name__)

app.register_blueprint(authBP, url_prefix='/auth')
app.register_blueprint(ticketBP, url_prefix='/ticket')
app.register_blueprint(bankAccountBP, url_prefix='/bankAccount')
app.register_blueprint(memberBP, url_prefix='/member')
app.register_blueprint(paymentBP)

if __name__ == "__main__":
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
