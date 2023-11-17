""" def alterar_cadastro_existente(id):
       if request.is_json:
        data = request.get_json()
        nome = data.get("nome")
        idade = data.get("idade")
        sexo = data.get("sexo")

        if "nome" in data and data["nome"]:
         validar_nome(data)
         query_update = "UPDATE pessoas SET nome = %s WHERE id = %s"                                             
         values_update = (nome, id)
         execute_query(query_update, values_update)
         return jsonify({"mensagem": "Nome atualizado com sucesso!"}), 200
        
         if "idade" in data and data["idade"]:
          validar_idade(data)
          query_update = "UPDATE pessoas SET idade = %s WHERE id = %s"                                             
          values_update = (idade, id)
          execute_query(query_update, values_update)
          return jsonify({"mensagem": "Idade atualizada com sucesso!"}), 200
         
         if "sexo" in data and data["sexo"]:
          validar_sexo(data)
          query_update = "UPDATE pessoas SET sexo = %s WHERE id = %s"                                             
          values_update = (sexo, id)
          execute_query(query_update, values_update)
          return jsonify({"mensagem": "Sexo atualizado com sucesso!"}), 200
         

        if "idade" in data and data["idade"]:
         validar_idade(data)
         query_update = "UPDATE pessoas SET idade = %s WHERE id = %s"                                             
         values_update = (idade, id)
         execute_query(query_update, values_update)
         return jsonify({"mensagem": "Idade atualizada com sucesso!"}), 200
         
         if "nome" in data and data["nome"]:
          validar_nome(data)
          query_update = "UPDATE pessoas SET nome = %s WHERE id = %s"                                             
          values_update = (nome, id)
          execute_query(query_update, values_update)
          return jsonify({"mensagem": "Nome atualizado com sucesso!"}), 200
          
         if "sexo" in data and data["sexo"]:
          validar_sexo(data)
          query_update = "UPDATE pessoas SET sexo = %s WHERE id = %s"                                             
          values_update = (sexo, id)
          execute_query(query_update, values_update)
          return jsonify({"mensagem": "Sexo atualizado com sucesso!"}), 200


        if "sexo" in data and data["sexo"]:
         validar_sexo(data)
         query_update = "UPDATE pessoas SET sexo = %s WHERE id = %s"                                             
         values_update = (sexo, id)
         execute_query(query_update, values_update)
         return jsonify({"mensagem": "Sexo atualizado com sucesso!"}), 200
        
         if "nome" in data and data["nome"]:
          validar_nome(data)
          query_update = "UPDATE pessoas SET nome = %s WHERE id = %s"                                             
          values_update = (nome, id)
          execute_query(query_update, values_update)
          return jsonify({"mensagem": "Nome atualizado com sucesso!"}), 200
        
         if "idade" in data and data["idade"]:
          validar_idade(data)
          query_update = "UPDATE pessoas SET idade = %s WHERE id = %s"                                             
          values_update = (idade, id)
          execute_query(query_update, values_update)
          return jsonify({"mensagem": "Idade atualizada com sucesso!"}), 200
         
    else:
        return jsonify({"erro": "A solicitação deve conter dados JSON"}), 400 """

















if request.is_json:
        data = request.get_json()
        is_valid, error_message = validar_dados(data)

        if not is_valid:
            return jsonify({"erro": error_message}), 400
        

# Verificar duplicatas
        query_duplicate_check = "SELECT id FROM pessoas WHERE nome = %s"
        duplicate_check_result = execute_query(query_duplicate_check, (nome,))
        if duplicate_check_result:
            return jsonify({"erro": "Já existe um registro com o mesmo nome"}), 409
else:
        return jsonify({"erro": "A solicitação deve conter dados JSON"}), 400  