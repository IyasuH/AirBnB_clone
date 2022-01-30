#!/usr/bin/python3
"""
init file to reload storage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
