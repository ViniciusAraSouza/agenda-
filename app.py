from flask import Flask, render_template, request, redirect, url_for
from models.database import init_db
from models.tarefa import Tarefa


app = Flask(__name__)  # Cria a aplicação Flask

init_db()  # Inicializa o banco de dados e cria a tabela se não existir

# Página inicial
@app.route('/')
def home():
    return render_template("home.html", titulo='Lista de Desejos')

# -------------------------
# Página da agenda (lista e criação de tarefas)
# -------------------------
@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        # Pega os dados do formulário
        titulo = request.form['titulo-tarefa']
        tipo = request.form.get('tipo-tarefa')
        data = request.form.get('data-conclusao')
        status = request.form.get('status', 'Pendente')
        indicado_por = request.form.get('indicado-por')

        # Cria objeto Tarefa e salva no banco
        tarefa = Tarefa(titulo, tipo, data, status, None, indicado_por)
        tarefa.salvar_tarefa()

        return redirect(url_for('agenda'))

    # Busca todas as tarefas para exibir
    tarefas = Tarefa.obter_tarefas()

    return render_template(
        'agenda.html',
        titulo='Lista de Desejos',
        tarefas=tarefas
    )

# -------------------------
# Rota para excluir tarefa
# -------------------------
@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    if tarefa:
        tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

# -------------------------
# Rota para atualizar tarefa
# -------------------------
@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):
    tarefa_selecionada = Tarefa.id(idTarefa)

    if request.method == 'POST':
        # Atualiza dados do formulário
        tarefa_selecionada.titulo = request.form['titulo-tarefa']
        tarefa_selecionada.tipo = request.form.get('tipo-tarefa')
        tarefa_selecionada.data_conclusao = request.form.get('data-conclusao')
        tarefa_selecionada.status = request.form.get('status', tarefa_selecionada.status)
        tarefa_selecionada.indicado_por = request.form.get('indicado-por')     

        # Salva atualização no banco
        tarefa_selecionada.atualizar_tarefa()
        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()

    return render_template(
        'agenda.html',
        titulo='Editando tarefa',
        tarefas=tarefas,
        tarefa_selecionada=tarefa_selecionada
    )

# -------------------------
# Rota para concluir tarefa
# -------------------------
@app.route('/concluir/<int:idTarefa>')
def concluir(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    if tarefa:
        tarefa.concluir_tarefa()
    return redirect(url_for('agenda'))

# -------------------------
# Executa a aplicação Flask
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)