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

Je sais pas faire du Python, j'ai pas réussi à démarrer une app Python.
Et en plus, Docker ne voulait pas écraser /app/app.py.

### 3. Variables d'environnement

```bash
curl http://127.0.0.1:8000
{"message":"Available routes","routes":{"get_user_by_id":"http://127.0.0.1:8000/user/1","list_all_users":"http://127.0.0.1:8000/users"}}
```