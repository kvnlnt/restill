def content_size(environ):
    try:
        req_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        req_body_size = 0

    return req_body_size


def content_type():
    return ('Content-Type', 'text/html')


def content_length(resp_body):
    return ('Content-Length', str(len(resp_body)))
