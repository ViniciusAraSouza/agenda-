from models.database import Database

class Tarefa:
    def __init__(self, titulo, tipo=None, data_conclusao=None, status='Pendente', id_tarefa=None, indicado_por=None):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.tipo = tipo
        self.data_conclusao = data_conclusao
        self.status = status
        self.indicado_por = indicado_por

    # Salva nova tarefa no banco
    def salvar_tarefa(self):
        with Database() as db:
            query = """
            INSERT INTO tarefas (titulo, tipo, data_conclusao, status, indicado_por)
            VALUES (?, ?, ?, ?, ?);
            """
            params = (self.titulo, self.tipo, self.data_conclusao, self.status, self.indicado_por)
            db.executar(query, params)

    # Atualiza tarefa existente
    def atualizar_tarefa(self):
        with Database() as db:
            query = """
            UPDATE tarefas SET titulo=?, tipo=?, data_conclusao=?, status=?, indicado_por=?
            WHERE id=?;
            """
            params = (self.titulo, self.tipo, self.data_conclusao, self.status, self.indicado_por, self.id_tarefa)
            db.executar(query, params)

    # Excluir tarefa
    def excluir_tarefa(self):
        with Database() as db:
            query = "DELETE FROM tarefas WHERE id=?;"
            db.executar(query, (self.id_tarefa,))

    # Marcar tarefa como concluída
    def concluir_tarefa(self):
        with Database() as db:
            query = "UPDATE tarefas SET status='Concluída' WHERE id=?;"
            db.executar(query, (self.id_tarefa,))

    # Retorna todas as tarefas
    @classmethod
    def obter_tarefas(cls):
        with Database() as db:
            query = "SELECT id, titulo, tipo, data_conclusao, status, indicado_por FROM tarefas;"
            resultados = db.buscar_tudo(query)

        tarefas = []
        for id_tarefa, titulo, tipo, data, status, indicado_por in resultados:
            tarefas.append(cls(titulo, tipo, data, status, id_tarefa, indicado_por))
        return tarefas

    # Retorna uma tarefa pelo ID
    @classmethod
    def id(cls, id_tarefa):
        with Database() as db:
            query = "SELECT id, titulo, tipo, data_conclusao, status, indicado_por FROM tarefas WHERE id=?;"
            resultado = db.buscar_tudo(query, (id_tarefa,))
            if resultado:
                id_tarefa, titulo, tipo, data, status, indicado_por = resultado[0]
                return cls(titulo, tipo, data, status, id_tarefa, indicado_por)
            return None