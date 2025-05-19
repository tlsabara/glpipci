
# glpipci - GLPI Python Comunicator Interface - [unofficial]


![PyPI](https://img.shields.io/pypi/v/pyglpi) ![Python Version](https://img.shields.io/pypi/pyversions/pyglpi) ![License](https://img.shields.io/pypi/l/pyglpi) ![Beta](https://img.shields.io/badge/status-beta-yellow)

Um cliente Python para a API do GLPI.

## Instalação

Para instalar o pacote, use o seguinte comando:

```bash
pip install glpipci
```

## Uso

Exemplo de como usar o pacote

```python
from glpipci.comunicator.v10_0.api import GLPIApiClient

client = GLPIApiClient(username="admin", password="password")
response = client.make_get("http://localhost:8090/apirest.php/some_endpoint")
print(response.json())
```

## Contribuição
Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-branch`).
3. Faça suas alterações e commit (`git commit -m 'Add some feature'`).
4. Envie para o repositório remoto (`git push origin feature-branch`).
5. Crie um novo Pull Request.
6. Aguarde a revisão e feedback.


## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
