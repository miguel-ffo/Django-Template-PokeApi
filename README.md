# PokeApi


<img src="img/Captura de tela 2024-08-23 212024.png" alt="Exemplo imagem">

>Consumo de api em Django que pesquisa pokemons para o desafio da fábrica de software 2024.2.


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `<Python>`
- Você tem uma máquina `<Windows / Linux / Mac>`.


## 🚀 Instalando PokeApi

Para clonar o PokeApi, siga estas etapas:

Navegue até o diretório onde deseja clonar o repositório: Use o comando cd para mudar para o diretório desejado. Por exemplo:

```
cd /caminho/para/seu/diretorio
```

Execute o comando git clone:

```
git clone https://github.com/miguel-ffo/whorkshop-fabrica-2024.2-miguel.git
```



## ☕ Usando a PokeApi

Para usar PokeApi, siga estas etapas:

Acesse o diretório do repositório clonado: Após a clonagem, você pode entrar no diretório do repositório com:

```
cd whorkshop-fabrica-2024.2-miguel
```
Crie um ambiente virtual:

O ambiente virtual isola as dependências do seu projeto. Crie e ative um ambiente virtual com o seguinte comando:

No Windows:

```
python -m venv venv
venv\Scripts\activate
```

No macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:

```
pip install -r requirements.txt
```

Configure a senha do seu root no MySQL no script_db.py :

```
root_connection = MySQLdb.connect(user='root', passwd='seu_password', host=db_host)  # Atualize com a senha do root
```
Rode o script_db.py:

```
python manage.py script_db.py
```
Aplique as migrações:

As migrações são necessárias para criar e atualizar o esquema do banco de dados. Aplique as migrações com os seguintes comandos:

```
python manage.py makemigrations
python manage.py migrate
```

Inicie o servidor de desenvolvimento:

Finalmente, inicie o servidor de desenvolvimento do Django para rodar o projeto:
 
 ```
python manage.py runserver
```

O servidor começará a rodar, e você deverá ver uma saída no terminal indicando que o servidor está ativo, geralmente ouvindo na porta 8000 por padrão (http://127.0.0.1:8000/).






## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://avatars.githubusercontent.com/u/142344702?v=4"width="100px;" alt="Foto do Miguel Figueiredo no GitHub"/><br>
        <sub>
          <b>Miguel Figueiredo </b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://s2.glbimg.com/FUcw2usZfSTL6yCCGj3L3v3SpJ8=/smart/e.glbimg.com/og/ed/f/original/2019/04/25/zuckerberg_podcast.jpg" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Mark Zuckerberg</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o título do link">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

#