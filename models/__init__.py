#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Check the value of the environment variable HBNB_TYPE_STORAGE
storage_type = os.environ.get('HBNB_TYPE_STORAGE')

# Create and configure the appropriate storage instance
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Load data from storage
storage.reload()
