import os
import sys
import urllib.request
import json

class translator():
    def __init__(self):
        self.client_id = ""
        self.client_secret = ""
        self.url = "https://openapi.naver.com/v1/papago/n2mt"

    def translate(self, eng):
        data = "source=en&target=ko&text=" + eng
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id",self.client_id)
        request.add_header("X-Naver-Client-Secret",self.client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        response_body = json.loads(response.read())
        kor = response_body['message']['result']['translatedText']
        return kor
