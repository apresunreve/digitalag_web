#!/usr/bin/python3

import os
import cgi
import cgitb
import urllib.request
import dns.resolver


cgitb.enable()
with open('/etc/resolv.kube', 'r') as f:
    kubedns = str(f.read()).strip()
res = dns.resolver.Resolver(configure=False)
res.nameservers = [ kubedns ]

errorHTML='''<html>
<head>
</head>
<body><p> Invalid user credentials.  You can't access this page. CAUSE</p>
</body>
</html>
'''

print ("Content-type: text")
print ("")
#print ("<html>")
#print ("<head></head><body>Debug</body></html>")
#quit()


form = cgi.FieldStorage()

if form.getvalue("state"):
    state = str(form.getvalue("state"))
else:
    errorHTML = errorHTML.replace("CAUSE", "Lost State")
    print (errorHTML)
    quit()
if form.getvalue("code"):
    code = str(form.getvalue("code"))
else:
    errorHTML = errorHTML.replace("CAUSE", "Lost Auth")    
    print (errorHTML)
    quit()

item = "i30080website"
if form.getvalue("ms"):
    item = str(form.getvalue("ms"))

port = "30080"
if form.getvalue("port"):
    port = str(form.getvalue("port"))

page = "index.html"
if form.getvalue("page"):
    page = str(form.getvalue("page"))    
    if '?' in page:
        # This is usually a cgi script with parameters
        # myscript?p1=222
        page.replace("?","&")
        
path=""
if form.getvalue("path"):
    path = str(form.getvalue("path"))

parm=""
pcnt=1
while form.getvalue("p"+str(pcnt)):
    parm = parm+"&p"+str(pcnt) + "="+ str(form.getvalue("p"+str(pcnt)))
    pcnt=pcnt+1


statecode = "&state=" + state + "&code=" +code

# The full DNS name is default.svc.cluster.local
item_orig = item
item = item + ".default.svc.cluster.local"
r = res.resolve(item, 'A')
ipaddr = str(r[0])
msrl='http://'+ipaddr+':'+port+'/' + path + '/'+ page + '?' + "&" + statecode + parm


with urllib.request.urlopen(msrl) as response:
   html = str(response.read().decode("utf-8"))

html=html.replace("href=\"http", "href = \" http")
#Above: Don't want to accidently replace hard coded links

cgibSwap = "href = \"/cgi-bin/callms.py?ms=" + item_orig + "&port=" + port + "&path=/cgi-bin/" + statecode + "&page="
html=html.replace("href=\"/cgi-bin/", cgibSwap)

baseSwap = "href = \"/cgi-bin/callms.py?ms=" + item_orig + "&port=" + port + "&path=/" + statecode + "&page="
html=html.replace("href=\"/", baseSwap)

cntxSwap = "href = \"/cgi-bin/callms.py?ms=" + item_orig + "&port=" + port + "&path=" + page + statecode + "&page="
html=html.replace("href=\"", cntxSwap)

formSwap = "action = \"/cgi-bin/callms.py?"
html=html.replace("action=\"/cgi-bin/", formSwap)

frm2Swap = "<input type = \"hidden\" name = \"state\" value = \"" + state +"\">"
frm2Swap = frm2Swap + "<input type = \"hidden\" name = \"code\" value = \"" + code +"\"></form>"
html=html.replace("</form>", frm2Swap)


html=html.replace("\\n","") #Remove new lines inserted by Python
html=html.replace("\\t","") #Remove new lines inserted by Python

print (html)


#
