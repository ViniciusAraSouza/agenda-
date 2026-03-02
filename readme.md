# Agenda em Python em Flask

Este projeto foi elaborado para permiertir o aprendizadp de conceitos como o padrão de projeto MVC  (Model-View-Controller), framework Flask e seus componentes, variáveis de ambiente, paradigma de progamação orientado a objetos e reforço de fundamentos da linguagem de progamação Python.

Para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork deste repositório, clicando no botão `Fork` 

2. Clone este repositorio localmente:

~~~bash
git clone <url_repositorio>
~~~

3. Abra o projeto ultilizando seu IDE preferido

4. Crie, preferencialmente um ambiente virtual, ultilizando sua versão  do Python ou superior 3.12.10:

~~~bash
python -m venv .venv
~~~

5. Atuve seu ambiente virtual.

    No bash:

    ~~~bash
    source .venv/Scripts/activate
    ~~~

    No PowerShell:
    
    ~~~powerShell
    .\.venv\Scripits\Activate\ps1
    ~~~

6. Instale todas as dependencias constantes no `requirements.txt`:

~~~python
pip install -r requirements.txt
~~~

7. Copie o arquivo `.env.example` cole na raiz do projetoe renomeie a cópia para `.env`.

8. Edite o arquivo .env para definir o caminho de seu banco de dados na constante `DATABASE`. Exemplo:

~~~env
DATABASE='./data/meubanco.db'
~~~

9. Rode a aplicação no Pyhton ultilizando o comando:

~~~bash
flask run
~~~

10. Acesso a aplicação no endereço e porta indicados no terminal. Exemplo:`http://127.0.0.1:5000`
