# -*- coding: cp949 -*-
import os, os.path, sys, time
os.environ['PATH'] = os.path.join(os.environ['JAVA_HOME'], r'jre\bin\client') + ';' + os.environ['PATH']
import lucene

BlogDir = "./data"
IndexDir = "./luceneIndex"
LutPath = IndexDir + "/lastupdatetime.txt"

class BlogSearcher(object):
	def __init__(self, blogDir, indexDir):
		"초기화 작업"
		lucene.initVM(lucene.CLASSPATH)		# JVM을 초기화합니다.
    
		self.blogDir = blogDir
		self.indexDir = indexDir
		self.analyzer = lucene.StandardAnalyzer()
		self.store = lucene.FSDirectory.getDirectory(self.indexDir)

	def __MakeResultFormat(self, hits, searcher):
		"검색 결과 작성"
		ret = []
		for h in hits:
			doc = lucene.Hit.cast_(h).getDocument()
			ret.append((doc.get("bloger").encode("cp949"), doc.get("path").encode("cp949")))

		searcher.close()
		return tuple(ret)
	
	def SearchExactContents(self, keyword):
		"블로그 내용에 대하서 Exactch Matching 수행"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		k = keyword.decode('cp949').encode('utf-8')
		query = lucene.QueryParser('contents', self.analyzer).parse(k)

		hits = searcher.search(query)
		print ("%s matching documents" % hits.length())

		return self.__MakeResultFormat(hits, searcher)

	def SearchPrefixContents(self, keyword):
		"블로그 내용에 대하여 Prefix Matching 수행"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		
		k = keyword.decode('cp949').encode('utf-8')
		query = lucene.PrefixQuery( lucene.Term("contents", k) )

		hits = searcher.search(query)
		print ("%s matching documents" % hits.length())	

		return self.__MakeResultFormat(hits, searcher)

	def SearchPrefixAll(self, keyword):
		"블로그 내용과 ID에 대해여 Prefix Matching 수행"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		keyword+="*"
		k = keyword.decode('cp949').encode('utf-8')

		tqBloger = lucene.WildcardQuery( lucene.Term("bloger", k) )
		tqContents = lucene.WildcardQuery( lucene.Term("contents", k) )

		qBoolean = lucene.BooleanQuery()
		qBoolean.add(tqBloger, lucene.BooleanClause.Occur.SHOULD)
		qBoolean.add(tqContents, lucene.BooleanClause.Occur.SHOULD)

		hits = searcher.search(qBoolean)
		print ("%s matching documents" % hits.length())

		return self.__MakeResultFormat(hits, searcher)

	def SearchExactAll(self, keyword):
		"블로그 내용과 ID에 대해여 Exact Matching 수행"
		searcher = lucene.IndexSearcher(self.store)

		print("Searching for ", keyword)
		k = keyword.decode('cp949').encode('utf-8')

		tqBloger = lucene.TermQuery(lucene.Term("bloger", k))
		tqContents = lucene.TermQuery(lucene.Term("contents", k))

		qBoolean = lucene.BooleanQuery()
		qBoolean.add(tqBloger, lucene.BooleanClause.Occur.SHOULD)
		qBoolean.add(tqContents, lucene.BooleanClause.Occur.SHOULD)

		hits = searcher.search(qBoolean)
		print ("%s matching documents" % hits.length())

		return self.__MakeResultFormat(hits, searcher)

	def UpdateIndex(self):
		"인덱스를 최신의 내용으로 갱신"
		self.lastIndexingTime = self.__ReadLatestUpdateTime()	# 마지막으로 인덱스한 시간(None-인덱스한 적이 없음)
		writer = lucene.IndexWriter(self.store, self.analyzer, lucene.IndexWriter.MaxFieldLength(1048576))

		for root, dirnames, filenames in os.walk(self.blogDir):
			for filename in filenames:
				if not filename.endswith('.txt'):	# txt 파일이 아닌 경우 인덱스하지 않음	
					continue	

				path = os.path.join(root, filename)
				if (self.lastIndexingTime != None and self.lastIndexingTime >= int(os.stat(path).st_mtime)):
					continue		# 이미 인덱스에 추가된 데이터인 경우

				print("Adding: %s" % filename)
				try:
					f = open(path)
					content = f.read()
					f.close()

					doc = lucene.Document()
					doc.add(lucene.Field(	"bloger", 
											path.rsplit("\\", 2)[1],		# 파일이 들어있는 디렉토리를 블로거로 설정
											lucene.Field.Store.YES,
											lucene.Field.Index.UN_TOKENIZED))
					doc.add(lucene.Field(	"path", 
											path,
											lucene.Field.Store.YES,
											lucene.Field.Index.UN_TOKENIZED))
					doc.add(lucene.Field(	"contents", 
											content,
											lucene.Field.Store.NO,
											lucene.Field.Index.TOKENIZED))
					writer.addDocument(doc)
				except Exception, e:
					print("Failed in adding index: %s" % e)

		writer.optimize()
		writer.close()

		self.__WriteLatestUpdateTime()		# 인덱스한 시간을 기록
		print("Completely updated!")
	
	def __WriteLatestUpdateTime(self):
		"인덱싱한 시간을 기록"
		try:
			f = open(LutPath, "w")
			f.write(str(int(time.time())))		# 현재 시간을 기록
			f.close()
		except:
			print("Fail to WriteLatestUpdateTime")
			return False
		else:
			return True
	
	def __ReadLatestUpdateTime(self):
		"가장 최근에 인덱싱한 시간을 읽음"
		try:
			f = open(LutPath, "r")
			t = int(f.read())
			f.close()
		except:
			return None					# 인덱스를 처음 만드는 경우
		else:
			return t


##################################################################################################

#if __name__ == '__main__':
# 	bs = BlogSearcher(BlogDir, IndexDir)

