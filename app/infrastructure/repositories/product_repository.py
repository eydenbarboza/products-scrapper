from infrastructure.base_mongodb import BaseMongoDB



class ProductRepository(BaseMongoDB):
    """
    Repository class for managing operations on a specific MongoDB collection.

    Inherits common database operations from BaseMongoDB and adds functionality
    specific to a named collection.
    """

    def __init__(self, db_url: str, db_name: str, collection_name: str) -> None:
        """
        Args:
            db_url (str): The URL of the MongoDB database.
            db_name (str): The name of the MongoDB database.
            collection_name (str): The name of the collection to operate on.
        """
        super().__init__(db_url, db_name)
        self.collection_name = collection_name
        self.collection = None


    def connect(self) -> None:
        """
        Establishes a connection to the database and initializes the collection.
        """
        super().connect()
        self.collection = self.get_collection(self.collection_name)


    def find_all(self, filter_data: dict = {}):
        """
        Finds all documents in the collection that match the filter criteria.

        Args:
            filter_data (dict, optional): The filter criteria for the search,
            defaults to an empty dict.

        Returns:
            Cursor: A cursor to the documents that match the filter criteria.
        """
        return super().find_all(
            collection=self.collection, 
            filter_data=filter_data
        )


    def insert(self, data: dict):
        """
        Inserts a single document into the collection.

        Args:
            data (dict): The document to insert.

        Returns:
            InsertOneResult: The result of the insert operation.
        """
        return super().insert(
            collection=self.collection,
            data=data
        )


    def update(self, filter_data: dict = {}, update_data: dict = {}):
        """
        Updates a single document in the collection that matches the filter criteria.

        Args:
            filter_data (dict, optional): The filter criteria for selecting the 
            document to update. Defaults to an empty dict.
            
            update_data (dict, optional): The update operations to apply to the 
            selected document. Defaults to an empty dict.

        Returns:
            UpdateResult: The result of the update operation.
        """
        return super().update(
            collection=self.collection,
            filter_data=filter_data,
            update_data=update_data
        )


    def delete(self, filter_data: dict = {}):
        """
        Deletes a single document from the collection that matches the filter 
        criteria.

        Args:
            filter_data (dict, optional): The filter criteria for selecting the 
            document to delete. Defaults to an empty dict.

        Returns:
            DeleteResult: The result of the delete operation.
        """
        return super().delete(
            collection=self.collection,
            filter_data=filter_data
        )
