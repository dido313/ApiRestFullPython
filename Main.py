from flask import Flask, request, jsonify
from flask_cors import CORS
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import mysql.connector

app = Flask(__name__)
CORS(app)
# Configuração do banco de dados
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "3694481",
    "database": "cadastros",
    "autocommit": True  # Para evitar a necessidade de commit manual
}

# app.config["JWT_SECRET_KEY"] = "ChaveSecreta123"  # Substitua por uma chave secreta forte
# jwt = JWTManager(app)


con = mysql.connector.connect(**db_config)
def validar_nome(data):
    nome = data.get("nome")
    if not nome or not isinstance(nome, str) or not 3 <= len(nome) <= 50:
     return False, "O campo 'nome' é obrigatório e deve ter entre 3 e 50 caracteres."

def validar_idade(data):
    idade = data.get("idade")
    if not idade or not isinstance(idade, int) or idade <= 0:
     return False, "O campo 'idade' é obrigatório e deve ser um número inteiro positivo."

def validar_sexo(data):
    sexo = data.get("sexo")
    if not sexo or not isinstance(sexo, str) or sexo not in ("M", "F"):
     return False, "O campo 'sexo' é obrigatório e deve ser 'M' (masculino) ou 'F' (feminino)."
    

def validar_dados(data):
    nome = data.get("nome")
    idade = data.get("idade")
    sexo = data.get("sexo")

    if not nome or not isinstance(nome, str) or not 3 <= len(nome) <= 50:
        return False, "O campo 'nome' é obrigatório e deve ter entre 3 e 50 caracteres."

    if not idade or not isinstance(idade, int) or idade <= 0:
        return False, "O campo 'idade' é obrigatório e deve ser um número inteiro positivo."

    if not sexo or not isinstance(sexo, str) or sexo not in ("M", "F"):
        return False, "O campo 'sexo' é obrigatório e deve ser 'M' (masculino) ou 'F' (feminino)."

    return True, ""

def execute_query(query, values=None, fetchall=False):
    cursor = con.cursor()
    try:
        cursor.execute(query, values)
        result = cursor.fetchall() if fetchall else None
        return result
    finally:
        cursor.close()

@app.route('/api/cadastros', methods=['GET'])  #Testado
# @jwt_required()
def obter_dados_exemplo():
    query = "SELECT * FROM pessoas"
    result = execute_query(query, fetchall=True)
    return jsonify(result)

@app.route('/api/enviar', methods=['POST'])
# @jwt_required()
def receber_dados():
        data = request.get_json()
        nome = data.get("nome")
        idade = data.get("idade")
        sexo = data.get("sexo")
   
        is_valid, error_message = validar_dados(data)

        if is_valid:
         query_insert = "INSERT INTO pessoas (nome, idade, sexo) VALUES (%s, %s, %s)"
         values_insert = (nome, idade, sexo)
         execute_query(query_insert, values_insert)
         return jsonify({"mensagem": "Dados inseridos com sucesso!"}), 201
        else :
         return jsonify({"erro": error_message}), 400
    

@app.route('/api/enviar/<int:id>', methods=['PUT'])   # PUT É USADO PARA MODIFICAR COMPLETAMENTE O RECURSO
# @jwt_required()
def atualizar_dados(id):
    data = request.get_json()
    nome = data.get("nome")
    idade = data.get("idade")
    sexo = data.get("sexo")

    is_valid, error_message = validar_dados(data)

    if is_valid:
        # Substitua este trecho pela lógica adequada para atualizar os dados no banco de dados
        query_update = "UPDATE pessoas SET nome = %s, idade = %s, sexo = %s WHERE id = %s"
        values_update = (nome, idade, sexo, id)
        execute_query(query_update, values_update)
        # Aqui, estamos apenas simulando a atualização de um elemento na lista como banco de dados
       
        return jsonify({"mensagem": f"Dados do ID {id} atualizados com sucesso!"}), 200
        
    else:
        return jsonify({"erro": error_message}), 400
 


@app.route('/api/alterar/<int:id>', methods=['PATCH'])     #aqui ele tem que identificar que campo do dado que veio, e fazer a devida alteração sql baseado no dado que veio
# @jwt_required()                                           # PATCH É USADO PARA MODIFICAR PARCIALMENTE O RECURSO 
def alterar_cadastro_existente(id):
    if request.is_json:
        data = request.get_json()
        nome = data.get("nome")
        idade = data.get("idade")
        sexo = data.get("sexo")
        if "nome" in data and data["nome"]:
         validar_nome(data)
         query_update = "UPDATE pessoas SET nome = %s WHERE id = %s"                                             #, idade = %s, sexo = %s WHERE id = %s
         values_update = (nome, id)
         execute_query(query_update, values_update)
         return jsonify({"mensagem": "Nome atualizado com sucesso!"}), 200
        
        if "idade" in data and data["idade"]:
         validar_idade(data)
         query_update = "UPDATE pessoas SET idade = %s WHERE id = %s"                                             #, idade = %s, sexo = %s WHERE id = %s
         values_update = (idade, id)
         execute_query(query_update, values_update)
         return jsonify({"mensagem": "Idade atualizada com sucesso!"}), 200
        
        if "sexo" in data and data["sexo"]:
         validar_sexo(data)
         query_update = "UPDATE pessoas SET sexo = %s WHERE id = %s"                                             #, idade = %s, sexo = %s WHERE id = %s
         values_update = (sexo, id)
         execute_query(query_update, values_update)
         return jsonify({"mensagem": "Sexo atualizado com sucesso!"}), 200
        
    else:
        return jsonify({"erro": "A solicitação deve conter dados JSON"}), 400

@app.route('/api/excluir/<int:id>', methods=['DELETE'])
# @jwt_required()
def excluir_cadastro(id):
    query_delete = "DELETE FROM pessoas WHERE id = %s"
    values_delete = (id,)
    execute_query(query_delete, values_delete)

    return jsonify({"mensagem": "Cadastro excluído com sucesso!"}), 200

'''
@app.route('/api/login', methods=['POST'])
def login():
    if request.is_json:
        data = request.get_json()
        username = data.get("username")  # Substitua pelos campos reais de login
        password = data.get("password")  # Substitua pelos campos reais de login

        # Adicione lógica de autenticação aqui (por exemplo, verifique usuário/senha no banco de dados)
        if username == "dido" and password == "123":
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"erro": "Credenciais inválidas"}), 401
    else:
        return jsonify({"erro": "A solicitação deve conter dados JSON"}), 400
'''

if __name__ == '__main__':
    app.run()