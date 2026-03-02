from models.database import Database


class Tarefa:
    def __init__(self, titulo, tipo=None, data_conclusao=None,
                 status='Pendente', id_tarefa=None, indicado_por=None):

        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.tipo = tipo
        self.data_conclusao = data_conclusao
        self.status = status
        self.indicado_por = indicado_por

    def salvar_tarefa(self):
        with Database() as db:
            query = """
            INSERT INTO tarefas (titulo, tipo, data_conclusao, status, indicado_por)
            VALUES (?, ?, ?, ?, ?);
            """
            params = (
                self.titulo,
                self.tipo,
                self.data_conclusao,
                self.status,
                self.indicado_por
            )
            db.executar(query, params)

    def atualizar_tarefa(self):
        with Database() as db:
            query = """
            UPDATE tarefas
            SET titulo=?, tipo=?, data_conclusao=?, status=?, indicado_por=?
            WHERE id=?;
            """
            params = (
                self.titulo,
                self.tipo,
                self.data_conclusao,
                self.status,
                self.indicado_por,
                self.id_tarefa
            )
            db.executar(query, params)

    def excluir_tarefa(self):
        with Database() as db:
            db.executar("DELETE FROM tarefas WHERE id=?;", (self.id_tarefa,))

    def concluir_tarefa(self):
        with Database() as db:
            db.executar("UPDATE tarefas SET status='Concluída' WHERE id=?;", (self.id_tarefa,))

    @classmethod
    def obter_tarefas(cls):
        with Database() as db:
            resultados = db.buscar_tudo("""
                SELECT id, titulo, tipo, data_conclusao, status, indicado_por
                FROM tarefas;
            """)

        tarefas = []
        for id_tarefa, titulo, tipo, data, status, indicado_por in resultados:
            tarefas.append(
                cls(titulo, tipo, data, status, id_tarefa, indicado_por)
            )
        return tarefas

    @classmethod
    def obter_por_id(cls, id_tarefa):
        with Database() as db:
            resultado = db.buscar_tudo("""
                SELECT id, titulo, tipo, data_conclusao, status, indicado_por
                FROM tarefas
                WHERE id=?;
            """, (id_tarefa,))

        if resultado:
            id_tarefa, titulo, tipo, data, status, indicado_por = resultado[0]
            return cls(titulo, tipo, data, status, id_tarefa, indicado_por)

        return None