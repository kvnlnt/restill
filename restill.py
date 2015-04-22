#!/usr/bin/env python

from wsgiref.simple_server import make_server
from resources.properties import Properties
from cgi import parse_qs
from cgi import escape
from headers import content_size
from headers import content_type
from headers import content_length
import json

html = "%s"

resources = {
    'properties': Properties,
}


def application(environ, start_resp):

    # get request info
    req_size = content_size(environ)
    req_body = environ['wsgi.input'].read(req_size)
    req_data = parse_qs(req_body)
    req_uri = environ['PATH_INFO']
    req_method = environ['REQUEST_METHOD']

    # get resource
    resource = req_uri.split('/')[1]
    resource = escape(resource)
    resource = resources[resource](req_method, req_data)

    # create response
    resp = json.dumps(resource.__dict__)
    resp_body = html % (resp)
    resp_status = '200 OK'
    resp_headers = [content_type(), content_length(resp_body)]

    # run response
    start_resp(resp_status, resp_headers)

    # return body
    return [resp_body]

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
