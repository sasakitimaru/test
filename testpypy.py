from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = "driver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)
address_list = []
driver.get("https://www.google.com/search?q=%E5%9F%BC%E7%8E%89%E7%9C%8C+%E9%A3%AF%E8%83%BD%E5%B8%82+%E5%85%AC%E5%9C%92&biw=1440&bih=789&tbm=lcl&sxsrf=ALeKk03jnV_UZBh7u8svPaf3ZIb7FtzsuA%3A1620456983102&ei=FzaWYJTiBdOB-Qan84GwBA&oq=%E5%9F%BC%E7%8E%89%E7%9C%8C+%E9%A3%AF%E8%83%BD%E5%B8%82+%E5%85%AC%E5%9C%92&gs_l=psy-ab.3..38l4.26454.29023.0.29742.13.11.0.0.0.0.274.1485.0j3j4.7.0....0...1c.1j4.64.psy-ab..10.3.690...0j35i39k1j0i433i131k1j0i7i30k1j0i13i30k1.0.u4MqzK9XzyA#rlfi=hd:;si:;mv:[[35.860475699999995,139.34730600000003],[35.8288892,139.29101459999998]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:1")
#flag = True
#start = time.time()
#a = driver.find_elements_by_class_name("section-layout section-scrollbox mapsConsumerUiCommonScrollable__scrollable-y mapsConsumerUiCommonScrollable__scrollable-show mapsConsumerUiSubviewSectionLayout__section-layout-flex-vertical")
#driver.execute_script("window.scrollTo(0,1000)")
"""
while flag == True:
   #無限ループしないために、念のため時間経過でbreak
   if time.time() - start < 20:

      #JavaScriptメソッドで、要素を指定しつつスクロール処理
      startHeight = driver.execute_script("var startHeight = document.getElementsByClassName('section-layout section-scrollbox mapsConsumerUiCommonScrollable__scrollable-y mapsConsumerUiCommonScrollable__scrollable-show mapsConsumerUiSubviewSectionLayout__section-layout-flex-vertical')[0].scrollTop; return startHeight")
      lastHeight = 1000#driver.execute_script("var lastHeight = document.getElementsByClassName('section-layout section-scrollbox mapsConsumerUiCommonScrollable__scrollable-y mapsConsumerUiCommonScrollable__scrollable-show mapsConsumerUiSubviewSectionLayout__section-layout-flex-vertical')[0].scrollHeight; return lastHeight")
      driver.execute_script("document.getElementsByClassName('section-layout section-scrollbox mapsConsumerUiCommonScrollable__scrollable-y mapsConsumerUiCommonScrollable__scrollable-show mapsConsumerUiSubviewSectionLayout__section-layout-flex-vertical')[0].scrollTop = 1000;")
#document.getElementsByClassName('section-layout section-scrollbox mapsConsumerUiCommonScrollable__scrollable-y mapsConsumerUiCommonScrollable__scrollable-show mapsConsumerUiSubviewSectionLayout__section-layout-flex-vertical')[0].scrollHeight;")

      #最下段までスクロールしたら終了
      if startHeight == lastHeight:
         flag = False
      else:
         flag = True
         time.sleep(3)

   #或いは時間経過でbreak
   else:
      break
"""
#class="mapsConsumerUiSubviewSectionDivider__section-divider mapsConsumerUiSubviewSectionDivider__section-divider-bottom-line"
c=driver.find_elements_by_class_name('mapsConsumerUiSubviewSectionGm2Placesummary__title-container')
for i in c:
    print(i.text)
#print(c[7].text)
time.sleep(5)
driver.close()
