# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import robotparser
import urllib2
import time, traceback, re, sys, os
import sqlite3

crawler_name = 'python_daum_crawler'	# 크롤러 이름
mainpage = 'http://blog.daum.net/'	# 다움 메인 페이지
mainpath = './data/'		# data 저장 경로

# robot parser를 세팅합니다.
rp = robotparser.RobotFileParser( mainpage + 'robots.txt' )
rp.read()

def canFetch( url ):
	"수집 가능 여부를 체크합니다."
	return rp.can_fetch( crawler_name, url )
	
def getContent( url, delay=1):
	"웹문서를 다운로드 받습니다."
	time.sleep( delay ) # 약간의 딜레이를 위해 잠시 기다립니다.
	
	if not canFetch( url ):
		# 웹마스터가 수집을 원치 않는 페이지는 수집을하지 않습니다.
		#print 'This url can NOT be fetched by our crawler :', url
		return None
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent',crawler_name)]
		contents = opener.open(url).read()
	except:
		traceback.print_exc()	# 에러 발생 시, 에러로그를 출력합니다.
		return None
	return contents
	
def getArticleInfo( soup ):
	"daum blog 내의 article info를 얻어옵니다."
	
	rBlog = re.compile('.+blog.daum.net/\w+/\d+.*?')
	URLs = soup('a',{'href':rBlog})
	
	return [ u.get('href').split('?')[0] for u in URLs ]

def getOwnArticles( contents ):
	"해당 블로그에 포함되는 글들의 리스트를 가져옵니다."
	ret = []
	soup = BeautifulSoup( contents )
	rBlog = re.compile('.+/BlogTypeView.+')
	for u in soup('a',{'href':rBlog}):
		href = u.get('href')
		article = href.split('articleno=')[1].split('&')[0]
		if ret.count(article)<1:
			ret.append( article )
	return ret

def gatherNeighborInfo( soup ):
	"이웃 블로거/혹은 다녀간 블로거 정보를 수집합니다."

	#daum blog 관련 주소를 찾습니다.
	rBlog = re.compile('http://blog.daum.net/\w+')
	Neighbors = soup('a',{'href':rBlog})
	cnt = 0
	for n in Neighbors:
		url = n.get('href')
		blogname = url.split('/')[-1]
		if url and url.startswith('http://') and db.isCrawledURL(url)<1:
			db.insertURL( url, 1 ) # 읽은 것으로 체크합니다.
			
			url2 = getRedirectedURL( url )
			if not url2: continue
			re_url = 'http://blog.daum.net' + url2
			body = getContent( re_url, 0 ) #frame내의 문서를 읽어옵니다.
			if body:
				for u in getOwnArticles( body ):
					#자신의 글 주소들을 db에 저장합니다.
					fullpath = 'http://blog.daum.net/'+blogname+'/'+u
					cnt+=db.insertURL( fullpath )
			
	if cnt>0: print '%d neighbor articles inserted'%cnt

def getRedirectedURL( url ):
	"본문에 해당하는 frame의 url을 얻어옵니다."
	contents = getContent( url )
	if not contents: return None

	#redirect
	try:
		soup = BeautifulSoup( contents )
		frame = soup('frame')		
		src = frame[0].get('src')
	except:
		src = None
	return src

def getBody( soup, parent ):
	"본문 텍스트를 구합니다."

	# 본문 주소를 포함한 iframe를 찾습니다.
	rSrc = re.compile('.+/ArticleContentsView.+')
	iframe = soup('iframe',{'src':rSrc})
	if len(iframe)>0: # iframe이 있는 경우
		src = iframe[0].get('src')
		iframe_src = 'http://blog.daum.net'+src
		
		# 그냥 request하면 안되고, referer를 지정해야지 browser를 통해서 request한 것으로 인식합니다.
		req = urllib2.Request( iframe_src )
		req.add_header('Referer', parent )
		body = urllib2.urlopen(req).read()
		soup = BeautifulSoup( body )
		return str(soup.body)	# html의 body부분을 문자열로 반환합니다.
	else:
		print 'NULL contents' #iframe으로 본문을 싼 경우에 대해서만 처리합니다.
		return ''

def parseArticle( url ):
	"해당 url을 parsing하고 저장합니다."
	
	#blog id와 article id를 얻습니다.
	article_id = url.split('/')[-1]
	blog_id = url.split('/')[-2]
	
	#for debugging, temp
	if blog_id.isdigit():
		print 'digit:', url.split('/')
	
	#redirect된 주소를 얻어옵니다.
	newURL = getRedirectedURL( url )
	
	if newURL:
		try:
			#blog 폴더를 만듭니다.
			os.mkdir( mainpath + blog_id )
		except:
			# 폴더를 만들다 에러가 난 경우 무시합니다.
			pass
		
		newURL = 'http://blog.daum.net'+newURL
		contents = getContent( newURL, 0 )
		if not contents:
			print 'Null Contents...'
			# 해당 url이 유효하지 않은 경우 에러(-1)로 표시합니다.
			db.updateURL( url, -1 )
			return

		# html을 파싱합니다.
		soup = BeautifulSoup( contents )
	
		#이웃 블로거 정보가 있나 확인합니다.
		gatherNeighborInfo( soup )		

		# 블로그 url이 있을 경우 db에 insert합니다.
		n=0
		for u in getArticleInfo( soup ):
			n+=db.insertURL( u )
		if n>0: print 'inserted %d urls from %s'%(n,url)
			
		# title을 얻습니다.
		sp = contents.find('<title>')
		if sp>-1:
			ep = contents[sp+7:].find('</title>')
			title = contents[sp+7:sp+ep+7]
		else:
			title = ''
					
		#본문 HTML을 보기 쉽게 정리합니다.
		contents = getBody( soup, newURL )
		
		# script들을 제거합니다.
		pStyle = re.compile('<style(.*?)>(.*?)</style>', re.IGNORECASE | re.MULTILINE | re.DOTALL )
		contents = pStyle.sub('', contents)
		pStyle = re.compile('<script(.*?)>(.*?)</script>', re.IGNORECASE | re.MULTILINE | re.DOTALL )
		contents = pStyle.sub('', contents)
		pStyle = re.compile("<(.*?)>", re.IGNORECASE | re.MULTILINE | re.DOTALL )
		contents = pStyle.sub("", contents)
				
		#txt file을 저장합니다.
		fTXT = open( mainpath + blog_id + '/' + article_id + '.txt', 'w' )
		fTXT.write( title+'\n' ) # txt file의 첫라인은 제목을 저장합니다.
		fTXT.write( contents )
		fTXT.close()
		
		# 처리했다고 db에 표시합니다.
		db.updateURL( url )
		
	else:
		print 'Invalid blog article...'
		# 해당 url이 유효하지 않은 경우 에러(-1)로 표시합니다.
		db.updateURL( url, -1 )
	
class DB:
	"SQLITE3 wrapper class"
	def __init__(self):
		self.conn = sqlite3.connect('crawlerDB')
		self.cursor = self.conn.cursor()
		self.cursor.execute('CREATE TABLE IF NOT EXISTS urls(url text, state int)')
		self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS IDX001 ON urls(url)')
		self.cursor.execute('CREATE INDEX IF NOT EXISTS IDX002 ON urls(state)')
	def commit(self):
		self.conn.commit()
	def __del__(self):
		self.conn.commit()
		self.cursor.close()
		
	def insertURL(self, url, state=0):
		#'/' 제거
		if url[-1]=='/': url=url[:-1]
		try:	
			self.cursor.execute("INSERT INTO urls VALUES ('%s',%d)"%(url,state))
		except:
			return 0
		else:
			return 1
			
	def selectUncrawledURL(self):
		self.cursor.execute('SELECT * FROM urls where state=0')
		return [ row[0] for row in self.cursor.fetchall() ]

	def updateURL(self, url, state=1):
		if url[-1]=='/': url=url[:-1]
		self.cursor.execute("UPDATE urls SET state=%d WHERE url='%s'"%(state,url))
		
	def isCrawledURL(self, url):
		if url[-1]=='/': url=url[:-1]
		self.cursor.execute("SELECT COUNT(*) FROM urls WHERE url='%s' and state=1"%url)
		ret = self.cursor.fetchone()
		return ret[0]

db = DB()

if __name__=='__main__':
	print 'starting crawl.py...'
	
	# 메인 페이지를 체크합니다.
	contents = getContent( mainpage )
	URLs = getArticleInfo( BeautifulSoup( contents ) )
	nSuccess = 0
	for u in URLs:
		nSuccess += db.insertURL( u ) #메인 페이지로부터 얻은 url들을 등록합니다.
	print 'inserted %d new pages.'%nSuccess
	
	# 수집된 url 정보를 처리합니다.
	import BlogSearcher
	bs = BlogSearcher.BlogSearcher('./data', './index')
	while 1: # 무한루프
		uncrawled_urls = db.selectUncrawledURL()
		if not uncrawled_urls: break
		for u in uncrawled_urls: 
			#아직 읽지않은 url들을 얻어서 처리합니다.
			print 'downloading %s'%u
			try:
				parseArticle( u )
			except:
				traceback.print_exc()
				db.updateURL( u, -1 )
			db.commit()
		bs.UpdateIndex()