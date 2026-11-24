import os
from urllib.parse import quote_plus
import pymongo
from pymongo.errors import OperationFailure


class MongoQueries:
    """Camada de conexão com o MongoDB (baseada no example_crud_mongo do Prof. Howard Roatti).

    Responsável (Membro 1 - Kaike):
    - Manter a conexão com o database ``labdatabase`` na porta ``27017``.
    - Suportar tanto o MongoDB sem autenticação (container padrão do Docker / VM LabDatabase)
      quanto o MongoDB autenticado via ``authentication.mongo`` ou variáveis de ambiente.
    """

    def __init__(self):
        self.host = os.getenv("MONGO_HOST", "localhost")
        self.port = int(os.getenv("MONGO_PORT", "27017"))
        self.service_name = os.getenv("MONGO_DB", "labdatabase")
        self.user = os.getenv("MONGO_USER")
        self.passwd = os.getenv("MONGO_PASSWORD")

        auth_file = os.path.join(
            os.path.dirname(__file__), "passphrase", "authentication.mongo"
        )
        if not self.user and os.path.exists(auth_file):
            with open(auth_file, "r", encoding="utf-8") as f:
                conteudo = f.read().strip()
                if "," in conteudo:
                    self.user, self.passwd = [parte.strip() for parte in conteudo.split(",", 1)]

    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        # Usa URI com credenciais apenas quando MONGO_USE_AUTH=1 ou quando o servidor exigir
        use_auth = os.getenv("MONGO_USE_AUTH", "0").strip() in {"1", "true", "TRUE"}
        if use_auth and self.user and self.passwd:
            uri = f"mongodb://{quote_plus(self.user)}:{quote_plus(self.passwd)}@{self.host}:{self.port}/"
        else:
            uri = f"mongodb://{self.host}:{self.port}/"

        self.mongo_client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
        self.db = self.mongo_client[self.service_name]

        # Caso o servidor exija autenticação e MONGO_USE_AUTH não tenha sido definido,
        # reconecta automaticamente utilizando o arquivo authentication.mongo:
        if not use_auth and self.user and self.passwd:
            try:
                self.db.list_collection_names()
            except OperationFailure:
                self.mongo_client.close()
                uri_auth = (
                    f"mongodb://{quote_plus(self.user)}:{quote_plus(self.passwd)}"
                    f"@{self.host}:{self.port}/"
                )
                self.mongo_client = pymongo.MongoClient(uri_auth, serverSelectionTimeoutMS=5000)
                self.db = self.mongo_client[self.service_name]

    def close(self):
        if hasattr(self, "mongo_client"):
            self.mongo_client.close()
