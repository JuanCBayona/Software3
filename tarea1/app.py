#Backend. De framework usamos Flask
from flask import Flask, jsonify, request

#Ejecutar Flask
#servidor
app = Flask(__name__)


#Llamar información de la "base de datos"
from datos import registered_users

#Ruta Get
@app.route('/greeting/<string:user_name>', methods=['GET'])
def getUser(user_name):
    found =[user for user in registered_users if user['name'] == user_name]
    #Verificar si existe el usuario
    if (len(found) > 0):
        return jsonify({"user": found, "message" : "Hola"})
    else:        
        return jsonify({"user" :user_name, "message":"no es un usuario registrado"})

#Ruta Post
@app.route('/register', methods = ['POST'])
def addUsr():
    register_user = {
        "name": request.json['name'],
        "lang": request.json['lang']
    }
    registered_users.append(register_user)
    return jsonify({"message": "El usuario ha sido registrado"})


#Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000)


#Para guardar datos, se hace uso de Insomnia