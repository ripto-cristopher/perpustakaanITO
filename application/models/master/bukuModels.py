from settings.queryFile import QueryStringDb


def getAllBuku():
    customQuery = QueryStringDb()
    query = '''         
            select 
                b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit, (select count(*)  from subbuku s where idbuku = b.id) as jumlahBuku
            from 
                buku b
            left join penerbit p
                on b.idpenerbit  = p.id
            left join pengarang p2  
                on b.idpengarang = p2.id
            left join kategori k    
                on b.idkategori = k.id ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)



def insertBuku(idpenerbit, idpengarang, idkategori, nama, tahunterbit):
    customQuery = QueryStringDb()
    query = '''         
        insert into buku (idpenerbit, idpengarang,idkategori,nama, tahunterbit)
        values (%(idpenerbit)s, %(idpengarang)s, %(idkategori)s, %(nama)s, %(tahunterbit)s)
            '''
    kondisi = {
        'idpenerbit': idpenerbit,
        'idpengarang': idpengarang,
        'idkategori': idkategori,
        'nama': nama,
        'tahunterbit': tahunterbit,

    }
    return customQuery.execute(query, kondisi)


def updateBuku(id, idpenerbit, idpengarang, idkategori, nama, tahunterbit):
    customQuery = QueryStringDb()
    query = '''         
        update buku set 
            idpenerbit = %(idpenerbit)s, 
            idpengarang = %(idpengarang)s,
            idkategori = %(idkategori)s,
            nama =  %(nama)s, 
            tahunterbit = %(tahunterbit)s
        where id = %(id)s
            '''
    kondisi = {
        'id': id,
        'idpenerbit': idpenerbit,
        'idpengarang': idpengarang,
        'idkategori': idkategori,
        'nama': nama,
        'tahunterbit': tahunterbit
    }
    return customQuery.execute(query, kondisi)


def getAllsubBuku(id):
    customQuery = QueryStringDb()
    query = '''         
        select 
            s.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama as namaBuku, tahunterbit  
        from 
            subbuku s
        left join buku b
            on s.idBuku = b.id
        left join penerbit p
            on b.idpenerbit  = p.id
        left join pengarang p2  
            on b.idpengarang = p2.id
        left join kategori k    
            on b.idkategori = k.id
        where b.id = %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)


def insertSubBuku(idBuku):
    customQuery = QueryStringDb()
    query = '''         
        insert into subBuku
            (idbuku, tanggalmasuk)
        values
            (%(idBuku)s, CURRENT_DATE) 
        RETURNING id;
            '''
    kondisi = {
        'idBuku': idBuku
    }
    return customQuery.execute_select(query, kondisi)


def getBuku(id):
    customQuery = QueryStringDb()
    query = '''         
            select 
                b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit  
            from 
                buku b
            left join penerbit p
                on b.idpenerbit  = p.id
            left join pengarang p2  
                on b.idpengarang = p2.id
            left join kategori k    
                on b.idkategori = k.id 
            where b.id = %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)
