from utils import config


class SplashScreen:

    def __init__(self):
        # Nomes dos criadores (mesmo grupo da C2)
        self.created_by0 = "Bruno Mauro Bayer Laiber"
        self.created_by1 = "Daniel Lima Del'Antonio"
        self.created_by2 = "Gabriel Antônio Galdino dos Santos"
        self.created_by3 = "Issacar Mattos Gutler"
        self.created_by4 = "Kaike Vaccari do Nascimento"
        self.created_by5 = "Werney Ferreira Rocha"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2026/2"

    def get_documents_count(self, collection_name: str) -> int:
        # Retorna o total de documentos computado pela query no MongoDB
        df = config.query_count(collection_name=collection_name)
        return int(df[f"total_{collection_name}"].values[0])

    def get_updated_screen(self) -> str:
        return f"""
        ################################################################################
        #               SISTEMA DE CONTROLE DE HORAS COMPLEMENTARES
        #
        # TOTAL DE DOCUMENTOS EXISTENTES:
        #     1 - CURSOS:                   {str(self.get_documents_count("cursos")).rjust(5)}
        #     2 - ALUNOS:                   {str(self.get_documents_count("alunos")).rjust(5)}
        #     3 - CATEGORIAS DE ATIVIDADE:  {str(self.get_documents_count("categorias_atividade")).rjust(5)}
        #     4 - ADMINISTRADORES:          {str(self.get_documents_count("administradores")).rjust(5)}
        #     5 - TICKETS DE ATIVIDADES:    {str(self.get_documents_count("tickets_atividades")).rjust(5)}
        #
        # CRIADO POR: {self.created_by0}
        #             {self.created_by1}
        #             {self.created_by2}
        #             {self.created_by3}
        #             {self.created_by4}
        #             {self.created_by5}
        #
        # PROFESSOR:  {self.professor}
        #
        # DISCIPLINA: {self.disciplina}
        #             {self.semestre}
        ################################################################################
        """
