import urllib


def testStatusCode():
	url = 'http://www.mozilla.com/en-US/abck'
	page = urllib.urlopen(url)
	if  page.code == 404:
	    print 'passed'
	else:
	    print "%s returned %d" %(url,page.code)
	
	
testStatusCode()
