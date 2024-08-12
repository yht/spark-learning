#!/bin/bash
docker run --rm -p 4040:4040 -p 8888:8888 -p 8080:8080 \
  -v .:/home/jovyan/work -e GRANT_SUDO=yes --user root \
  -e JUPYTER_TOKEN="password" ryht/spark-notebook
