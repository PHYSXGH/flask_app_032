from flask import Blueprint, request
from .validation import validate_schema

frame_numbers = Blueprint('frame_numbers', __name__)

extract_frame_schema = {
    "type": "object",
    "properties": {
        "Filename": {
            "type": "string"
        },
        "FirstFrameNumber": {
            "type": "string"
        },
        "LastFrameNumber": {
            "type": "string"
        }
    },
    "required": ["Filename", "FirstFrameNumber", "LastFrameNumber"]
}


@frame_numbers.route('/extract_frame_filenames', methods=['POST'])
def extract_frame_filenames():
    validate_schema(extract_frame_schema, additional_properties_allowed=True)

    contents = request.json

    filename = contents['Filename']
    first_frame_number = contents['FirstFrameNumber']
    last_frame_number = contents['LastFrameNumber']

    first_frame = filename.replace('%07d', first_frame_number)
    last_frame = filename.replace('%07d', last_frame_number)

    response = {
        'FirstFrame': first_frame,
        'LastFrame': last_frame
    }

    return response
