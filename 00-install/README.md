# Instalasi Spark

## Docker on Windows

Pastikan WSL & Docker Desktop sudah terinstall bila menggunakan Windows.

```{sh}
C:\> docker pull ryht/spark-notebook
```

Silakan unduh [berkas zip](https://github.com/yht/spark-learning/archive/refs/heads/main.zip) proyek ini. Lalu unzip/extract di folder Downloads folder user Anda.

```
C:\> docker run --rm -p 4040:4040 -p 8888:8888 -p 8080:8080 -v C:\Users\user\Downloads\spark-learning-main:/home/jovyan/work -e GRANT_SUDO=yes --user root ryht/spark-notebook
```

Pastikan folder user disesuaikan dengan folder login user Anda.

Berikut layanan yang bisa diakses:
* Jupyter Notebook: [http://localhost:8888](http://localhost:8888).
* Spark Console: [http://localhost:4040](http://localhost:4040).
* Testing API: [http://localhost:8080](http://localhost:8080) (default: unreachable).


