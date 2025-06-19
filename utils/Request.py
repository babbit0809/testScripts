import requests
import json

'''Base methods of CRUD (Create, Read, Update, Delete )'''
Methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']


class UnSupportMethodException(Exception):
    pass


class HTTPClient(object):
    def __init__(self, url, method, headers=None, cookies=None):
        self.url = url
        self.method = method.upper()
        if self.method not in Methods:
            raise UnSupportMethodException(f"UnSupport Method: {self.method}, please check input parameter.")
        self.session = requests.session()
        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, dtype='json', **kwargs):
        """For GET use params, for POST use data & data_type"""
        if dtype == 'str':
            send_string = data
        else:
            send_string = json.dumps(data)
        print(f"\nRequest Payload:{send_string}, {type(send_string)}")
        response = self.session.request(url=self.url, method=self.method, params=params, data=send_string, **kwargs)
        response.encoding = 'utf-8'
        print(f"\nRequest URL: {self.url} "
              f"\nRequest Method: {self.method} "
              f"\nStatus Code: {response.status_code} "
              f"\nTime(Sec): {response.elapsed.total_seconds()} "
              f"\nResponse Content:\n{response.text}")

        return response


if __name__ == '__main__':
    pass
