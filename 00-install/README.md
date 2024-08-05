# Instalasi Spark

## Docker on Windows

Pastikan WSL & Docker Desktop sudah terinstall bila menggunakan Windows.

```{sh}
C:\> docker pull quay.io/jupyter/all-spark-notebook
C:\> docker run --rm -p 4040:4040 -p 8888:8888 -p 8080:8080 -v C:\Users\user\Downloads\spark-learning:/home/jovyan/work -e GRANT_SUDO=yes --user root quay.io/jupyter/all-spark-notebook
```

Berikut layanan yang bisa diakses:
* Jupyter Notebook: [http://localhost:8888](http://localhost:8888).
* Spark Console: [http://localhost:4040](http://localhost:4040).
* Testing API: [http://localhost:8080](http://localhost:8080) (default: unreachable).


