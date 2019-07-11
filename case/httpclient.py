import requests
import unittest


class httpclient(unittest.TestCase):

    def __init__(self, url, method='get', body_type='urlencoded'):
        self.url = url
        self.method = method
        self.body_type = body_type
        self.params = {}
        self.headers = {}
        self.res = None
        self._type_equality_funcs = {}

    def set_headers(self, headers):
         if isinstance(headers, dict):
            self.headers = headers
         else:
             raise Exception('头信息只支持字典格式！')

    def set_params(self, params):
         if isinstance(params, dict):
            self.params = params
         else:
             raise Exception('请求正文只支持字典格式！如果是xml，格式如下：{"xml": "content"}')

    def send(self):
        if self.method == 'GET':
            self.res = requests.get(url=self.url, headers=self.headers, params=self.params)
        elif self.method == 'POST':
            if self.body_type == 'urlencoded':
                self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
                self.res = requests.post(url=self.url, headers=self.headers, data=self.params)
            elif self.body_type == 'json':
                self.headers['Content-Type'] = 'application/json'
                self.res = requests.post(url=self.url, headers=self.headers, json=self.params)
            elif self.body_type == 'xml':
                self.headers['Content-Type'] = 'text/xml'
                xml_str = self.body.get('xml')
                if xml_str:
                    self.res = requests.post(url=self.url, headers=self.headers, data=xml_str)
                else:
                    raise Exception('正文体格式错误！xml正文格式如下：{"xml": "content"}')
        else:
            raise Exception("只支持get或post请求！")

    @property
    def status_code(self):
        if self.res:
            return self.res.status_code
        else:
            print('响应对象为空')
            return None

    @property
    def res_times(self):
        if self.res:
            return round(self.res.elapsed.total_seconds() * 1000)
        else:
            print('响应对象为空')
            return None

    @property
    def text(self):
        if self.res:
            return self.res.text
        else:
            print('响应对象为空')
            return None

    def check_status_code_is_200(self):
        self.assertEqual(self.status_code, 200, '响应状态码不等于200， 实际结果：{code}'.format(code=self.status_code))


    def check_res_times_less_than(self, times):
        self.assertLess(self.res_times, times, '响应时间超过预期值， 实际结果：{times}'.format(times=self.res_times))