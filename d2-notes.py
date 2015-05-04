
##
# Day 2 Sockets Notes
##
#
# webfaction imap server
# Username: python200_demo Password: demo

# >>> import imaplib
# >>> dir(imaplib)
# ['AllowedVersions', 'CRLF', 'Commands', 'Continuation', 'Debug', 'Flags', 'IMAP4', 'IMAP4_PORT', 'IMAP4_SSL', 'IMAP4_SSL_PORT', 'IMAP4_stream', 'Int2AP', 'InternalDate', 'Internaldate2tuple', 'Literal', 'MapCRLF', 'Mon2num', 'ParseFlags', 'Response_code', 'Time2Internaldate', 'Untagged_response', 'Untagged_status', '_Authenticator', '_MAXLINE', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', 'binascii', 'errno', 'random', 're', 'socket', 'ssl', 'subprocess', 'sys', 'time']
# >>> imaplib.Debug = 4
# >>> conn = imaplib.IMAP4_SSL('mail.webfaction.com')
#   48:04.64 imaplib version 2.58
#   48:04.64 new IMAP4 connection, tag=NMHK
#   48:04.70 < * OK [CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN] Dovecot ready.
#   48:04.70 > NMHK0 CAPABILITY
#   48:04.76 < * CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE AUTH=PLAIN
#   48:04.76 < NMHK0 OK Capability completed.
#   48:04.76 CAPABILITIES: ('IMAP4REV1', 'LITERAL+', 'SASL-IR', 'LOGIN-REFERRALS', 'ID', 'ENABLE', 'IDLE', 'AUTH=PLAIN')
# >>> conn.login(python200_demo, demo)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'python200_demo' is not defined
# >>> conn.login('python200_demo', 'demo')
#   48:35.29 > NMHK1 LOGIN python200_demo "demo"
#   48:37.69 < * CAPABILITY IMAP4rev1 LITERAL+ SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS MULTIAPPEND UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS
#   48:37.69 < NMHK1 OK Logged in
# ('OK', ['Logged in'])
