from pymongo import MongoClient

MONGO_URI = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.2"  # Cambiar si usas MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["pruebamongo"]
