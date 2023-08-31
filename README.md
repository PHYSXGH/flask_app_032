# This is a Flask web-application

This is an application that processes the input according to the specifications.

It includes four unit tests, ran using pytest.

The CI/CD pipeline uses Github actions.

It lints the code and runs the four unit tests, after which it builds a container
image using, but currently does not push it to any repository.

The container itself uses gunicorn which enables it to handle multiple connections
at once, essentially running separate instances of the python application 
for each session.

The flask application is contained inside the frame_number_extractor folder,
with the frame_number.py file storing the endpoint itself. The validation.py file
contains some added logic to validate the structure of the body of the incoming
POST request before they are processed. This will ensure that incorrectly formatted
inputs don't cause unwanted behaviour.

The unit tests handle the expected scenario wherein a correct output is produced for
the sample input and some edge cases which invoke the expected error codes. They are
all stored in the test folder.