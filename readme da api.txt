API SmartCadastro | Flask, MySQL

A API SmartCadastro é um serviço web construído utilizando Flask e MySQL, fornecendo funcionalidades para gerenciamento de dados de usuários. Segue padrões como JWT para autenticação e inclui suporte para CORS. Abaixo estão as principais características e pontos de acesso:

Obter Dados do Usuário:

Endpoint: /api/cadastros (GET)
Descrição: Recupera dados do usuário do banco de dados.
Enviar Dados do Usuário:

Endpoint: /api/enviar (POST)
Descrição: Aceita e valida dados do usuário, inserindo-os no banco de dados.
Atualizar Dados do Usuário:

Endpoint: /api/enviar/<int:id> (PUT)
Descrição: Modifica os dados do usuário identificado pelo ID fornecido com novas informações.
Atualização Parcial dos Dados do Usuário:

Endpoint: /api/alterar/<int:id> (PATCH)
Descrição: Permite a atualização de campos específicos (nome, idade ou gênero) para um usuário identificado pelo ID fornecido.
Excluir Dados do Usuário:

Endpoint: /api/excluir/<int:id> (DELETE)
Descrição: Exclui os dados do usuário associados ao ID fornecido.
Configuração do Banco de Dados:


Nome: Obrigatório, 3 a 50 caracteres, alfabético.

Idade: Obrigatória, número inteiro positivo.

Gênero: Obrigatório, 'M' (masculino) ou 'F' (feminino).

A API utiliza Flask como framework web, MySQL para armazenamento de dados e incorpora suporte para CORS. Ela fornece pontos de acesso para operações CRUD, garantindo o manuseio seguro dos dados e seguindo as regras de validação especificadas.





