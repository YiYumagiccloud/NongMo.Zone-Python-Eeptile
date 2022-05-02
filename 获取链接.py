import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from tqdm import tqdm

from Tools.工具 import 创建文件夹

UA = {"User-Agent": UserAgent().random}

默认 = 'https://www.ilovexs.com/'

输入 = input('链接路径 :').split(' ')

for 路径 in 输入:

    网页 = requests.get(f'{默认}{路径}', headers=UA).text

    对象 = BeautifulSoup(网页, 'lxml')

    写真名 = 对象.select(".entry-content p")[0].string

    链接 = [i['src'] for i in 对象.select(".entry-content div a img")]

    去重链接 = list(filter(None, sorted(set(链接), key=链接.index)))

    创建文件夹('NongMo', f'{写真名}')

    print(f' - 开始下载 {写真名}, 共{len(去重链接)}张 - ')
    print()

    for 几, 下载链接 in enumerate(tqdm(去重链接,  desc='下载进度', ncols=69), start=1):

        图片 = requests.get(下载链接, headers={"User-Agent": UserAgent().random}, stream=True)

        with open(f'D:\\图片\\爬到的图片\\NongMo\\{写真名}\\第{几}张.png', 'wb') as F:

            for 数据 in 图片.iter_content(16):

                F.write(数据)
    print()
    print(f' - {写真名}, {len(去重链接)}张, 下载完成 - ')
