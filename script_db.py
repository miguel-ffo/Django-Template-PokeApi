import os
import django
import MySQLdb
from django.conf import settings
from django.core.management import call_command

# Configure o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projeto.settings')  # Substitua 'seu_projeto' pelo nome do seu projeto

# Inicializa as configurações do Django
django.setup()

def create_database():
    db_name = settings.DATABASES['default']['NAME']
    db_user = settings.DATABASES['default']['USER']
    db_password = settings.DATABASES['default']['PASSWORD']
    db_host = settings.DATABASES['default']['HOST']

    try:
        # Conectando ao servidor MySQL como root
        root_connection = MySQLdb.connect(user='seu_user', passwd='seu_password', host=db_host)  # Atualize com a senha do root
        cursor = root_connection.cursor()

        # Criando o banco de dados
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        
        # Criando o usuário Pokemon com a senha pokemon
        cursor.execute("CREATE USER IF NOT EXISTS 'Pokemon'@'localhost' IDENTIFIED BY 'pokemon';")
        
        # Garantindo todas as permissões para o usuário no banco de dados criado
        cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO 'Pokemon'@'localhost';")
        cursor.execute("FLUSH PRIVILEGES;")  # Aplica as mudanças

        root_connection.commit()
        cursor.close()
        root_connection.close()

        print(f"Banco de dados '{db_name}' criado com sucesso e usuário 'Pokemon' configurado.")
    
    except MySQLdb.OperationalError as e:
        print(f"Erro ao conectar ao MySQL: {e}")

def migrate():
    # Executa as migrações do Django
    call_command('migrate')

if __name__ == "__main__":
    create_database()
    migrate()
