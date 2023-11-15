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