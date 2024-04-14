from flask import render_template, request, redirect, session, flash, url_for
from library import app, db
from models.models import Books


@app.get('/livros')
def index():
    books = Books.query.order_by(Books.id)
    return render_template('lista.html', titulo='books', books=books)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Livro')


@app.route('/criar', methods=['POST', ])
def criar():
    name = request.form['name']
    category = request.form['category']
    author = request.form['author']

    books = Books.query.filter_by(name=name).first()

    if books:
        flash('Livro já existente!')
        return redirect(url_for('index'))

    new_book = Books(name=name, category=category, author=author)
    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    book = Books.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando Livro', book=book)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    book = Books.query.filter_by(id=request.form['id']).first()
    book.name = request.form['name']
    book.category = request.form['category']
    book.author = request.form['author']

    db.session.add(book)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    Books.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Livro deletado com sucesso!')
    return redirect(url_for('index'))
