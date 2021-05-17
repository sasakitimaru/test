from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = "driver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)
address_list = []
driver.get("https://www.google.com/maps/search/%E5%85%A5%E9%96%93%E5%B8%82%E3%80%80%E5%85%AC%E5%9C%92/@35.831455,139.3681826,14z/data=!3m1!4b1")
flag = True
start = time.time()

while flag == True:
   #無限ループしないために、念のため時間経過でbreak
   if time.time() - start < 20:

      #JavaScriptメソッドで、要素を指定しつつスクロール処理
      startHeight = driver.execute_script("var startHeight = 0; return startHeight")
      lastHeight = driver.execute_script("var lastHeight = 1000; return lastHeight")
      driver.execute_script("document.getElementsByClassName('mapsConsumerUiSubviewSectionDivider__section-divider mapsConsumerUiSubviewSectionDivider__section-divider-bottom-line')[0].scrollTop = document.getElementsByClassName('mapsConsumerUiSubviewSectionDivider__section-divider mapsConsumerUiSubviewSectionDivider__section-divider-bottom-line')[0].scrollHeight;")

      #最下段までスクロールしたら終了
      if startHeight == lastHeight:
         flag = False
      else:
         flag = True
         time.sleep(3)

   #或いは時間経過でbreak
   else:
      break
#class="mapsConsumerUiSubviewSectionDivider__section-divider mapsConsumerUiSubviewSectionDivider__section-divider-bottom-line"
c=driver.find_elements_by_class_name('mapsConsumerUiSubviewSectionGm2Placesummary__title-container')
for i in c:
    print(i.text)
#print(c[7].text)
time.sleep(5)
driver.close()
