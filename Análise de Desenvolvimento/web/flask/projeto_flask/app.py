from flask import Flask, render_template

app = Flask(__name__)

@app.route('/aluno')
def aluno():
    return render_template("aluno.html", nome_aluno='Rafael', matricula=123456, nota=5.9)

app.run(debug=True)