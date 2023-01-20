-- id diambil dari nisn/nis jika siswa, NUPTK (Nomor Unik Pendidik dan Tenaga Kependidikan) jika staf atau tenaga pengajar, idanggotaperpustakaan berguna juga untuk login
-- email untuk pengiriman pemberintahuan (dibuat jika memungkinkan)
-- status = { 'aktif', 'tidak aktif'}, aktif jika anggota perpustakaan masih dalam organisasi, tidak aktif jika telah keluar dari organisasi (lulus, pindah, atau dikeluarkan)
-- kategori = { 'guru', 'siswa'}
-- password dalam bentuk hash 256 , default tanggal lahir format (yyyymmdd)

create table anggotaperpustakaan (
id int primary key not NULL,
nama VARCHAR ( 50 ) NOT NULL,
email VARCHAR ( 50 ) UNIQUE NOT NULL,
status Varchar (20)  not null DEFAULT 'aktif',
tanggallahir date not null,
kategori varchar (20) not null,
password varchar (100) NOT null 
)

create table penerbit (
id BIGSERIAL  primary key not NULL,
nama VARCHAR (50) NOT NULL
)

create table pengarang (
id BIGSERIAL  primary key not NULL,
nama VARCHAR (50) NOT NULL
)

create table kategori (
id BIGSERIAL  primary key not NULL,
nama VARCHAR (50) NOT NULL
)

create table judulBuku (
id BIGSERIAL  primary key not NULL,
idpenerbit BIGINT REFERENCES penerbit (id),
idpengarang BIGINT REFERENCES pengarang (id),
idkategori BIGINT REFERENCES kategori (id),
nama varchar (100) not null,
tahunTerbit int not null
)

-- status = {'hilang', 'rusak', 'perbaikan','tersedia'}

create table buku (
id BIGSERIAL  primary key not NULL,
idJudulBuku BIGINT REFERENCES judulBuku (id),
status Varchar (20) not null DEFAULT 'tersedia' ,
tanggalMasuk date not null
)

-- admin login dengan id dan password
-- id diambil dari no induk staf (asumsi staf semua ada no id)
-- status = { 'aktif', 'tidak aktif'}, aktif jika admin perpustakaan masih dalam organisasi, tidak aktif jika telah keluar dari organisasi


create table admin (
id int primary key not NULL,
status Varchar (20)  not null DEFAULT 'aktif',
nama Varchar (50) not null,
password varchar (100) NOT NULL 

)

create table peminjaman (
id BIGSERIAL  primary key not NULL,
idbuku BIGINT REFERENCES buku (id),
idadmin BIGINT REFERENCES admin (id),
idanggotaperpustakaan bigint REFERENCES anggotaperpustakaan (id),
tanggalpeminjaman date not null default current_date ,
bataspengembalian date not null default current_date + interval '1 day' * 7,
flag int not null default 1
)

create table pengembalian (
id BIGSERIAL primary key not NULL,
idbuku BIGINT REFERENCES Buku (id),
idadmin BIGINT REFERENCES admin (id),
tanggalpengembalian date not null default current_date,
denda int
)


-- hapus table


drop table anggotaperpustakaan 

drop table buku 

drop table judulbuku  

drop table admin 

drop table peminjaman 

drop table pengembalian 

drop table kategori 

drop table penerbit 

drop table pengarang 