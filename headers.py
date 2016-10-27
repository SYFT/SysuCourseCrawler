import copy

general = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Host":"uems.sysu.edu.cn",
    "Pragma":"no-cache",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
}

checkcode = copy.copy(general)
checkcode['Accept'] = 'image/webp,image/*,*/*;q=0.8'
checkcode['Referer'] = 'http://uems.sysu.edu.cn/elect'

login = copy.copy(general)
login['Accept-Encoding'] = 'gzip, deflate'
login['Content-Length'] = '104'
login['Content-Type'] = 'application/x-www-form-urlencoded'
login['origin'] = 'http://uems.sysu.edu.cn'
login['Referer'] = 'http://uems.sysu.edu.cn/elect'
