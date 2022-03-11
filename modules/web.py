import time
import requests
import re
from UA池 import ua
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Download:
    def __init__(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=option)

    def search(self, keyword):
        url = 'https://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=' + keyword
        self.driver.get(url)
        time.sleep(0.5)
        # 返回搜索结果
        song_name_list = re.findall('<a class="song_name" title="(.*?)"', self.driver.page_source)
        return song_name_list

    def parse_html(self, song_list, index):
        tag = self.driver.find_element(by=By.LINK_TEXT, value=f'{song_list[index]}')
        tag.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # 返回要下载歌曲的网页代码
        return self.driver.page_source

    def run(self, song_list, index):
        html = self.parse_html(song_list, index)
        audio_link = re.findall('<audio class="music" id="myAudio" src="(.*?)"', html)[0]
        title = re.findall('<span class="audioName" title="(.*?)">', html)[0]

        with open(f'{title}.MP3', 'wb') as f:
            f.write(requests.get(url=audio_link, headers=ua(3)).content)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])
