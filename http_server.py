
import socket
import sys
import mimetypes

www_root = 'web_root'

def response_ok(content, type):
    """returns a basic HTTP response"""
    resp = []
    resp.append("HTTP/1.1 200 OK")
    resp.append("Content-Type: %s" % type)
    resp.append("")
    if content:
        resp.append(content)
    else:
        resp.append('no content to report')
    return "\r\n".join(resp)

def response_http_error(http_error):
    """returns an HTTP error code"""
    resp = []
    resp.append("HTTP/1.1 %s" % http_error)
    resp.append("")
    return "\r\n".join(resp)

def response_not_found():
    """returns a 404 Not Found"""
    resp = []
    resp.append("HTTP/1.1 404 Not Found")
    resp.append("")
    return "\r\n".join(resp)

def response_method_not_allowed():
    """returns a 501 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 501 Not Implemented")
    resp.append("")
    return "\r\n".join(resp)

def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
        raise NotImplementedError("We only accept GET")
    print >>sys.stderr, 'request is okay'
    return uri

def build_request(conn):
    """Build request"""
    while True:
        data_chunk = [] # Create new list
        data = conn.recv(1024) # Receive data chunk - blocking until data is received
        data_chunk.append(data) # Add data to list
        if len(data) < 1024 or not data:
            break
    return "\r\n".join(data_chunk)

def resolve_uri(uri):
    """
     return file contents and type -
     e.g., blah/blah/image.jpg - content = image, type = img/jpg ??
    """

    m, t = mimetypes.guess_type(www_root + uri, strict=True)

    if m.startswith('text/'):
        mode = 'r'
    else:
        mode = 'rb'

    f = open(www_root + uri, 'rb')
    c = f.read()
    f.close()
    return (c, m)

def server():

    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>sys.stderr, "making a server on %s:%s" % address
    sock.bind(address)
    sock.listen(1)

    try:

        while True:

            print >>sys.stderr, 'waiting for a connection'
            conn, addr = sock.accept()

            try:

                print >>sys.stderr, 'connection - %s:%s' % addr

                request = build_request(conn)

                print >>sys.stderr, 'request built: %s' % request

                try:
                    uri = parse_request(request)
                except NotImplementedError:
                    response = response_method_not_allowed()
                else:

                    try:
                        content, type = resolve_uri(uri)
                    except IOError:
                        response = response_not_found()
                    except TypeError:
                        response = response_http_error('404.3 Mime Not Found')
                    else:
                        response = response_ok(content, type)

                print >>sys.stderr, 'sending response'
                conn.sendall(response)

            finally:
                conn.close()

    except KeyboardInterrupt:
        sock.close()
        return


if __name__ == '__main__':
    server()
    sys.exit(0)
