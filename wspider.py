# -*- coding: utf-8 -*-
# author:mistchan

import requests
from urllib.parse import urlencode
import re
import pandas as pd

drug = {
    '卡培他滨': '128074',
    '替吉奥': '126470'

}

url_post = 'http://14.215.129.81:8082/BaseInfo/ashx/QuestionHandler.ashx'
url_get = 'http://14.215.129.81:8082/ashx/loginhandler.ashx?'

param = {
    'username': 'ds11995',
    'password': '123'
}
url = url_get + urlencode(param)
header1 = {
    'Host': '14.215.129.81:8082',
    'Referer': 'http://14.215.129.81:8082/welcome.html',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/79.0.3945.117 Safari/537.36'
}
header2 = {
    'Host': '14.215.129.81:8082',

    'Referer': 'http://14.215.129.81:8082/welcome.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/79.0.3945.117 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/json'
}

session = requests.Session()
login = session.get(url, headers=header1)
r = session.post(url_post, headers=header2, data=login.json())

header4 = {
    'Host': '14.215.129.81:8082',

    'Referer': 'http://14.215.129.81:8082/DataFlow/DataFlowDetails.aspx?navid=42',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',

}
url_check = 'http://14.215.129.81:8082/DataFlow/ashx/DataFlowHandler.ashx'
data_ch = {
    'filter': ' {"BeginDate":"2019-07-01","endDate":"2020-01-14","ItemId":128074}',
    'page': '1',
    'rows': '20',
}

r_result = session.post(url_check, headers=header4, data=data_ch)
row_ = r_result.text[9:11]
a='2019-07-01'
data_ch = {
    'filter': ' {{"BeginDate":"{}","endDate":"2020-01-14","ItemId":128074}}'.format(a),
    'page': '1',
    'rows': row_,
}

r_result = session.post(url_check, headers=header4, data=data_ch)

result_str = re.sub(r'null', '\'\'', r_result.text)
filename = ''
result_dirt = eval(result_str)
print(result_dirt)
# df = pd.DataFrame(result_dirt['rows'])
# summary = df.pivot_table(['itemQty'], index=['customerName'], columns=['itemCurName', 'billtypename'], aggfunc=sum,
#                          fill_value=0)
# writer = pd.ExcelWriter('{}.xlsx'.format(filename))
# df.to_excel(writer, sheet_name='明细', index=False)
# summary.to_excel(writer, sheet_name='统计')
# writer.save()
