import requests
from bs4 import BeautifulSoup as soup
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

if __name__ == '__main__':

    # 请求数据, C罗的ID为2371
    url = 'https://understat.com/player/2371'
    html = requests.get(url)

    # 解析处理数据
    parse_soup = soup(html.content, 'lxml')
    scripts = parse_soup.find_all('script')
    strings = scripts[3].string

    ind_start = strings.index("('")+2
    ind_end = strings.index("')")
    json_data = strings[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    data = json.loads(json_data)
    print(data)
    # 处理数据, 包含射门位置、预期进球、射门结果、赛季
    x = []
    y = []
    xg = []
    result = []
    season = []
    for i, _ in enumerate(data):
        for key in data[i]:
            if key == 'X':
                x.append(data[i][key])
            if key == 'Y':
                y.append(data[i][key])
            if key == 'xG':
                xg.append(data[i][key])
            if key == 'result':
                result.append(data[i][key])
            if key == 'season':
                season.append(data[i][key])
    columns = ['X', 'Y', 'xG', 'Result', 'Season']
    df_understat = pd.DataFrame([x, y, xg, result, season], index=columns)
    df_understat = df_understat.T
    df_understat = df_understat.apply(pd.to_numeric, errors='ignore')
    # 得到最终的结果
    print(df_understat)