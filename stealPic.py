#!/usr/bin/python
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
	
def getImage(html):
	reg = r'src="(.*?\.jpg)" width'
	imagre = re.compile(reg)
	imagelist = re.findall(imagre,html)
	
	x=0
	for imgurl in imagelist:
		urllib.urlretrieve(imgurl,"%s.jpg" %x)
		x+=1
	
#if __name__ == "__main()__":
html = getHtml("http://tieba.baidu.com/f?kw=mv&tp=1")
getImage(html)
	
		

	

	