"""
A mostly unnecessary file that calls the creator and loader for the db

written by: Matthew Lopez
"""

import db_creator
import db_loader
import picture_downloader

db_creator.create_it()
db_loader.load_it()
picture_downloader