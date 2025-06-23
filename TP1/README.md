# Part 1 : Init

## II. Un premier conteneur en vif

### 1. Simple run

```bash
docker run -d -p 8000:8000 it4lik/meow-api
1ace1ae98856499e2f4e786d48c315c03119812da46f49e12e457e81fab95b6d
```

Vérifier les conteneurs en cours :
```bash
docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                    NAMES
1ace1ae98856   it4lik/meow-api   "python3 -m http.ser…"   42 seconds ago   Up 40 seconds   0.0.0.0:8000->8000/tcp   nice_swartz
```

Afficher les logs du conteneur :
```bash
docker logs 1ace1ae98856
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://172.17.0.2:8000
Press CTRL+C to quit
```

### 2. Volumes

```bash
docker run -v "C:\Users\___\Documents\B3_Dev_and_Data\Semestre_6\Docker_avance\TP\TP1\Part1\app.py:/app/app.py" -p 8000:8000 it4lik/meow-api
```

```bash
curl localhost:8000

            <html><body>
            <h1>Meow! Voici un GIF de chat nul 🐱</h1>
            <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" alt="Chat gif">
            </body></html>
```

### 3. Variables d'environnement

```bash
curl http://127.0.0.1:8000
{"message":"Available routes","routes":{"get_user_by_id":"http://127.0.0.1:8000/user/1","list_all_users":"http://127.0.0.1:8000/users"}}
```

# Part 2 : Images

## I. Images publiques

```bash
docker pull python:3.11
docker pull mysql:5.7
docker pull wordpress
docker pull linuxserver/wikijs
```

Lister les images que j'ai sur ma machine : 
```bash
docker images
```

## II. Construire une image

### A. Build la meow-api

```bash
docker run -p 8000:8000 meow-api
```

### B. Packagez vous-même une app

```bash
docker run -p 8000:8000 python_app:version_de_ouf
Cet exemple d'application est vraiment naze 👎
```

### C. Ecrire votre propre Dockerfile

Image déployée : https://hub.docker.com/repository/docker/clairesbaffe/airport_app/general

# Part 3 : Compose

## I. Getting started

### 1. Run it

```bash
docker compose ps
time="2025-06-23T11:38:47+02:00" level=warning msg="C:\\Users\\___\\Documents\\B3_Dev_and_Data\\Semestre_6\\Docker_avance\\TP\\TP1\\Part3\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
NAME                          IMAGE     COMMAND        SERVICE               CREATED          STATUS          PORTS
part3-conteneur_flopesque-1   debian    "sleep 9999"   conteneur_flopesque   42 seconds ago   Up 41 seconds
part3-conteneur_nul-1         debian    "sleep 9999"   conteneur_nul         42 seconds ago   Up 41 seconds
```

## II. A working meow-api

```bash
curl localhost:8000/users
[{"favorite_insult":"Tu as le charisme d\u00e2\u20ac\u2122un slip humide.","id":1,"name":"Alice"},{"favorite_insult":"T\u00e2\u20ac\u2122es pas b\u00c3\u00aate, t\u00e2\u20ac\u2122es... tr\u00c3\u00a8s conceptuel.","id":2,"name":"Bob"},{"favorite_insult":"Si la b\u00c3\u00aatise \u00c3\u00a9tait un sport, tu serais m\u00c3\u00a9daill\u00c3\u00a9.","id":3,"name":"Charlie"},{"favorite_insult":"M\u00c3\u00aame Google ne te trouve pas int\u00c3\u00a9ressant.","id":4,"name":"Diana"}]
```

```bash
curl localhost:8000/user/3
{"favorite_insult":"Si la b\u00c3\u00aatise \u00c3\u00a9tait un sport, tu serais m\u00c3\u00a9daill\u00c3\u00a9.","id":3,"name":"Charlie"}
```