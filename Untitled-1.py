
#Añadir más palabras 
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
print("Hola! Soy una aplicación para definir palabras muy XD")
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

#Donde nosotros vamos a validar si la palabra está en el dictionario 
if word in meme_dict.keys():
    print(word, ":" ,meme_dict[word])
else:
    print('Lo siento, esta palabra no está en el dictionario')
