import re
import urllib
import json
from flask import current_app

# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class IPInfo(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def teardown(self, exception):
        ctx = stack.top

    @property
    def browser(self):
        """获得访客浏览器类型."""
        ua = request.headers.get('User-Agent')
        if (ua):
            browser = ua
            if (re.compile(r'MSIE', re.I).search(ua) or re.compile(r'rv:([^\)]+)\) like Gecko', re.I).search(ua)):
                browser = 'MSIE'
            elif (re.compile(r'Firefox', re.I).search(ua)):
                browser = 'Firefox'
            elif (re.compile(r'Chrome', re.I).search(ua)):
                browser = 'Chrome'
            elif (re.compile(r'Safari', re.I).search(ua)):
                browser = 'Safari'
            elif (re.compile(r'Opera', re.I).search(ua)):
                browser = 'Opera'
            elif (re.compile(r'MinxingMessenger', re.I).search(ua)):
                browser = 'MinxingMessenger'
            elif (re.compile(r'QQ', re.I).search(ua)):
                browser = 'TencentQQ'
            elif (re.compile(r'MicroMessenger', re.I).search(ua)):
                browser = 'WeChat'
            return(browser)
        else:
            return('Unknown')

    @property
    def lang(self):
        """获得访客浏览器语言."""
        lang = request.headers.get('Accept-Language')
        if (lang):
            if (re.compile(r'zh-cn', re.I).search(lang)):
                lang = '简体中文'
            elif (re.compile(r'zh', re.I).search(lang)):
                lang = '繁体中文'
            else:
                lang = 'English'
            return(lang)
        else:
            return('Unknown')

    @property
    def os(self):
        """获得访客操作系统."""
        ua = request.headers.get('User-Agent')
        if (ua):
            if (re.compile(r'win', re.I).search(ua)):
                os = 'Windows'
            elif (re.compile(r'iphone', re.I).search(ua)):
                os = 'iPhone'
            elif (re.compile(r'mac', re.I).search(ua)):
                os = 'MAC'
            elif (re.compile(r'android', re.I).search(ua)):
                os = 'Android'
            elif (re.compile(r'linux', re.I).search(ua)):
                os = 'Linux'
            elif (re.compile(r'unix', re.I).search(ua)):
                os = 'Unix'
            elif (re.compile(r'bsd', re.I).search(ua)):
                os = 'BSD'
            else:
                os = 'Other'
            return(os)
        else:
            return('Unknown')

    @property
    def ipaddress(self):
        """获得IP地址."""
        if (request.headers.get('Client-IP')):
            ip = request.headers.get('Client-IP')
        if (request.headers.get('X-Forwarded-For')):  # 获取代理ip
            ips = request.headers.get('X-Forwarded-For').split(',')
            if (ip):
                ips.insert(0, ip)
            for i in ips:
                if (not re.compile('^(10|172\.16|192\.168)\.', re.I).match(i) and i != 'unknown'):  # 排除局域网ip
                    ip = i
                    break
        tip = request.remote_addr if (request.remote_addr) else ip
        if (tip == '127.0.0.1'):  # 获得本地真实IP
            return self.getOnlineIP()
        else:
            return(tip)

    def getOnlineIP(self):
        """获得本地真实IP."""
        before = time.time()
        html = urllib.request.urlopen(
            'http://ip.taobao.com/service/getIpInfo.php?ip=myip').read()
        after = time.time()
        self.taobao_timeout = self.taobao_timeout + int(after - before)
        ipArray = json.loads(str(html, encoding='utf-8'))
        if (ipArray and ipArray['code'] == 0):
            return ipArray['data']['ip']

    @property
    def location(self, request, ip):
        """根据ip获得访客所在地地名."""
        if (not ip):
            ip = self.ipaddress()

        html = urllib.request.urlopen(
            'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip).read()
        ipArray = json.loads(str(html, encoding='utf-8'))

        if (ipArray and ipArray['code'] == 0):
            return ipArray
        else:
            return False
