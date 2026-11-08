# Genera index.html (fotos en la carpeta fotos/) e index_autonomo.html (fotos incrustadas).
# Uso: python construir.py   (necesita plantilla.html y fotos_base64.json en la misma carpeta)
import json
t = open("plantilla.html", encoding="utf-8").read()
img = json.load(open("fotos_base64.json"))
M = "/*__IMG__*/{}"
rutas = {k: "fotos/" + k + ".png" for k in img}
cab = '<!doctype html>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
open("index.html", "w", encoding="utf-8").write(cab + t.replace(M, json.dumps(rutas)))
open("index_autonomo.html", "w", encoding="utf-8").write(cab + t.replace(M, json.dumps(img)))
