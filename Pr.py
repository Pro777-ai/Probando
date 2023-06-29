# Probando
pm = {"LOL": "una respuesta a algo gracioso",
      "CRINGE": "algo raro o embarazoso",
      "ROFL": "una respuesta a una broma",
      "SHEESH": "ligera desaprobación",
      "CREEPY": "aterrador, siniestro",
      "AGGRO": "ponerse agresivo/enojado"}

word = input("Escribe la palabra que no entiendas: ")

if word in pm:
    print(pm[word])
else:
    print("Esa palabra no está en este programa")
