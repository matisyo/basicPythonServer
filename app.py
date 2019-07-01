from flask import Flask,request
app = Flask(__name__)

@app.route('/usuario/<int:idusuario>')
def get_user(idusuario, methods=['GET', 'POST']):
	if request.method == 'POST':
		return f'Fue POST -> {idusuario}'
	return f'Fue GET -> {idusuario}'
