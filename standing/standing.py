from selenium import webdriver
import time

def main():
	driver = webdriver.PhantomJS(service_log_path='../log/ghostdriver.log')
	URL = 'https://overwatchleague.com/en-us/standings'
	driver.get(URL)
	time.sleep(10)
	table = driver.find_element_by_id('standings')
	
	for n in table.find_elements_by_xpath("//tr"):
		print(n.get_attribute('innerHTML'))

		print('=======')

	driver.quit()

if __name__ == '__main__':
	main()