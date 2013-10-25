# -*- coding: cp949 -*-
import os, os.path, sys
os.environ['PATH'] = os.path.join(os.environ['JAVA_HOME'], r'jre\bin\client') + ';' + os.environ['PATH']
import lucene
lucene.initVM(lucene.CLASSPATH)		# Initialize  JVM

def	IndexCreate(fileDir, indexDir):
	analyzer = lucene.StandardAnalyzer()	# 루씬에서 사용하는 객체 생성
	store = lucene.FSDirectory.getDirectory(indexDir)
	writer = lucene.IndexWriter(store, analyzer)

	for root, dirnames, filenames in os.walk(fileDir):	# 입력받은 폴더에서 텍스트 파일만 검색
		for filename in filenames:
			if not filename.endswith('.txt'):
				continue
			
			print("Adding: %s" % filename)
			try:
				path = os.path.join(root, filename)
				f = open(path)
				content = f.read()
				f.close()

				content = content.decode('cp949').encode('utf-8')	# 인코딩을 'utf-8'로 변경

				doc = lucene.Document()				# Document 객체 추가
				doc.add(lucene.Field(	"name", 	# 파일명
										filename,
										lucene.Field.Store.YES,
										lucene.Field.Index.NO))
				doc.add(lucene.Field(	"path", 	# 파일 경로
										path,
										lucene.Field.Store.YES,
										lucene.Field.Index.NO))
				if len(content) > 0:
					doc.add(lucene.Field(	"content", 		# 파일 내용
											content,
											lucene.Field.Store.NO,
											lucene.Field.Index.TOKENIZED))
				else:
					print("Warning: No contents in %s" % filename)
				writer.addDocument(doc)				# 인덱스에 Document 추가
			except Exception, e:
				print("Failed in adding index: %s" % e)

	writer.optimize()          # 인덱스 최적화 및 IndexWriter 객체 닫기
	writer.close()

def SearchKeyword(indexDir, keyword):
	directory = lucene.FSDirectory.getDirectory(indexDir)
	searcher = lucene.IndexSearcher(directory)		# 인덱스 검색 객체
	analyzer = lucene.StandardAnalyzer()

	print ("Searching for %s" % keyword)
	keyword = keyword.decode('cp949').encode('utf-8')
	queryParser = lucene.QueryParser('content', analyzer)				# 질의 생성
	query = queryParser.parse(keyword)
	
	hits = searcher.search(query)					# 검색 수행
	print ("%s matching documents" % hits.length())	# 결과 갯수

	for h in hits:									# 결과 출력
		doc = lucene.Hit.cast_(h).getDocument()
		print("Path: %s, name: %s" % (doc.get("path"), doc.get("name")))

	searcher.close()

if __name__ == '__main__':
	IndexCreate("./files", "./txt_index")
	SearchKeyword("./txt_index", "apple")
