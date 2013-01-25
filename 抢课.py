#mic抢课系统
import urllib2,cookielib,urllib
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
urllib2.install_opener(opener)
opener.addheaders = [('Referer','http://mis.uic.edu.hk/mis/usr/index.do')]
 
def login(username,password):
    param=urllib.urlencode({'j_username':username,'j_password':password,'usertype':'student'})
    loginPage=urllib2.urlopen('http://mis.uic.edu.hk/mis/usr/login.sec',param)
    loginPage.close()
 
def replaceCouse(oldCouseID,newCouseID):
    param=urllib.urlencode({'id':newCouseID,'oldId':oldCouseID})
    replaceCousePage = urllib2.urlopen('http://mis.uic.edu.hk/mis/student/es/replace.do',param)
    page = replaceCousePage.read().replace(" ","")
    replaceCousePage.close()
    print "Replace Couse\n"+"Old Couse ID: "+oldCouseID+"\nNew Couse ID: "+newCouseID
    return page


#抢课脚本2
# -*- coding: utf-8 -*-
# Author xingzhi
# Date 2012-07-06
import urllib2,urllib,cookielib
from bs4 import BeautifulSoup
 
class MIS:
 
  REFERERPAGE = 'http://mis.uic.edu.hk/mis/usr/index.do'
  LOGINPAGE = 'http://mis.uic.edu.hk/mis/usr/login.sec'
  BASEURL = 'http://mis.uic.edu.hk/mis/student/es/'
  ELECTIVE = 'http://mis.uic.edu.hk/mis/student/es/elective.do'
  ELEDETAIL = 'http://mis.uic.edu.hk/mis/student/es/eleDetail.do'
  SELECTPAGE = 'http://mis.uic.edu.hk/mis/student/es/select.do'
 
  def __init__(self, username, password):
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    self.opener.addheaders = [('Referer',self.REFERERPAGE)]
    self.targetCourse = []
    self.__login(username,password)
    self.__getAllCourses()
 
  def __getSoup(self,pageURL,paramaters=None):
    page = self.opener.open(pageURL,paramaters)
    html = "".join([line.strip() for line in page.read().split("\n")])
    soup = BeautifulSoup(html)
    page.close()
    return soup
 
  def __login(self,username,password):
    paramaters = urllib.urlencode({'j_username':username,'j_password':password,'usertype':'student'})
    soup = self.__getSoup(self.LOGINPAGE,paramaters)
    who = soup.find("dd", "name").contents[1].contents[2].encode('utf-8')
    print "\nWelcome, %s \n" % who
 
  def __getViewCoursesLink(self):
    soup = self.__getSoup(self.ELECTIVE)
    viewCoursesLinks = soup.findAll(title="Select Course")
    courseLinks = []
    for link in viewCoursesLinks:
      courseLinks.append(self.BASEURL + link['href'])
    return courseLinks
 
  def __getelectiveTypeId(self):
    courseLinks = self.__getViewCoursesLink()
    self.electiveTypeId = []
    for link in courseLinks:
      self.electiveTypeId.append(link[link.find('=')+1:])
 
  def __getAllCourses(self):
    courseLinks = self.__getViewCoursesLink()
    self.courses = []
    for i in range(len(courseLinks)):
      soup = self.__getSoup(courseLinks[i])
      courses = soup.find_all('td',id=True)
      for course in courses:
        self.courses.append({'id':course['id'],'name':course.string,'type':i})
 
  def __selectCoursesFromFindResult(self,targetList):
    for i in targetList:
      i = int(i)
      self.targetCourse.append(self.findResult[i])
 
  def displayAllCourses(self):
    print '-------------------------------------------\n'
    print '| Here are all the courses to be selected |\n'
    print '-------------------------------------------\n'
    for course in self.courses:
      print course.get('name')
 
  def findCourse(self,keyword):
    self.findResult = []
    for course in self.courses:
      if course.get('name').lower().find(keyword.lower()) != -1:
        self.findResult.append(course)
 
  def printFindResult(self):
    print '**** Here are all the result of finding the courses ****\n'
    for i in range(len(self.findResult)):
      print '[%d]' % i, self.findResult[i].get('name')
    print '\n'
 
  def printTargetCourse(self):
    print '**** Here are all your target courses ****\n'
    for course in self.targetCourse:
      print course.get('name')
    print '\n'
 
  def prepareSelect(self,keyword=None):
    if not keyword:
      keyword = raw_input("plese input the keyword of course:")
 
    self.findCourse(keyword)
    if not self.findResult:
      print "Sorry, cannot find the course."
    else:
      self.printFindResult()
      print 'plese choose the courses \n'
      print 'like: 1,2,3 \n'
      targetList = raw_input('choise:')
      targetList = targetList.split(',')
      self.__selectCoursesFromFindResult(targetList)
      self.printTargetCourse()
 
  def select(self):
    electiveTypeId = self.__getelectiveTypeId()
    for course in self.targetCourse:
      electiveTypeId = electiveTypeId[course.get('type')]
      id = course.get('id')
      param=urllib.urlencode({'id':id,'electiveTypeId':electiveTypeId})
      replaceCousePage = self.opener.open(SELECTPAGE,param)
 
def main():
  xingzhi = MIS('e930000000','**********')
  #xingzhi.displayAllCourses()
  #xingzhi.findCourse()
  #xingzhi.prepareSelect()
  #xingzhi.prepareSelect("Music")
  #xingzhi.select()
 
if __name__ == "__main__":
    main()
