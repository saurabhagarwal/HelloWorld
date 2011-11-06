import urllib,re,sys

def FindNotices(url,page,number):
  f=urllib.urlopen(url) 
  s=f.read()
  f.close()
  if number<=15 & number>=0:
    for i in range(number):
      print re.findall(r'<td .+sr_no.+">(.+)</a></td></tr><tr>',s)[i]
  else: 
    for i in range(15):
      print re.findall(r'<td .+sr_no.+">(.+)</a></td></tr><tr>',s)[i]
    url="http://tp.iitkgp.ernet.in/notice/index.php?page="
    page=page+1
    FindNotices(url+str(page),page,number-15)

def main():
  url="http://tp.iitkgp.ernet.in/notice/index.php?page="
  FindNotices(url+'1',1,int(sys.argv[1]))

if __name__ == "__main__":
    main()
