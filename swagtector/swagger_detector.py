import httpx
from termcolor import colored
from lxml import html

class SwaggerDetector:
    def __init__(self, url, output=None):
        self.url = url
        self.output = output
        self.endpoints = self.__get_swagger_endpoints()

    def __get_swagger_endpoints(self):
        with open('swagtector/list.txt', 'r') as e:
            endpoints = e.read().splitlines()
        return endpoints

    def __get_response_title(self, endpoint):
        try:
            response = httpx.get(f"{self.url}/{endpoint}", verify=False)
            tree = html.fromstring(response.content)
            title = tree.find('.//title').text
        except Exception:
            response = None
            title = None
        return response, title

    def __detect_swagger(self):
        for endpoint in self.endpoints:
            response, title = self.__get_response_title(endpoint)
            if title and 'Swagger' in title:
                print(
                    colored(f"[+] Swagger UI detected at {self.url}/{endpoint}", 'green'))
                if self.output:
                    with open(self.output, 'a') as file:
                        file.write(f"{self.url}/{endpoint}\n")
                break

    def run(self):
        self.__detect_swagger()