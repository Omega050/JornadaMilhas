# JornadaMilhas

## Descrição
JornadaMilhas é uma API desenvolvida com Django REST Framework como parte do desafio Back-End 7 da Alura. O projeto tem como objetivo facilitar a gestão de viagens, permitindo o cadastro e a consulta de destinos turísticos.

## Tecnologias Utilizadas
- Python 3.12.4
- Django 5.1.6
- Django REST Framework

## Configuração do Ambiente
### Clonando o repositório
```sh
 git clone https://github.com/Omega050/JornadaMilhas.git
 cd JornadaMilhas
```

### Criando e ativando um ambiente virtual
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### Instalando dependências
```sh
pip install -r requirements.txt
```

### Configurando o banco de dados
1. Configure as variáveis de ambiente no arquivo `.env` (se necessário).
2. Aplique as migrações:
   ```sh
   python manage.py migrate
   ```

### Executando o servidor localmente
```sh
python manage.py runserver
```

## Endpoints Principais
A API expõe os seguintes endpoints:
- `GET /destinos/` - Lista todos os destinos
- `POST /destinos/` - Cria um novo destino
- `GET /destinos/{id}/` - Obtém detalhes de um destino específico
- `PUT /destinos/{id}/` - Atualiza um destino
- `DELETE /destinos/{id}/` - Remove um destino

## Testes
Para rodar os testes automatizados:
```sh
python manage.py test
```

## Contribuição
1. Fork este repositório.
2. Crie um branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas modificações (`git commit -m 'Adiciona nova feature'`).
4. Envie para o repositório (`git push origin minha-feature`).
5. Abra um Pull Request.

## Licença
Este projeto está sob a licença MIT. Para mais informações, consulte o arquivo `LICENSE`.

