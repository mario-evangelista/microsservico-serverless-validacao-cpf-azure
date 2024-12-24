# Microsserviço Serverless para Validação de CPF

Este projeto implementa um microsserviço serverless na **Azure Functions** para validar CPFs brasileiros. Ele recebe um CPF via requisição HTTP e retorna um JSON indicando se o CPF é válido ou não.

## 🚀 Funcionalidades

- Validação de formato do CPF.
- Verificação do dígito verificador.
- Resposta em formato JSON.

## 🛠️ Tecnologias Utilizadas

- [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/)
- Python 3.x
- Azure CLI
- Azure Functions Core Tools

## 📂 Estrutura do Projeto

```plaintext
microsservico-serverless-validacao-cpf-azure/
├── ValidateCPF/
│   ├── function_app.py          # Lógica principal da função
├── host.json                # Configuração global da Azure Function
├── local.settings.json      # Configurações locais (não incluir no controle de versão)
└── requirements.txt         # Dependências do projeto
```

## 🧑‍💻 Como Executar Localmente

### Pré-requisitos

- Python 3.x instalado
- Azure Functions Core Tools instalado
- Azure CLI instalado

### Passos

1. Clone este repositório:
   ```bash
   git clone https://github.com/mario-evangelista/microsservico-serverless-validacao-cpf-azure.git
   cd microsservico-serverless-validacao-cpf-azure
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor local:
   ```bash
   func start
   ```

4. Faça uma requisição HTTP:
   ```bash
   curl -X POST http://localhost:7071/api/ValidateCPF -H "Content-Type: application/json" -d '{"cpf": "12345678909"}'
   ```

## 🌐 Implantação no Azure

1. Faça login no Azure:
   ```bash
   az login
   ```

2. Crie o ambiente no Azure:
   ```bash
   az group create --name CPFValidatorResourceGroup --location eastus
   az functionapp create --resource-group CPFValidatorResourceGroup --consumption-plan-location eastus --runtime python --functions-version 4 --name CPFValidatorApp --storage-account <STORAGE_ACCOUNT_NAME>
   ```

3. Implante o código:
   ```bash
   func azure functionapp publish CPFValidatorApp
   ```

4. Use a URL gerada para fazer requisições.

## 📄 Exemplo de Resposta

### Requisição

```json
{
  "cpf": "12345678909"
}
```

### Resposta

```json
{
  "cpf": "12345678909",
  "is_valid": true
}
```

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Feito com ❤️ por [Mário Evangelista](https://github.com/mario-evangelista).**
