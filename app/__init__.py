from flask import Flask

app = Flask(__name__)

from app import views
from app import error_handlers
from app import locator
from app import locator2
from app import add_record
from app import add_property
from app import edit_or_delete
from app import edit_result
from app import delete_result
from app import select_record1
from app import select_record2
from app import database
