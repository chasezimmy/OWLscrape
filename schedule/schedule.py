import json
from selenium.common.exceptions import NoSuchElementException


def get_match_start(div):
	date = {'date': None, 'day': None}
	try:
		date['date'] = div.find_element_by_class_name('Date-monthAndDay').text
	except NoSuchElementException:
		pass

	try:
		date['day'] = div.find_element_by_class_name('Date-dayOfWeek').text
	except NoSuchElementException:
		pass

	return date


def get_match_teams(div):
	return {'home': div[0].text, 'away': div[1].text}


def get_match_score(div):
	try:
		return {'home': div[0].text, 'away': div[2].text, 'winner': 'home' if div[0].text > div[2].text else 'away'}
	except IndexError:
		return {'home': 0, 'away': 0, 'winner': None}


def get_stage_week(div):
	
	try:
		stage = div[0].text
	except IndexError:
		stage = ""

	try:
		week = div[1].text
	except IndexError:
		week = ""

	return  {'stage': stage, 'week': week}


def save(matches, current_round):
	file = "{} - {}.json".format(current_round['stage'], current_round['week'])
	with open(file, 'w') as fp:
		json.dump(matches, fp)


def match_schedule_current(driver):
	URL = "https://overwatchleague.com/en-us/schedule"
	driver.get(URL)
	matches = {}

	current_round = get_stage_week(driver.find_elements_by_class_name('Tabs-tab--active'))

	for schedule in driver.find_elements_by_class_name('MatchSchedule'):

		date = get_match_start(schedule)

		for match in schedule.find_elements_by_class_name('MatchRow-contentWrapper--hover'):
			match_id = match.get_attribute('href').partition("/match/")[-1]
			teams = get_match_teams(match.find_elements_by_class_name('TeamLabel-info--noScore'))
			score = get_match_score(match.find_elements_by_class_name('MatchStatus-score'))

			matches[match_id] = {
				'teams': teams,
				'score': score,
				'winner': score['winner'],
				'date': date
			}

	save(matches, current_round)
