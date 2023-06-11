#!/usr/bin/python3

with open('/opt/bitnami/apache/cgi-bin/my_index.html', 'r') as f:
    html = f.readlines()
for h in html:
    print(h)