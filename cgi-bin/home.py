with open('/opt/bitnami/apache/cgi-bin/my_index.html', 'r') as f:
    html = f.readlines()
print(html)