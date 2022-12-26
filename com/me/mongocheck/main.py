from pymongo import MongoClient

def main():
    # There are many ways to create client instance
    m_client = MongoClient("localhost:27017")

    # Create new database with name i_db
    i_db = m_client.i_db

    # Create collection named i_collection. Equivalent of table in RDBMS
    i_collection = i_db.i_collection

    # Insert a jSON / Dict to collection
    reminder_doc = {"title": "I Remind", "message": "I am in Docker"}
    i_collection.insert_one(reminder_doc)
    i_collection


if __name__ == "__main__":
    main()