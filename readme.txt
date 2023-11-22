API SmartCadastro | Flask, MySQL

A API SmartCadastro é um serviço web construído utilizando Flask e MySQL, fornecendo funcionalidades para gerenciamento de dados de usuários. Segue padrões como JWT para autenticação e inclui suporte para CORS. Abaixo estão as principais características e pontos de acesso:

Fazer Login no Sistema de Autenticação:

Endpoint: /api/login (POST)
• Descrição: Ao enviar os Dados de Login em formato Json para este EndPoint, a api retornará um Json com um Token Para acesso a api

Exemplo de Solicitação de Autenticação utilizando o Endpoint /api/login (POST):

{
    "username":"SeuLoginAqui"
    "password":"SuaSenhaAqui"
}

• No Codigo você tem acesso as configurações de username e password.

• Se as credenciais forem válidas, receberá como retorno um Json contendo o web Token.



Obter Dados do Usuário:

Endpoint: /api/cadastros (GET)
• Descrição: Recupera dados do usuário do banco de dados.


Enviar Dados do Usuário:

Endpoint: /api/enviar (POST)

• Descrição: Aceita e valida dados do usuário, inserindo-os no banco de dados.
Exemplo de Solicitação PUT utilizando o Endpoint /api/enviar (POST):

{
    "nome": "Joao Carlos",
    "idade": 25,
    "sexo": "M"
}


Atualizar Dados do Usuário:

Endpoint: /api/enviar/id (PUT)
• Descrição: Modifica os dados do usuário identificado pelo ID fornecido com novas informações.

Exemplo de Solicitação PUT utilizando o Endpoint /api/enviar:

{
    "nome": "Joao Carlos de Almeida",
    "idade": 25,
    "sexo": "M"
}



Atualização Parcial dos Dados do Usuário:

Endpoint: /api/alterar/id (PATCH)
• Descrição: Permite a atualização de campos específicos (nome, idade ou gênero) para um usuário identificado pelo ID fornecido.

Exemplo de Solicitação PATCH utilizando o Endpoint /api/alterar/id:

{
    "nome": "Joao Carlos de Almeida Marinho Prado",
}

Excluir Dados do Usuário:

Endpoint: /api/excluir/id (DELETE)
• Descrição: Exclui os dados do usuário associados ao ID fornecido.


Para que os Dados não retornem erro, garanta que os dados sigam estes padroes:

Json: Deve ser um objeto Json válido, como nos exemplos acima mencionados.
Nome: Obrigatório, 3 a 50 caracteres, alfabético.
Idade: Obrigatória, número inteiro positivo.
Gênero: Obrigatório, 'M' (masculino) ou 'F' (feminino).


A API utiliza Flask como framework web, MySQL para armazenamento de dados e incorpora suporte para CORS. Ela fornece pontos de acesso para operações CRUD, garantindo o manuseio seguro dos dados e seguindo as regras de validação especificadas.





