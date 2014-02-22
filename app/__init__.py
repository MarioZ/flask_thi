from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'cstd'


client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
