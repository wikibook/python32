# -*- coding: cp949 -*-
from django.http import HttpResponse

#for template
from django.template import Context, loader

from BlogSearcher import *  # 3부 2장에서 했던 BlogSearcher를 임포트 합니다.
import os

#global value
BlogDir = "./data" 
IndexDir = "./index"

listSize = 10
showLength = 100

Blog_prefixURL ="http://blog.daum.net/"

def ParameterInputError(req):
    html = "error"
    return HttpResponse(html)
    
def BlogSearchPage(req,mode,keyword,page=1): # req : request
    global listSize
    page = int(page)
    resultTup = callBlogSearch(mode,keyword)
    showItemTup = resultTup[((page-1)*listSize):(page*listSize)] # 슬라이싱 10개의 정보만 가져옵니다.
    searchList = matchContentData(keyword,showItemTup) # 페이지에 표시할 데이터를 생성합니다
    
    totalSize = len(resultTup)       # 검색 결과 밑 부분에 네비게이터를 위한 부분입니다.
    pageCnt = totalSize / listSize
    if (totalSize % listSize ) != 0 :
	      pageCnt += 1
    
    pageList = range(1, pageCnt + 1)
    
    tpl = loader.get_template('search.html')   # 템플릿 로딩
    ctx = Context({ 
    		'searchList' : searchList,                   # 변수값들을 채워 줍니다.
    		'keyword' : keyword,
    		'mode': mode,
    		'pageList' : pageList,
    })
    
    html = tpl.render(ctx)
    return HttpResponse(html)
    
def callBlogSearch(mode,keyword):
    global BlogDir,IndexDir
    bs = BlogSearcher(BlogDir,IndexDir)
    if mode == "exAll":
        rfunc = bs.SearchExactAll
    elif mode == "preAll":
        rfunc = bs.SearchPrefixAll
    elif mode == "extCon":
        rfunc = bs.SearchExactContents
    elif mode == "preCon":
        rfunc = bs.SearchPrefixContents
    else:
        rfunc = bs.SearchExactAll
        
    searchTup = rfunc(keyword.encode('cp949'))
    return searchTup

def matchContentData(keyword,listTup):
    "템플릿에 사용될 데이터를 생성합니다."
    ResultData = []
    for item in listTup:
        conTitle,conPreview = makeContentPreview(keyword,item[1])
        conLink = makeContentLink(item[0],item[1])
        ResultData.append(({'preview':conPreview,'link':conLink,'title':conTitle}))
    return ResultData

def makeContentPreview(keyword,filepath):
    global showLength
    cFD = open(filepath)
    strTitle = cFD.readline()
    contData = cFD.read()
           
    #쓸데 없는 문자와 개행 문자를 삭제합니다.
    contData = contData.replace("&nbsp;","")        # &nbsp; 태그를 삭제합니다.
    contData = contData.replace("\n","")              # 라인리턴 문자를 삭제합니다.
    contData = contData.replace("\r","")              # 라인피드 문자를 삭제합니다.
    contData = contData.strip()                       # 공백을 제거합니다.
     
    contData = contData.decode('utf-8')
    strTitle = strTitle.decode('utf-8')
    
    pos = contData.find(keyword)
    
    PreviewData = ""
    if pos > (showLength/2):
        PreviewData = contData[pos - (showLength / 2) : pos + (showLength / 2)]
    else:
        PreviewData = contData[0:showLength]
		
    if len(PreviewData) <= 0 :
        PreviewData = u"(본문이 비어 있습니다)"
		
    # 데이터에서 키워드에 해당 하는 곳은 볼드체로 표시합니다.
    strTitle =  strTitle.replace(keyword, "<b>" + keyword + "</b>")
    PreviewData =  PreviewData.replace(keyword, "<b>" + keyword + "</b>")
        
    return strTitle,PreviewData

def makeContentLink(id,filepath):
    global Blog_prefixURL;
    list = filepath.split("\\")
    blog_uid = list[len(list)-1]
    blog_uid= blog_uid.replace(".txt","")
    return Blog_prefixURL + id + "/" + blog_uid



































