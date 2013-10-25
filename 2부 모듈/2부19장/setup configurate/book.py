from xml.dom.minidom import parse, parseString
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
        AddBook()
    elif menu == 'e':
        printBookList(SearchBookTitle())
    else:
        print ("error : unknow menu key")

#### xml function implementation
def LoadXMLFromFile():
    #fileName = str(input ("please input file name to load :"))
    fileName = "C:\\xml\\book.xml"
    global xmlFD
    try:
        xmlFD = open(fileName)
    except IOError:
        print ("invalid file name or path")
    else:
        try:
            dom = parse(xmlFD)
        except Exception:
            print ("loading fail!!!")
        else:
            print ("XML Document loading complete")
            return dom
    return None

def BooksFree():
    if checkDocument():
        BooksDoc.unlink()
     
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
                
def AddBook():
     global BooksDoc
     if not checkDocument() :
        return None
     
     ISBN = str(input ('insert ISBN :'))
     title = str(input ('insert Title :'))
     #create Book element
     newBook = BooksDoc.createElement('book')
     newBook.setAttribute('ISBN',ISBN)
     #create Title Element
     titleEle = BooksDoc.createElement('title')
     #create title text element
     titleNode = BooksDoc.createTextNode(title)
     print(type(titleNode))
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

def SearchBookTitle():
    global BooksDoc
    retlist = []
    if not checkDocument():
        return None
    
    keyword = str(input ('input keyword to search :'))
    
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
