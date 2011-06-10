import lxml.html
import urllib


def checkAllButtons():
    '''
        This script scrapes http://www.mozilla.com product
        download page grabs  *Nix,OSX,Windows download links
        and checks the status code for  each download url
    '''
    url ='http://www.mozilla.com/en-US/products/download.html'
    document = lxml.html.parse(url).getroot()
    document.make_links_absolute()
    osxLinks = document.body.cssselect("li.os_osx>a")
    link = osxLinks[0].get('href')
    print link
    response = urllib.urlopen(link)
    if response.code != 200:
        print "%s  is failing" % (link)
    
    #check for linux
    unixLinks = document.body.cssselect("li.os_linux>a")
    link = unixLinks[0].get('href')
    print link
    response = urllib.urlopen(link)
    if response.code != 200:
        print "%s  is failing" % (link)
    
    #check for windows
    winLinks = document.body.cssselect("li.os_windows>a")
    link = winLinks[0].get('href')
    print link
    response = urllib.urlopen(link)
    if response.code != 200:
        print "%s  is failing" % (link)
    
if __name__ == "__main__":
    checkAllButtons()
