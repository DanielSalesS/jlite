from unittest import TestCase, main
import sqlite3
import os
from jlite import Jlite


class TestInsertSingleRecord(TestCase):
    def check_table_exists(self):
        self.cursor.execute(
            f"""SELECT name
            FROM sqlite_master
            WHERE type='table' AND name='{self.table_name}';"""
        )
        self.cursor.fetchone()

    def setUp(self):
        self.path = r'tests/db/test_insert_single_record.db'
        self.jlite = Jlite(path=self.path)
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        self.table_name = 'teste1'

        if self.check_table_exists():
            columns_and_parameters = {
                'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
                'nome': 'TEXT NOT NULL',
                'idade': 'INTEGER',
                'cpf': ' VARCHAR(11) NOT NULL',
                'criado_em': 'DATE NOT NULL',
            }

            input_arguments = {
                'table_name': self.table_name,
                'table_config': columns_and_parameters,
            }
            self.jlite.create_table(**input_arguments)

    def test_insert_a_single_record(self):
        _ = 1 / 0


if __name__ == '__main__':
    main()
