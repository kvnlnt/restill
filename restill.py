#!/usr/bin/env python

from wsgiref.simple_server import make_server
from resources.properties import Properties
from cgi import parse_qs
from cgi import escape
import json

html = "%s"

resources = {
    'properties': Properties,
}


def application(environ, start_response):

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0)).lower()
    except (ValueError):
        request_body_size = 0

    # When the method is POST the query string will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    resource = environ['PATH_INFO'].split('/')[1]
    resource = escape(resource)
    resource = resources[resource]()
    resource = json.dumps(resource.__dict__)

    # age = d.get('age', [''])[0]  # Returns the first age value.
    # age = escape(age)

    response_body = html % (resource)

    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
