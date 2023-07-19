from urllib.parse import parse_qs


def wsgi_first(environ, start_response):
    body = parse_qs(environ[QUERY_STRING])
    status = "2000 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return body
