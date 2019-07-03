''' This script will take an old CONTENTdm url from a 6.x hosted site and
convert it to the responsive version. It works for collections, searches,
and references to single items.
written June 2019 by Kent Gerber
'''

from urllib.parse import urlparse
#pulls in package that breaks a url in logical parts of a list

#import pyperclip - doesn't work will need to troubleshoot

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

# content.clic.edu doesn't have certificate so replace it if present
# to use for other hosted site subsitute these variables ([your alias], [cdm hosted url])
newcdmnetloc = cdmnetloc.replace('content.clic.edu', 'cdm16120.contentdm.oclc.org')

#convert old path to responsive one - replace cdm with digital and remove landingpage
pathlist = cdmpath.split('/')

#results in list like this - ['', 'cdm', 'landingpage', 'collection', 'p15186coll6']
newpathlist = [word.replace('cdm', 'digital') for word in pathlist]
#should result in ['', 'digital', 'landingpage', 'collection', 'p15186coll6']

#remove deprecated, no longer used, parts of the old url
if 'landingpage' in newpathlist:
    newpathlist.remove('landingpage')
#deprecated from links to specific items
if 'ref' in newpathlist:
    newpathlist.remove('ref')
if 'singleitem' in newpathlist:
    newpathlist.remove('singleitem')

#reposition search in the url    
if 'search' in newpathlist:
    newpathlist.remove('search')
    newpathlist.insert(4, 'search')

#should result in ['', 'digital', 'collection', 'p15186coll6', 'search', ...]
newpath = '/'.join(newpathlist)

#put new url into a variable - newcdmurl
newcdmurl = newscheme + '://' + newcdmnetloc + newpath

#produce new repsonsive url using concatenation
print('Your new CONTENTdm responsive url is:')
print (newcdmurl)

#pyperclip.copy(newcdmurl) - currently doesn't work
