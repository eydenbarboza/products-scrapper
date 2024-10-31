from pymongo import MongoClient
from contextlib import contextmanager

from infrastructure.base_database import BaseDatabase



class BaseMongoDB(BaseDatabase):
    

    def __init__(self, db_url: str, db_name: str) -> None:
        self.db_url = db_url
        self.db_name = db_name
        self.client = None
        self.db = None


    def connect(self) -> None:
        """ Open connection """

        try:
            self.client = MongoClient(self.db_url)
            self.db = self.client[self.db_name]
        except Exception as e:
            print("ERROR: ", e)
        

    def disconnect(self) -> None:
        """ Close connection """
        
        if self.client:
            self.client.close()


    @contextmanager
    def get_db(self):
        """
        Context manager for obtaining a database connection.
        
        Connects to the database if not already connected, yields the database 
        object, and ensures disconnection after use.
        """

        if self.client is None:
            self.connect()
        try:
            yield self.db
        finally:
            self.disconnect()


    def get_collection(self, collection_name: str):
        """
        Retrieves a specific collection from the database.
        
        Args:
            collection_name (str): The name of the collection to retrieve.
        
        Returns:
            Collection: The specified collection object.
        """

        return self.db[collection_name]
    

    def find_all(self, collection, filter_data: dict = {}):
        """
        Finds all documents in a collection that match the filter criteria.
        
        Args:
            collection (Collection): The collection to search in.
            filter_data (dict): The filter criteria for the search.
        
        Returns:
            Cursor: A cursor to the documents that match the filter criteria.
        """

        return collection.find(filter_data)
    

    def insert(self, collection, data: dict = {}):
        """
        Inserts a single document into a collection.
        
        Args:
            collection (Collection): The collection to insert into.
            data (dict): The document to insert.
        
        Returns:
            InsertOneResult: The result of the insert operation.
        """

        return collection.insert_one(data)
    

    def insert_many(self, collection, data: dict):
        """
        Inserts multiple documents into a collection.
        
        Args:
            collection (Collection): The collection to insert into.
            data (dict): The documents to insert.
        
        Returns:
            InsertManyResult: The result of the insert operation.
        """

        return collection.insert_many(data)
    

    def update(self, collection, filter_data: dict = {}, update_data: dict = {}):
        """
        Updates a single document in a collection that matches the filter criteria.
        
        Args:
            collection (Collection): The collection to update in.
            filter_data (dict): The filter criteria for selecting the document to update.
            update_data (dict): The update operations to apply to the selected document.
        
        Returns:
            UpdateResult: The result of the update operation.
        """

        return collection.update_one(filter_data, update_data)
    

    def delete(self, collection, filter_data: dict = {}):
        """
        Deletes a single document from a collection that matches the filter criteria.
        
        Args:
            collection (Collection): The collection to delete from.
            filter_data (dict): The filter criteria for selecting the document to delete.
        
        Returns:
            DeleteResult: The result of the delete operation.
        """

        return collection.delete_one(filter_data)
