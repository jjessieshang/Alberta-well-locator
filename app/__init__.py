from flask import Flask

app = Flask(__name__)

from app import views
from app import error_handlers
from app import locator
from app import locator2
from app import add_record
from app import edit_or_delete
from app import edit_record
from app import delete_record
from app import select_record
from app import database
