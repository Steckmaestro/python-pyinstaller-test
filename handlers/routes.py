from calc.functions import add_values


def setup_routes(app):
    @app.route('/')
    def index():
        return '<h1>Hello, welcome to our mock calculator</h1>', 200

    @app.route('/add/<operands>')
    def addition(operands):
        oper1, oper2 = operands.split('&')
        result = add_values(oper1, oper2)
        return 'Result ' + str(result), 200
