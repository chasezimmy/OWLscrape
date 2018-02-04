#!/usr/bin/env python3
from selenium import webdriver
from schedule import schedule


def main():
	driver = webdriver.PhantomJS()

	schedule.match_schedule_current(driver) # Current week match schedule

	driver.quit()


if __name__ == '__main__':
	main()