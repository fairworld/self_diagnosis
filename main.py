from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

url = 'https://hcs.eduro.go.kr/#/loginHome'

# 변수선언
region = '경기도'
school_type = '초등학교'
school_name = '동암초'
name = '정은찬'
birth = '120613'
password = '0613'


options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('windows-size=1920x1080')
options.add_argument('disable-gpu')
# 혹은 options.add_argument("--disable-gpu")

# Headless Chrome에서 이미지 로딩을 막기 위한 설정
# prefs = {'profile.managed_default_content_settings.images': 2}
# options.add_experimental_option('prefs', prefs)

# UserAgent값을 바꿔줍시다!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR") # 한국어!

# 유의: chromedriver를 위에서 받아준
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!
driver = webdriver.Chrome('Selenium\\chromedriver.exe', options=options)

driver.get('about:blank')
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

driver.get(url)
driver.implicitly_wait(5)

link = '//*[@id="btnConfirm2"]'

driver.find_element_by_xpath(link).click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/button').click()

select = Select(driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select'))
select.select_by_visible_text(region)

select = Select(
    driver.find_element_by_xpath('// *[ @ id = "softBoardListLayer"] / div[2] / div[1] / table / tbody / tr[2] / td / select'))
select.select_by_visible_text(school_type)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys(school_name)
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p/a').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(name)
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/input').send_keys(birth)
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/input').send_keys(Keys.ENTER)

driver.find_element_by_xpath("//input[@title='비밀번호']").send_keys(password)
driver.find_element_by_xpath("//input[@value='확인 / Confirm']").click()

time.sleep(1)
driver.find_element_by_xpath("//button[@class='btn']").click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label').click()
driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label').click()

driver.find_element_by_xpath("//input[@value='제출 / Submit']").click()
