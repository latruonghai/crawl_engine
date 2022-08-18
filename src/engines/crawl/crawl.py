import bs4
import requests

Response = requests.models.Response
BeautifulSoup = bs4.BeautifulSoup
ResultSet = bs4.element.ResultSet


class Crawl:
    """
    Instance for crawling website data. This is abstract class for crawling action
    """

    def __init__(self, base_url: str):
        """

        :param base_url: used for detect what url used for crawling
        :return:
        """
        self.base_url = base_url

    # noinspection PyMethodMayBeStatic
    def get_request(self, url: str) -> Response:
        """
        :return: request from url
        """
        req = requests.get(url)

        return req

    def get_content(self, url: str) -> BeautifulSoup:
        response: Response = self.get_request(url)
        return bs4.BeautifulSoup(response.text, "html.parser")

    def get_element(self, content: BeautifulSoup, kwargs: dict) -> ResultSet:
        return content.find_all(**kwargs)


if __name__ == '__main__':
    crawl = Crawl('hello')
    content = crawl.get_content('https://vi.wikipedia.org/wiki/Leonhard_Euler')
    result = crawl.get_element(content, {'name': 'div', 'class_': 'mw-workspace-container vector-sidebar-container'})

    print(result)
