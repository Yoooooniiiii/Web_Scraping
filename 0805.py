#0805_ 네이버 관람객 평점 가져오기
import requests
from bs4 import BeautifulSoup

response = requests.get('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li')

final_movie_data = []

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')
    movie_title = a_tag.text
    #movie_title = a_tag.contents[0]
    movie_code = a_tag['href'].split('code=')[1]
    # split 사용하지 않고 가져오기
    # link = a_tag['href']
    # movie_code = link[link.find('code=') + len('code='):]

    movie_data = {'title': movie_title, 'code': movie_code}

    final_movie_data.append(movie_data)

for movie in final_movie_data:
    headers = {
        'authority': 'ssl.pstatic.net',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'image',
        'referer':
        'https://movie.naver.com/css/deploy/movie.all.css?20200629181825',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie':
        'NNB=T7454BSC7T7F4; ASID=d3b1f8af000001731f00928c00000067; _fbp=fb.1.1594085038941.1217611085; NRTK=ag#20s_gr#0_ma#-2_si#-2_en#-2_sp#-2; _ga=GA1.1.335975588.1594080211; _ga_4BKHBFKFK0=GS1.1.1595209449.1.1.1595209455.54; MM_NEW=1; NFS=2; MM_NOW_COACH=1; nx_ssl=2; page_uid=UyoeclprvxZssOykSr0ssssstfo-482649; BMR=s=1596593997073&r=https%3A%2F%2Fm.blog.naver.com%2Fdemonic3540%2F221229805234&r2=https%3A%2F%2Fwww.google.com%2F',
        'Referer': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=189069',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'charset': 'utf-8',
        'x-requested-with': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Connection': 'keep-alive',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'image',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'pragma': 'no-cache',
    }

    params = (('code', '{movie_code}'), )

    response = requests.get('https://movie.naver.com/movie/bi/mi/basic.nhn',
                            headers=headers,
                            params=params,
                            cookies=cookies)

    # 웹 전반을 이해하며, api를 가로채는 작업을 해봅시다
    # api : end-point를 미리 만들어놓고 바로 통신할 수 있게
    # 요청과 응답을 할 때 end-point를
    # 우리가 클릭으로 해야하는 일들을 api를 통해 처리할 수 있다고 생각하기

# 웹이 동작하는 방식에 대한 규칙 HTTP
# Headers : 요청에 대한 약속, 형식, 규칙등이 담긴다
# -Request URL :요청 보내는 URL (IP를 가리키는 도메인)
# -Request Method : GET / POST
# -Status Code : 요청에 대한 응답 -> 200(성공)
# -Remote Address : IP(HOST 주소)
# -HOST : 네트워크에 연결되어있는 컴퓨터들
# -:443 : PORT 의 종류 (https = 443 PORT)
# -Referrer Policy : HTTP 헤더중의 하나로, 방문 직전에 위치했던 페이지
#      no-referre : 헤더에 referre을 포함시키지 않겠다 : 어디서 들어오던지 상관없다
#      결제 시스템등 step이 있어야하는 과정에서 referre이 필요
