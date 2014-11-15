#!/usr/bin/python
#Easy to use script that generates the old style Issuu embed HTML.
#v0.2: quick tuning, created/modified a lazily hardset value into a var to allow for dynamicism.
#PhG

import re, urllib
from bs4 import BeautifulSoup

url = raw_input("Input the URL with http:// for the issuu site you want v1 embed code for (Ex: http://issuu.com/underrepublic/docs/undr_rpblc_mgzn__29)\r\n")
page = urllib.urlopen(url)
soup = BeautifulSoup(page.read())
sdocid = soup.findAll('meta', {"property":'og:video:secure_url'})

docid = str(re.findall("documentId\=[0-9]{12}\-[a-f0-9]{32}", str(sdocid))).replace("['", "").replace("']", "")
docname = 'docName=' + url.split('/')[5]
username = 'username=' + url.split('/')[3]

loadnfo = raw_input("Define what the loading text should say here:\r\n")
hexloadnfo = 'loadingInfoText=' + urllib.quote(loadnfo)

print("Below is the code for the issuu site and parameters that have been specified, simply copy and paste!\r\n\r\n")
print('<object style="width: 420px; height: 325px; z-index: 0; margin: 0px auto; display: block;" height="325" width="420"><param name="movie" value="http://static.issuu.com/webembed/viewers/style1/v1/IssuuViewer.swf?mode=embed&layout=http%3A%2F%2Fskin.issuu.com%2Fv%2Flight%2Flayout.xml&showFlipBtn=true&'+docid+'&'+docname+'&'+username+'&'+hexloadnfo+'&et=1364419538680&er=66"><param name="allowfullscreen" value="true"><param name="menu" value="false"><param name="allowscriptaccess" value="always">'+'<embed wmode="transparent" src="http://static.issuu.com/webembed/viewers/style1/v1/IssuuViewer.swf" type="application/x-shockwave-flash" allowfullscreen="true" menu="false" style="width: 420px; height: 325px; z-index: 0; margin: 0px auto; display: block;" flashvars="mode=embed&layout=http%3A%2F%2Fskin.issuu.com%2Fv%2Flight%2Flayout.xml&showFlipBtn=true&'+docid+'&'+docname+'&'+username+'&'+hexloadnfo+'&et=1364419538680&er=66" height="325" width="420"></object>')