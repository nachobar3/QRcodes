
import pymongo

def init_mongo():
    client = pymongo.MongoClient("mongodb+srv://ibarbero:muvinai@cluster0.sf15y.mongodb.net/sportclub_prod", tlsAllowInvalidCertificates=True)
    db = client.sportclub_prod
    return db


def init_mongo_test():
    client = pymongo.MongoClient("mongodb+srv://ibarbero:muvinai@cluster0.sf15y.mongodb.net/checkout", tlsAllowInvalidCertificates=True)
    db = client.checkout
    return db
