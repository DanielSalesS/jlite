from unittest import TestCase, main
import sqlite3
import os
from jlite import Jlite


class TestCreateTable(TestCase):
    def setUp(self):
        self.path = r'tests/db/test_create_table.db'
        self.jlite = Jlite(path=self.path)
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()

    def test_table_with_correct_name(self):

        table_name = 'teste1'
        columns_and_parameters = {
            'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'idade': 'INTEGER',
            'cpf': ' VARCHAR(11) NOT NULL',
            'criado_em': 'DATE NOT NULL',
        }

        input_arguments = {
            'table_name': table_name,
            'table_config': columns_and_parameters,
        }

        self.jlite.create_table(**input_arguments)

        self.cursor.execute(
            f"""SELECT name
            FROM sqlite_master
            WHERE type='table' AND name='{table_name}';"""
        )

        expected = table_name
        result = self.cursor.fetchone()[0]
        self.assertEqual(expected, result)

    def test_columns_with_correct_name(self):
        table_name = 'teste2'
        columns_and_parameters = {
            'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
            'nome': 'TEXT NOT NULL',
            'posicao': 'INTEGER',
            'reg': ' VARCHAR(6) NOT NULL',
            'criado_em': 'DATE NOT NULL',
        }

        input_arguments = {
            'table_name': table_name,
            'table_config': columns_and_parameters,
        }
        self.jlite.create_table(**input_arguments)

        self.cursor.execute(f"""PRAGMA table_info({table_name});""")

        expected = sorted(columns_and_parameters.keys())
        result = sorted(row[1] for row in self.cursor.fetchall())
        self.assertEqual(expected, result)

    def tearDown(self):
        self.conn.close()
        self.jlite.close_database_connection()
        os.remove(self.path)


if __name__ == '__main__':
    main()
