import sqlite3


class Jlite(object):
    """Classe de integração entre JSON e Sqlite.
    Args:
    ----------
    path(object): Caminho e nome do BD.

    Attributes:
    ----------
    self.conn(sqlite3.Connection): Conexão com o banco de dados.
    self.cursor(sqlite3.Cursor): Cursor do banco de dados.
    """

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, table_config):
        """Cria uma tabela no banco de dados.
        Args:
        ----------
        table_name(str): Nome da tabela.
        table_config(dict): Nomes e parametros que configuram as colunas.
        """

        end_of_the_string = ',\n' + ' ' * 12
        columns_and_parameters = ''

        for key_value in table_config.items():
            columns_and_parameters += ' '.join(key_value) + end_of_the_string

        columns_and_parameters = columns_and_parameters.rstrip(
            end_of_the_string
        )

        commands = f'''CREATE TABLE {table_name} (
            {columns_and_parameters}
            );'''

        self.cursor.execute(commands)

    def close_database_connection(self):
        self.conn.close()
