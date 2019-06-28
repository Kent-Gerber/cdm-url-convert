''' This script will take an old CONTENTdm url from a 6.x hosted site and
convert it to the responsive version. It works for collections, searches,
and references to single items.
'''
# written June 2019 by Kent Gerber

from urllib.parse import urlparse
#import pyperclip - doesn't work will need to troubleshoot
#pulls in package that breaks a url in logical parts of a list
print('Enter old CONTENTdm url:')
cdmurl = input()
o = urlparse(cdmurl)
o
#result looks something like this:
#ParseResult(scheme='http', netloc='cdm16120.contentdm.oclc.org', path='/cdm/landingpage/collection/p15186coll6', params='', query='', fragment='')
#create variables to store the parts of the url.
cdmscheme = o.scheme
cdmnetloc = o.netloc
cdmpath = o.path

#convert http to https and store in new variable
newscheme = "".join([cdmscheme,'s'])

#convert old path to responsive one - replace cdm with digital and remove landingpage
pathlist = cdmpath.split('/')

#results in list like this - ['', 'cdm', 'landingpage', 'collection', 'p15186coll6']
newpathlist = [word.replace('cdm', 'digital') for word in pathlist]
#should result in ['', 'digital', 'landingpage', 'collection', 'p15186coll6']

#remove any parts of the old url that no longer work
if 'landingpage' in newpathlist:
    newpathlist.remove('landingpage')
if 'ref' in newpathlist:
    newpathlist.remove('ref')
if 'search' in newpathlist:
    newpathlist.remove('search')
    newpathlist.insert(4, 'search')

#should result in ['', 'digital', 'collection', 'p15186coll6', 'search', ...]
newpath = '/'.join(newpathlist)

#put new url into a variable - newcdmurl
newcdmurl = newscheme + '://' + cdmnetloc + newpath

#produce new repsonsive url using concatenation
print('Your new CONTENTdm responsive url is:')
print (newcdmurl)

#pyperclip.copy(newcdmurl) - currently doesn't work
