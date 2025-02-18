# 📈 API de Gestão de Investimentos 💰
Uma API RESTful desenvolvida com Django e Django REST Framework para gerenciar moedas e investidores.

## 🚀 Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL 16

## ⚙ Instalação e Execução

1️⃣ Clone este repositório

```
git clone https://github.com/A-juli07/Giro-Teste_Pratico.git
cd Giro-Teste_Pratico
```

2️⃣ Crie um ambiente virtual e instale as dependências

No Windows:
```
python -m venv venv
venv\Scripts\activate
```

No Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
```

Instalando dependências:
```
pip install -r requirements.txt
```
3️⃣ Configure o banco de dados no settings.py

No caminho \Giro_Teste-Pratico\api_investimentos\api_investimentos\settings.py existe a especificação de DATABASES, verifique se está tudo corretamente configurado para o seu postgresql.


4️⃣ Inicie o postgresql na máquina (certifique que a porta esta correspondente a do settings do app) e aplique as migrações

Iniciando o servidor:
```
"C:\Program Files\PostgreSQL\16\bin\pg_ctl.exe" start -D "C:\Program Files\PostgreSQL\16\data"
```

Aplicando migrações:
No caminho \Giro_Teste-Pratico\api_investimentos, rode o comando abaixo.

```
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Inicie o servidor

```
python manage.py runserver
```

## 🧪 Executando os Testes

O projeto inclui testes unitários e de API. Entre no caminho \Giro_Teste-Pratico\api_investimentos e para rodar todos os testes:

```
python manage.py test
```
Se quiser rodar apenas um teste específico, use:

```
python manage.py test investimentos.tests.NomeDaClasseDeTeste
```

Ou um método de teste específico dentro da classe:

```
python manage.py test investimentos.tests.NomeDaClasseDeTeste.test_nome_do_metodo
```
