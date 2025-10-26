import firebase_admin

from firebase_admin import credentials, db

cred = credentials.Certificate('ruta/credenciales.json')

firebase_admin.initialize_app(cred, {'databaseURL':
'https://poryecto1-27113-default-rtdb.firebaseio.com/'})