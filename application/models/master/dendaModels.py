from settings.queryFile import QueryStringDb


def getDenda():
    customQuery = QueryStringDb()
    query = '''         
            SELECT 
                id, lamapengembalian, activate, to_char(besardenda, 'FM999G999G999G999G999D99') as besardenda
            FROM denda d 
            ORDER BY id DESC;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def getDendaActivate():
    customQuery = QueryStringDb()
    query = '''         
        select 
            count(*) from denda d
        where
            activate = true 
            '''
    kondisi = {
    }
    return customQuery.select(query, kondisi)


def insertDenda(lamapengembalian, besardenda):
    customQuery = QueryStringDb()
    query = '''         
            INSERT INTO denda 
                (lamapengembalian, besardenda)
            VALUES 
                (%(lamapengembalian)s, %(besardenda)s);
            '''
    kondisi = {
        "lamapengembalian" : lamapengembalian,
        "besardenda" : besardenda,
    }
    return customQuery.execute(query, kondisi)
