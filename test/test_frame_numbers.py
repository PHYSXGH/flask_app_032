import json

from frame_number_extractor import app


def test_extract_frame_filenames__success():
    # load sample input and output
    input_file = open('sample_files/input.json', 'r')
    raw_sample_input = input_file.read()
    output_file = open('sample_files/output.json', 'r')
    raw_sample_output = output_file.read()
    sample_output = json.loads(raw_sample_output)

    # initialize test client and send request
    client = app.test_client()
    r = client.post('/frame_numbers/extract_frame_filenames', data=raw_sample_input, content_type='application/json')

    assert r.status_code == 200
    assert r.json == sample_output


def test_extract_frame_filenames__incorrect_request_type():
    # initialize test client and send request
    client = app.test_client()
    r = client.get('/frame_numbers/extract_frame_filenames')

    assert r.status_code == 405


def test_extract_frame_filenames__incorrect_input_format():
    # load sample input and output
    input_file = open('sample_files/input.json', 'r')
    raw_sample_input = input_file.read()

    # initialize test client and send request
    client = app.test_client()
    r = client.post('/frame_numbers/extract_frame_filenames', data=raw_sample_input)

    assert r.status_code == 415


def test_extract_frame_filenames__incorrect_field_contents():
    # load sample input and output
    input_file = open('sample_files/input.json', 'r')
    raw_sample_input = input_file.read()
    sample_input = json.loads(raw_sample_input)
    output_file = open('sample_files/output.json', 'r')
    raw_sample_output = output_file.read()
    sample_output = json.loads(raw_sample_output)

    # modify the contents of the input file, making it different from the expected format
    sample_input['Filename'] = 123

    # initialize test client and send request
    client = app.test_client()
    r = client.post('/frame_numbers/extract_frame_filenames', data=json.dumps(sample_input), content_type='application/json')

    assert r.status_code == 400
