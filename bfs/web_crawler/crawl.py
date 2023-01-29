from typing import Optional, List
from urllib import request, error

from bs4 import BeautifulSoup

from bfs.web_crawler.web_page import WebPage


def _page(website_url: str) -> Optional[str]:
    try:
        html_page = request.urlopen(website_url, timeout=1)
        encoding = html_page.headers.get_content_charset()
        html = html_page.read().decode(encoding or 'utf-8')

        return html

    except (error.HTTPError, ValueError, TimeoutError, error.URLError):
        return None


def _find_all_links(html: str) -> List[str]:
    soup = BeautifulSoup(html)

    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'][:5] == 'https']

    return links


def make_web_page(url: str, depth: int) -> Optional[WebPage]:
    node = WebPage(url)

    if depth:
        html = _page(url)

        if html:
            links = _find_all_links(html)

            for link in links:
                child_node = make_web_page(link, depth - 1)

                if child_node:
                    print(link)
                    node.adjacent_nodes.append(child_node)

        else:
            return

    return node


if __name__ == '__main__':
    START_POINT = 'https://azdot.gov/'

    web = make_web_page(START_POINT, depth=2)
    print()
