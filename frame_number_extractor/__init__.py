from flask import Flask
from .frame_numbers import frame_numbers

app = Flask("frame_number_extractor")
app.register_blueprint(frame_numbers, url_prefix='/frame_numbers')