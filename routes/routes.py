from flask import render_template, request, redirect, session, flash, url_for
from library import app, db
from models.models import Books


@app.get('/')
def index():
    books = Books.query.order_by(Books.id)
    return render_template('lista.html', titulo='books', books=books)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Livro')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    autor = request.form['autor']

    livro = Books.query.filter_by(nome=nome).first()

    if livro:
        flash('Livro já existente!')
        return redirect(url_for('index'))

    novo_livro = Books(nome=nome, categoria=categoria, autor=autor)
    db.session.add(novo_livro)
    db.session.commit()

    return redirect(url_for('index'))
