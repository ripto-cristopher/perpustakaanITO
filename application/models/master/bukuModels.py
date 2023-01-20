from settings.queryFile import QueryStringDb


def getAllJudulBuku():
    customQuery = QueryStringDb()
    query = '''         
            select 
                b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit, (select count(*)  from buku s where  idJudulbuku = b.id) as jumlahBuku
            from 
                judulbuku  b
            left join penerbit p
                on b.idpenerbit  = p.id
            left join pengarang p2  
                on b.idpengarang = p2.id
            left join kategori k    
                on b.idkategori = k.id ;
            '''
    kondisi = {}
    return customQuery.select(query, kondisi)


def getJudulBuku(id):
    customQuery = QueryStringDb()
    query = '''         
            select 
                b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit, (select count(*)  from buku s where  idJudulbuku = b.id) as jumlahBuku
            from 
                judulbuku  b
            left join penerbit p
                on b.idpenerbit  = p.id
            left join pengarang p2  
                on b.idpengarang = p2.id
            left join kategori k    
                on b.idkategori = k.id
            where 
                b.id = %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)


def insertJudulBuku(idpenerbit, idpengarang, idkategori, nama, tahunterbit):
    customQuery = QueryStringDb()
    query = '''         
        insert into judulbuku  (idpenerbit, idpengarang,idkategori,nama, tahunterbit)
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



# def updateBuku(id, idpenerbit, idpengarang, idkategori, nama, tahunterbit):
#     customQuery = QueryStringDb()
#     query = '''         
#         update buku set 
#             idpenerbit = %(idpenerbit)s, 
#             idpengarang = %(idpengarang)s,
#             idkategori = %(idkategori)s,
#             nama =  %(nama)s, 
#             tahunterbit = %(tahunterbit)s
#         where id = %(id)s
#             '''
#     kondisi = {
#         'id': id,
#         'idpenerbit': idpenerbit,
#         'idpengarang': idpengarang,
#         'idkategori': idkategori,
#         'nama': nama,
#         'tahunterbit': tahunterbit
#     }
#     return customQuery.execute(query, kondisi)


def getAllBukuByIdJudulBuku(id):  # perlu diedit
    customQuery = QueryStringDb()
    query = '''         
        select 
            s.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama as namaBuku, tahunterbit, s.tanggalmasuk , s.status
        from 
            buku s
        left join judulbuku b
            on s.idjudulBuku = b.id
        left join penerbit p
            on b.idpenerbit  = p.id
        left join pengarang p2  
            on b.idpengarang = p2.id
        left join kategori k    
            on b.idkategori = k.id
        where b.id =  %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)


def getAllBuku():  
    customQuery = QueryStringDb()
    query = '''         
        select 
            s.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama as namaBuku, tahunterbit 
        from 
            buku s
        left join judulbuku b
            on s.idJudulBuku = b.id
        left join penerbit p
            on b.idpenerbit  = p.id
        left join pengarang p2  
            on b.idpengarang = p2.id
        left join kategori k    
            on b.idkategori = k.id
            '''
    kondisi = {
    }
    return customQuery.select(query, kondisi)

def getBuku(id):  # perlu diedit
    customQuery = QueryStringDb()
    query = '''         
        select 
            s.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama as namaBuku, tahunterbit 
        from 
            buku s
        left join judulbuku b
            on s.idJudulBuku = b.id
        left join penerbit p
            on b.idpenerbit  = p.id
        left join pengarang p2  
            on b.idpengarang = p2.id
        left join kategori k    
            on b.idkategori = k.id
        where s.id =  %(id)s
            '''
    kondisi = {
        'id': id
    }
    return customQuery.select(query, kondisi)


def insertBuku(idBuku):
    customQuery = QueryStringDb()
    query = '''         
        insert into Buku
            (idJudulbuku, tanggalmasuk)
        values
            (%(idBuku)s, CURRENT_DATE) 
        RETURNING id;
            '''
    kondisi = {
        'idBuku': idBuku
    }
    return customQuery.execute_select(query, kondisi)


# def getBuku(id):  # perlu diedit
#     customQuery = QueryStringDb()
#     query = '''         
#         select 
#             s.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama as namaBuku, tahunterbit  
#         from 
#             subbuku s
#         left join buku b
#             on s.idBuku = b.id
#         left join penerbit p
#             on b.idpenerbit  = p.id
#         left join pengarang p2  
#             on b.idpengarang = p2.id
#         left join kategori k    
#             on b.idkategori = k.id
#         where b.id = %(id)s
#             '''
#     kondisi = {
#         'id': id
#     }
#     return customQuery.select(query, kondisi)




# def getBuku(id):
#     customQuery = QueryStringDb()
#     query = '''         
#             select 
#                 b.id, p.nama as penerbit , p2.nama as pengarang, k.nama as kategori, b.nama, tahunterbit  
#             from 
#                 buku b
#             left join penerbit p
#                 on b.idpenerbit  = p.id
#             left join pengarang p2  
#                 on b.idpengarang = p2.id
#             left join kategori k    
#                 on b.idkategori = k.id 
#             where b.id = %(id)s
#             '''
#     kondisi = {
#         'id': id
#     }
#     return customQuery.select(query, kondisi)
