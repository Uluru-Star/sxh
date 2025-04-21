import requests

# 请求的 URL
url = 'http://jwxt.sit.edu.cn/jwglxt/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html?gnmkdm=N253512'

# 请求头
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "JSESSIONID=96D15E81087B6F39AAA7211720EA872B; route=62840941afd9737ac1eb7a4f6c551618; iPlanetDirectoryPro=TOfv6Nguipq2STagdjsZVQ",
    "referer": "http://jwxt.sit.edu.cn/jwglxt/xsxk/zzxkyzb_cxZzxkYzbIndex.html?doType=details&gnmkdm=N253512&layout=default",
    "referrer-policy": "strict-origin-when-cross-origin"
}

# 请求体的内容，修正为正确的键值对格式
data = {
    'jxb_ids': '1febdaeddc23c0d091eff5e3867447f19f535fe9e9e18360f297d78a6528cc91a4875a0934ad1247cb8d8c3cfcff1de502f19088ca55adcbccc0e894cad96ed14729b3c803cf954bb3134f972fec8d48419055e60bc63d17af90930f76b115b184c5e9d7409cda19e6d879214526f36f90100359986d7b96d525e2309561fff4',
    'kch_id': 'B2035115',
    'kcmc': '(B2035115)%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84+-+3+%E5%AD%A6%E5%88%86',
    'rwlx': '1',
    'rlkz': '0',
    'cdrlkz': '0',
    'rlzlkz': '0',
    'sxbj': '0',
    'xxkbj': '0',
    'qz': '0',
    'cxbj': '0',
    'xkkz_id': '27777E19CD523A5DE065E2219BB20201',
    'njdm_id': '2023',
    'zyh_id': 'B0303',
    'kklxdm': '01',
    'xklc': '1',
    'xkxnm': '2024',
    'xkxqm': '12',
    'jcxx_id': ''
}

# 发送POST请求，并自动处理URL编码
response = requests.post(url, headers=headers, data=data)

# 打印状态码、响应头部和响应内容
print(response.status_code)
print(response.headers)
print(response.text)

# 检查响应状态码
if response.status_code == 200:
    print("请求成功！")
else:
    print(f"请求失败，状态码：{response.status_code}")