#!/usr/bin/python3

import cgi
import cgitb
import urllib.request
import google.oauth2.credentials
import google_auth_oauthlib.flow
import flask

cgitb.enable()
form = cgi.FieldStorage()
state = str(form.getvalue("email"))
state=state.replace("@","DAB")

# Use the client_secret.json file to identify the application requesting
# authorization. The client ID (from that file) and access scopes are required.
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'],state=state)

# Indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required. The value must exactly
# match one of the authorized redirect URIs for the OAuth 2.0 client, which you
# configured in the API Console. If this value doesn't match an authorized URI,
# you will get a 'redirect_uri_mismatch' error.
develEnv="prod"
with open('/root/environment', 'r') as file:
    develEnv = file.readline().strip()
if (develEnv == "devel"):
    flow.redirect_uri = 'http://localhost:30080/cgi-bin/googleoauthresult.py'
else:
    flow.redirect_uri = 'https://reroutlab.org/icicle/authforward.py'


# Generate URL for request to Google's OAuth 2.0 server.
# Use kwargs to set optional request parameters.
authorization_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
    state=state,
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')


print(
'''Content-type: text/html

<html>
<head>
''')
print("<meta http-equiv=\"refresh\" content=\"2; url=\'" + authorization_url + "\'\" />")
print(
'''</head>
<body>
<p>You will be redirected soon!</p>
</body>
</html>
''')

