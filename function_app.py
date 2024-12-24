import re
import json
import azure.functions as func

def validate_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se tem 11 dígitos e não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            return False
    return True

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        cpf = req.params.get('cpf') or req.get_json().get('cpf')
        if not cpf:
            return func.HttpResponse(
                json.dumps({"error": "CPF not provided"}),
                status_code=400,
                mimetype="application/json"
            )

        is_valid = validate_cpf(cpf)
        return func.HttpResponse(
            json.dumps({"cpf": cpf, "is_valid": is_valid}),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
