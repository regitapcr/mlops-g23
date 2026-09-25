
# MLOps Project - G23

## Deskripsi

Repository ini merupakan project pengembangan sistem berbasis Machine Learning dengan menerapkan konsep MLOps. Project disusun untuk mengintegrasikan proses pengolahan data, pengembangan dan pelatihan model, backend, serta frontend dalam satu repository yang terstruktur.

Penerapan struktur MLOps pada project ini bertujuan agar proses pengembangan model dapat dilakukan secara lebih terorganisir, mudah diuji, dapat direproduksi, serta mendukung kolaborasi antaranggota tim. Selain itu, pemisahan setiap komponen project mempermudah proses pengembangan, pemeliharaan, dan deployment sistem di tahap selanjutnya.

## Struktur Project

mlops-g23/
│
├── frontend/          # Komponen antarmuka pengguna
├── backend/           # API dan logika utama aplikasi
├── model/             # Pengembangan dan pengelolaan model Machine Learning
├── data/
│   ├── raw/           # Data mentah
│   └── processed/     # Data yang telah melalui preprocessing
├── tests/             # Pengujian sistem dan model
├── docs/              # Dokumentasi project
├── .gitignore         # Daftar file/folder yang tidak disimpan ke Git
├── LICENSE            # Informasi lisensi project
├── requirements.txt   # Daftar dependency Python
└── README.md          # Dokumentasi utama repository
