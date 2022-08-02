from flask import Flask

app = Flask(__name__)

from app import views
from app import error_handlers
from app import locator
from app import locator2
from app import database
