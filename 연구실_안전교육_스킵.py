import requests


def skip(target, page, gapTime, content_length):

    login_cookie = "29471636583429471306294717123456789012345678912345678901234567891234567890123456789123456789012345678912345678901234567890123456789012345678901234567890123456789012345566778991234567890123456789"
    j_session = "DDDDDDDDDDDDDDDDDDDDDDD"
    smMemberNo = 123456

    url = 'https://safety.konkuk.ac.kr/ushm/edu/SetImgtechContents2019AfterVersionProcessUpdate.do'
    headers = {
        'Host': 'safety.konkuk.ac.kr',
        'Connection': 'keep-alive',
        'Content-Length': f'{content_length}',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://safety.konkuk.ac.kr',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://safety.konkuk.ac.kr/resources/contents/IMGT2023/209/02.html?passedPage={page-1}&checkurl={page}&smProgressNo={target}&smMemberNo={smMemberNo}',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': f'Login=; UTF8_Option=0; LoginCookie={login_cookie}; JSESSIONID={j_session}; edumaruVolume=0.5'
    }
    data = {
        'scheduleMemberProgressNo': f'{target}',
        'watchedpage': f'{page}',
        'gapTime': f'{gapTime}'
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    print(response.content)

for content_length in [56, 57, 58, 59]:
    for page in range(20):
        skip(654350, page, 300, content_length)
