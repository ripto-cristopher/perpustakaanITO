from settings.queryFile import QueryStringDb


def selectAdmins():
    customQuery = QueryStringDb()
    query = '''         
            select 
                id, password 
            from 
                admin 
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def selectAdmin(id):
    customQuery = QueryStringDb()
    query = '''         
            select 
                id, password 
            from 
                admin 
            where 
                id = %(id)s
            '''
    kondisi = {
        'id': id

    }
    return customQuery.select(query, kondisi)


def insertAdmin(id, nama, passwordHash):
    customQuery = QueryStringDb()
    query = '''
        insert into 
            admin (id, nama, password) 
        values 
            (%(id)s, %(nama)s, %(passwordhash)s)
            '''
    kondisi = {
        'id': id,
        'nama': nama,
        'passwordhash': passwordHash
    }
    return customQuery.execute(query, kondisi)


def selectUsers():
    customQuery = QueryStringDb()
    query = '''         
            select 
                id, password 
            from 
                anggotaperpustakaan 
            where
                status = 'aktif'
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def selectUser(id):
    customQuery = QueryStringDb()
    query = '''         
            select 
                id, password, email
            from 
                anggotaperpustakaan
            where 
                id = %(id)s 
                and status = %(aktif)s
            '''
    kondisi = {
        'id': id,
        'aktif': 'aktif'
    }
    return customQuery.select(query, kondisi)

def insertUser(id, nama,email ,tanggalLahir,kategori, passwordHash ):
    customQuery = QueryStringDb()
    query = '''
    insert into 
        anggotaperpustakaan (id, nama, email, tanggallahir, kategori, password)
        values (%(id)s , %(nama)s,%(email)s,%(tanggallahir)s,%(kategori)s, %(passwordhash)s)
            '''
    kondisi = {
        'id': id,
        'nama': nama,
        'email': email,
        'kategori': kategori,
        'tanggallahir': tanggalLahir,
        'passwordhash': passwordHash
    }

    print (query, kondisi)
    return customQuery.execute(query, kondisi)
