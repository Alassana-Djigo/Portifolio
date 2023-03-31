from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    #Roda apenas se estiver no index.html que é a __main__
    #"debug=True" Para actualizar sem ter que sair e entrar do servidor
