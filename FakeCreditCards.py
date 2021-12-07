import random
import names
from selenium.webdriver import Chrome
import time

PATH = '/Users/aziz/PycharmProjects/scrapingAnime/chromedriver' # where your chorme Driver is
url = "https://bilgimabedi.com/azer/us/index2.php" # the website to fill with data
driver = Chrome(PATH)
driver.get(url)


def get_visa(n):
	visa_prefix = ["4539", "4556", "4916", "4532", "4929", "4485", "4716"]
	visa_numbers = []
	for _ in range(n):
		rand_prefix = random.choice(visa_prefix)
		rand_number = str(random.randint(313243213432, 999999999999))
		full_number = rand_prefix + rand_number
		visa_numbers.append(full_number)
	return visa_numbers


def ccv(n):
	ccv_list = []
	for _ in range(n):
		ccv_number = str(random.randint(100, 978))
		ccv_list.append(ccv_number)
	return ccv_list


def full_names(n):
	full_name = []
	for _ in range(n):
		full_names = names.get_full_name()
		full_name.append(full_names)
	return full_name


VISA = get_visa(1)
CCV = ccv(1)
NAME = full_names(1)
print(NAME, VISA, CCV)

## code below only works for a specifc site. Change the XPATHS
for i in range(1000):
	rand_month = random.randint(1, 12)
	rand_year = random.randint(5, 13)

	card_holder = driver.find_element_by_xpath('//*[@id="card-holder-name"]').send_keys(NAME[i])
	card_number = driver.find_element_by_xpath('//*[@id="taddress"]').send_keys(VISA[i])
	CVV_number = driver.find_element_by_xpath('//*[@id="tcity"]').send_keys(CCV[i])
	MONTH = driver.find_element_by_xpath(f'//*[@id="tmonth"]/option[{rand_month}]').click()
	YEAR = driver.find_element_by_xpath(f'//*[@id="tyears"]/option[{rand_year}]').click()
	submit = driver.find_element_by_xpath('//*[@id="a-address-step1"]').click()
	driver.back()
	CVV_clear = driver.find_element_by_xpath('//*[@id="tcity"]').clear()
	card_clear = driver.find_element_by_xpath('//*[@id="taddress"]').clear()
	time.sleep(1)
driver.quit()
