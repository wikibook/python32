# *-* coding: cp949 -*- 
from xml.dom.minidom import parse, parseString # minidom 모듈의 파싱 함수를 임포트합니다.
from xml.etree import ElementTree

##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None

#### Menu  implementation
def printMenu():
    print("\nWelcome! Book Manager Program (xml version)") 
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("Add new book: a")
    print("sEarch Book Title: e")
    print("Make html: m")
    print("==================")
    
def launcherFunction(menu):
    global BooksDoc
    if menu ==  'l':
        BooksDoc = LoadXMLFromFile()
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':
        PrintDOMtoXML()
    elif menu == 'b':
        PrintBookList(["title",])
    elif menu == 'a':
        ISBN = str(input ('insert ISBN :'))
        title = str(input ('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    else:
        print ("error : unknow menu key")

#### xml function implementation
def LoadXMLFromFile():
    fileName = str(input ("please input file name to load :"))  # 읽어올 파일경로를 입력 받습니다.
    global xmlFD
 
    try:
        xmlFD = open(fileName)   # xml 문서를 open합니다.
    except IOError:
        print ("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xmlFD)   # XML 문서를 파싱합니다.
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            return dom
    return None

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()   # minidom 객체 메모리를 해제합니다.
     
def QuitBookMgr():
    global loopFlag
    loopFlag = 0
    BooksFree()

def PrintDOMtoXML():
    if checkDocument():
        print(BooksDoc.toxml())

def PrintBookList(tags):
    global BooksDoc
    if not checkDocument():
       return None
        
    booklist = BooksDoc.childNodes
    book = booklist[0].childNodes
    for item in book:
        if item.nodeName == "book":
            subitems = item.childNodes
            for atom in subitems:
               if atom.nodeName in tags:
                   print("title=",atom.firstChild.nodeValue)
                
def AddBook(bookdata):
     global BooksDoc
     if not checkDocument() :
        return None
     
     #create Book element
     newBook = BooksDoc.createElement('book')
     newBook.setAttribute('ISBN',bookdata['ISBN'])
     #create Title Element
     titleEle = BooksDoc.createElement('title')
     #create title text element
     titleNode = BooksDoc.createTextNode(bookdata['title'])
     # connect to title node
     try:
         titleEle.appendChild(titleNode)
     except Exception:
         print ("append child fail- please,check the parent element & node!!!")
         return None
     else:
         titleEle.appendChild(titleNode)

     # connect to book node
     try:
         newBook.appendChild(titleEle)
         booklist = BooksDoc.firstChild
     except Exception:
         print ("append child fail- please,check the parent element & node!!!")
         return None
     else:
         if booklist != None:
             booklist.appendChild(newBook)

def SearchBookTitle(keyword):
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None
        
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
        
    #get Book Element
    bookElements = tree.getiterator("book")  # return list type
    for item in bookElements:
        strTitle = item.find("title")
        if (strTitle.text.find(keyword) >=0 ):
            retlist.append((item.attrib["ISBN"], strTitle.text))
    
    return retlist    

def MakeHtmlDoc(BookList):
    from xml.dom.minidom import getDOMImplementation
    #get Dom Implementation
    impl = getDOMImplementation()
    
    newdoc = impl.createDocument(None, "html", None)  #create DOM
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    #create body
    body = newdoc.createElement('body')

    for bookitem in BookList:
        #create bold element
        b = newdoc.createElement('b')
        #create text node
        ibsnText = newdoc.createTextNode("ISBN:" + bookitem[0])
        b.appendChild(ibsnText)

        body.appendChild(b)
    
        #create br tag
        br = newdoc.createElement('br')

        body.appendChild(br)

        #create title Element
        p = newdoc.createElement('p')
        #create text node
        titleText= newdoc.createTextNode("Title:" + bookitem[1])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  #line end
         
    #append Body
    top_element.appendChild(body)
    
    return newdoc.toxml()
    
def printBookList(blist):
    for res in blist:
        print (res)
    
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("Error : Document is empty")
        return False
    return True
  

##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")

