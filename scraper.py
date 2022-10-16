import requests
import lxml.html as html


HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//h2/a/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            # title = parsed.xpath(XPATH_TITLE)[0]
            # summary = parsed.xpath(XPATH_SUMMARY)[0]
            # body = parsed.xpath(XPATH_BODY)
        else:
            raise ValueError(f'Error : {response.status_code}')
    except Exception as e:
        print(e)


def run():
    parse_home()


if __name__ == "__main__":
    run()