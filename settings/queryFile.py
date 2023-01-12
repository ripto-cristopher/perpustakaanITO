import psycopg2
from settings.credentials import *


def responseJSON(status_code, flag, message, result):
    resp = {}
    resp['status_code'] = status_code
    resp['status'] = flag
    resp['message'] = message
    resp['result'] = result
    return resp


def rows_to_dict_list(cursor):
    ''' Function return list of dictionary  '''
    columns = [i[0].lower() for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]


class QueryStringDb(object):
    def __init__(self):
        self._db_connection = psycopg2.connect(
            user=USER_POSTGRES_DB, password=PASSWORD_POSTGRES_DB, host=HOST, port=PORT, database=DATABASE)
        self._db_cursor = self._db_connection.cursor()

    def __del__(self):
        self._db_cursor.close()
        self._db_connection.close()

    def select(self, p_query, p_param):
        try:
            self._sqlQuery = p_query
            self._v_kondisi = p_param
            self._db_cursor.execute(self._sqlQuery, self._v_kondisi)
            self._result = rows_to_dict_list(self._db_cursor)
            return responseJSON(200, "T", "Sukses", self._result)
        except Exception as error:
            return responseJSON(200, "F", str(error), [])

    def execute(self, p_query, p_param):
        try:
            self._sqlQuery = p_query
            self._v_kondisi = p_param
            self._db_cursor.execute(self._sqlQuery, self._v_kondisi)
            self._db_connection.commit()
            return responseJSON(200, "T", "Method Execute Berhasil Dijalankan!", None)
        except psycopg2.Error as error:
            v_msg_error = 'error select : {error_code}, {error}'.format(
                error_code=error.pgcode, error=str(error.pgerror))
            return responseJSON(error.pgcode, "F", f"Kode: {error.pgcode}. {error.pgerror}", [])

    def execute_select(self, query, kondisi):
        try:
            self.query = query
            self.kondisi = kondisi
            self._db_cursor.execute(self.query, self.kondisi)
            self._db_connection.commit()
            self._result = rows_to_dict_list(self._db_cursor)
            return responseJSON(200, "T", "Execute Select Berhasil!", self._result)
        except psycopg2.Error as e:
            return responseJSON(200, 'F', f"Kode: {e.pgcode}, Error: {e.pgerror}", None)
