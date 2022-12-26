# ipymongodb

Get MongoDB Server setup
I choose docker way.

```console
docker pull mongo

docker run -p 27017:27017 -d mongo:latest

docker ps

docker logs mongo
```


Get mongo python client
This helps to interact with server.

```console
pip3 install pymongo
```
```python
from pymongo import MongoClient

#There are many ways to create client instance
m_client = MongoClient("localhost:27017")

#Create new database with name i_db
i_db = m_client.i_db

#Create collection named i_collection. Equivalent of table in RDBMS
i_collection = i_db.i_collection

#Insert a jSON / Dict to collection
reminder_doc = {"title" : "I Remind", "message" : "I am in Docker"}
i_collection.insert_one(reminder_doc)

```
