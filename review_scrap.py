# 0806
# 실습 : 네이버 영화 크롤링 실습
#     1. 영화 별 리뷰 출력 (한 페이지만 먼저)
#     2. 영화 별 리뷰 출력 및 데이터화 (각 영화별 10 페이지)
import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'https://movie.naver.com/movie/running/current.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li')

movie_data = []

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')

    movie_title = a_tag.text
    movie_code = a_tag['href'].split('code=')[1]

    movie_data.append({'title': movie_title, 'code': movie_code})
    #print(movie_data) # title, code 잘 뽑힘

headers = {
    'authority':
    'movie.naver.com',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site':
    'same-origin',
    'sec-fetch-mode':
    'navigate',
    'sec-fetch-dest':
    'iframe',
    'referer':
    'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language':
    'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie':
    'NNB=ET35ULQSGT7V4; NRTK=ag#20s_gr#2_ma#0_si#0_en#0_sp#0; ASID=7d8801ba00000173222173040000005f; _fbp=fb.1.1594080518895.593955966; NaverSuggestUse=use%26unuse; _ga=GA1.1.1742802988.1596162534; _ga_7VKFYR6RV1=GS1.1.1596162534.1.1.1596162555.39; MM_NEW=1; NFS=2; MM_NOW_COACH=1; nx_ssl=2; BMR=s=1596630572413&r=https%3A%2F%2Fm.post.naver.com%2Fviewer%2FpostView.nhn%3FvolumeNo%3D28914002%26memberNo%3D1972782%26vType%3DVERTICAL&r2=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtab_lve.ag20sgrpma0si0en0sp0%26ie%3Dutf8%26query%3D%25EC%25BB%25A8%25EB%25B2%2584%25EC%258A%25A4; page_uid=UyqFUwprvmsssbb0vKhssssssLV-217256; JSESSIONID=0F4A8391C2FC66B5416E5FEBE5ACB984; csrf_token=5483ea43-7397-4558-a299-7826a4972f28',
}

for movie in movie_data:
    movie_name = movie['title']
    #아 파일명에 : 안들어가네
    movie_name = re.sub(':', '_', movie_name)
    movie_code = movie['code']
    # print(movie_name)  # 울지마 톤즈 2 _ 슈크란 바바
    # print(movie_code)
for i in range(1, 3):
    params = (
        ('code', movie_code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    review_response = requests.get(
        'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn',
        headers=headers,
        params=params)
    #(review_response)

    review_soup = BeautifulSoup(review_response.text, 'html.parser')
    review_list = review_soup.select("div > div > div.score_result > ul > li")
    #print(review_list)

    for review in review_list:
        score = review.select_one("div.star_score > em").text
        review_text = review.select_one(
            "div.score_reple > p > span:nth-last-child(1)")

        if (review_text.select_one('span > a') != None):  #
            review_text = review_text.select_one('span > a')['data-src']
        else:
            review_text = review_text.text.split()

        print(movie_name, score, review_text)

    # with open('./{movie_name}_평점과리뷰.csv', 'a') as csvfile:
    #     fieldnames = ['score', 'review']
    #     csvwriter = csv.DictWriter(csvfile, fieldnames)

    #     for i in range(1, 11):
    #         params = (
    #             ('code', movie_code),
    #             ('type', 'after'),
    #             ('isActualPointWriteExecute', 'false'),
    #             ('isMileageSubscriptionAlready', 'false'),
    #             ('isMileageSubscriptionReject', 'false'),
    #         )

    #         review_response = requests.get(
    #             'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn',
    #             headers=headers,
    #             params=params)
    #         #(review_response)

    #         review_soup = BeautifulSoup(review_response.text, 'html.parser')
    #         review_list = review_soup.select(
    #             "div > div > div.score_result > ul > li")
    #         #print(review_list)

    #         for review in review_list:
    #             score = review.select_one("div.star_score > em").text
    #             review_text = review.select_one(
    #                 "div.score_reple > p > span:nth-last-child(1)")

    #             if (review_text.select_one('span > a') != None):  #
    #                 review_text = review_text.select_one(
    #                     'span > a')['data-src']
    #             else:
    #                 review_text = review_text.text.split()

    #             #print(score, review_text)
    #             csvwriter.writerow({
    #                 'score': score,
    #                 'review': ' '.join(review_text)
    #             })
