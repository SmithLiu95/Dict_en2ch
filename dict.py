from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

if __name__ == '__main__':
    words=sys.argv[1:]
    flag_example_config=False
    for x in words:
        if x.startswith('--example') or x.startswith('--e'):
            flag_example_config=True
        print('----Word: '+x+'----')
        respnse = ''
        print('url:  http://dict.cn/'+x)
        try:
            response = urlopen('http://dict.cn/'+x)
        except Exception as e:
            message = str(e)
            print(message)
            break
        html_doc = response.read()
        soup = BeautifulSoup(html_doc, 'lxml', from_encoding='utf8')
        p = [s.extract() for s in soup('div')]
        flag_example=flag_example_config

        for div in p:
            attr = div.attrs
            if 'class' not in attr:
                continue
            if 'ifufind' in attr['class']:
                print('word '+x+' is not in dict.cn!')
                break
            if 'basic' in attr['class']:
                print(x+'  释义')
                tmp=div.get_text()
                tmp=tmp[2:-518]
                print(tmp)
            if flag_example and 'layout' in attr['class'] and 'sort' in attr['class']:
                flag_example=False
                print('例句')
                print(div.get_text()[2:])
