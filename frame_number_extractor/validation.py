from flask import request
from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest, UnsupportedMediaType


def validate_schema(schema, content=None, additional_properties_allowed=False):
    if not content:
        if request.content_type != 'application/json':
            raise UnsupportedMediaType('Expected content-type application/json')
        if request.is_json:
            content = request.json
    schema["additionalProperties"] = additional_properties_allowed

    validate_dict_content_with_schema(content, schema)


def validate_dict_content_with_schema(content, schema):
    try:
        validate(content, schema)
    except ValidationError as e:
        raise BadRequest(e.message)
