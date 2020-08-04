#0730_3교시_최주원강사님
import requests
from bs4 import BeautifulSoup
import csv

# response = requests.get('https://www.naver.com/')
# print(response.text)

# URL의 규칙성을 찾아보자
# 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EA%B4%91%EC%A3%BC+%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5+%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90'
# 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start=11&refresh_start=0'
# 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=44&start=21&refresh_start=0'
# 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=60&start=31&refresh_start=0'

# def get_news_soup_objects():

#     soup_objects = []

#     #페이지 반복문
#     for i in range(1, 102, 10):
#         base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
#         #start_num은 10씩 올라간다
#         start_num = 11
#         end_url = '&refresh_start=0'

#         URL = base_url + str(start_num) + end_url

#         response = requests.get(URL)
#         #print(response.text)
#         # respons.headers, cookie여러가지
#         soup = BeautifulSoup(response.text, 'html.parser')
#         #html tag기준으로 파싱객체 만들고 soup에 그 return값을 담기
#         #BeautifulSoup함수에 어떤 객체를 어떻게 파싱할것인지 그 return값을 변수에 담기
#         soup_objects.append(soup)

#     return soup_objects

soup_objects = []

#페이지 반복문
for i in range(1, 102, 10):
    base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    #start_num은 10씩 올라간다
    start_num = 11
    end_url = '&refresh_start=0'

    URL = base_url + str(start_num) + end_url

    response = requests.get(URL)
    #print(response.text)
    # respons.headers, cookie여러가지
    soup = BeautifulSoup(response.text, 'html.parser')
    #html tag기준으로 파싱객체 만들고 soup에 그 return값을 담기
    #BeautifulSoup함수에 어떤 객체를 어떻게 파싱할것인지 그 return값을 변수에 담기
    soup_objects.append(soup)

#print(len(soup_objects))

#print(type(soup))  #<class 'bs4.BeautifulSoup'>
#print(soup)

# select -> 배열로 return
# select_one -> 여러개 있다면 배열로 전체가아닌 첫번째꺼 한개만!

#chrome개발자모드에서 크롤링하고싶은 부위의 태그 가져오기
# 다음 > 표시를 이용해 좁혀나가기 folder들어가는 느낌으로
# id = #, class = ., 으로 해도되고 []안에 써도됨
# print(
#     soup.select(
#         'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li'
#     ))

#재사용성을 위해 for문 안에 넣는 것이 아니라 밖으로 빼기
# ex 함수 만들기
# news_section = soup.select(
#     'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li'
# )

# for news in news_section:
#     print(news.select_one('dl > dt > a'), '\n')

# #실습 -> a태그 안에 있는 href와 title 가져오기
# for news in news_section:
#     print(news.select_one('dl > dt > a')['title'])
#     print(news.select_one('dl > dt > a')['href'], '\n')

#실습 : 반복문으로 바꾸기
# for soup in soup_objects:
#     news_section = soup.select(
#         'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li'
#     )
#     for news in news_section:
#         print(news.select_one('dl > dt > a')['title'])
#         print(news.select_one('dl > dt > a')['href'], '\n')

for soup in soup_objects:

    news_section = soup.select(
        'div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul[class=type01] > li'
    )

    for news in news_section:
        a_tag = news.select_one('dl > dt > a')

        news_title = a_tag['title']
        news_link = a_tag['href']

        news_data = {'title': news_title, 'link': news_link}
        #실습 : csv파일로 만들어보기
        with open('./news.csv', 'a') as csvfile:
            fieldnames = ['title', 'link']
            csvwriter = csv.DictWriter(csvfile, fieldnames)

            csvwriter.writerow(news_data)
