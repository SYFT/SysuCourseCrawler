# coding: utf-8

# package import
import urllib, urllib2, cookielib, hashlib, copy, sys
from bs4 import BeautifulSoup
import files, urls, headers, postdata

def openWeb(url, headers, post_data = None, limit = 1):
    request = urllib2.Request(url, post_data, headers)
    print url
    print headers
    try :
        response = opener.open(request, timeout = limit)
    except Exception as e:
        print e
        raise Exception('Open ' + url + ' fail.')
    return response

def download(url, headers, storePath, post_data = None, limit = 1):
    request = urllib2.Request(url, post_data, headers)
    try:
        response = opener.open(request, timeout = limit)
        things = open(storePath, 'wb')
        things.write(response.read())
        things.close()
    except Exception as e:
        print e
        raise Exception('Download ' + url + ' failed.')

# def getCheckcode(imgPath):
#     img = Image.open(imgPath)
#     img.load()
#     # denoise
#     img = denoise.denoise(img)

if __name__ == '__main__':
    # build opener
    cookie = cookielib.MozillaCookieJar(files.cookiepath)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    
    while True:
        try :
            # open main page
            response = openWeb(url = urls.mainpage, headers = headers.general)
            print 'Open main page.'
            
            # download checkcode
            download(url = urls.checkcode,
                     headers = headers.checkcode,
                     storePath = files.checkcodepath)
            print 'Download checkcode'

            # checkcode = getCheckcode(files.checkcodepath)
            studentId = raw_input('Please input your student id: ')
            password = raw_input('Please input your password: ')
            checkcode = raw_input('Please input the checkcode: ')
            password = hashlib.md5(password)
            password = password.hexdigest().upper()
            
            post_data = copy.copy(postdata.login)
            post_data['username'] = studentId
            post_data['password'] = password
            post_data['j_code'] = checkcode
            post_data = urllib.urlencode(post_data)
            response = openWeb(url = urls.login,
                               post_data = post_data,
                               headers = headers.login)
            print response.getcode()
            break
        except Exception as e:
            print e
            print 'Now try again'
                
    
    print response.headers
    print response.url
    sid = response.url[response.url.find('sid=') + 4 : ]
    print sid
    
    queryString = copy.copy(postdata.query)
    queryString['sid'] = sid
    queryString['xnd'] = '2016-2017'
    queryString['xq'] = '1'
    queryString = urllib.urlencode(queryString)
    response = openWeb(url = urls.querycourse + queryString,
                       headers = headers.general)
    html = response.read()
    soup = BeautifulSoup(html)
    courses = soup.select('tbody > tr')
    for course in courses:
        temp = course.find_all('td')
        temp = list(temp)
        ret = []
        for t in temp:
            if t.string:
                s = unicode(t.string)
                s = s.replace(u'\n', u'')
                s = s.replace(u'\t', u'')
                ret.append(s)
            else: ret.append(u'')
        ret = tuple(ret)
        print ret

