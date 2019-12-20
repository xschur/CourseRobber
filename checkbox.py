# -*- encoding:utf-8 -*-
# author:schur

import requests
from bs4 import BeautifulSoup
import json

course_list = []
json_format = {
    'checkbox' : '',
    'cname' : '',
    'type0' : '',
    'teacher' : '',
    'grade' : '',
    'when' : ''
}

burp0_url = "https://dean.bjtu.edu.cn:443/course_selection/courseselecttask/selects_action/?kch=&kxh=&kclbdm=&kzm=&action=load&order=&iframe=school&submit=&has_advance_query=&page={}"
burp0_cookies = {"UM_distinctid": "", "sessionid": "", "csrftoken": ""}
burp0_headers = {"Connection": "close", "Upgrade-Insecure-Requests": "1", "DNT": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3833.144 Safari/537.36", "Sec-Fetch-User": "?1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "nested-navigate", "Referer": "https://dean.bjtu.edu.cn/course_selection/courseselecttask/selects_action/?action=load&iframe=school", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7"}
#requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

def page_info(i):
    url = burp0_url.format(str(i))
    res = requests.get(url, headers=burp0_headers, cookies=burp0_cookies).text
    soup = BeautifulSoup(res, 'html5lib')
    course = soup.find_all('tr')[1:]
    for j in course:
        try:
            info = j.find_all('input')
            checkbox = info[0].get('value')
            info = j.find_all('td')
            cname = info[2].text
            type0 = info[4].text
            grade = info[6].text
            teacher = info[8].text
            when = info[9].text
            data = {}
            data['checkbox'] = checkbox
            data['cname'] = cname
            data['type0'] = type0
            data['teacher'] = teacher
            data['grade'] = grade
            data['when'] = when
            print(data)
            course_list.append(data)
        except Exception as err:
            print(str(err))
            print(j)
            continue



def main():
    for i in range(1,54):
        page_info(i)
    with open('course.json', 'a') as f:
        json.dump(course_list,f)

if __name__ == '__main__':
    main()