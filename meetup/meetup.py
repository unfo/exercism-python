from datetime import date, timedelta

def meetup_day(year, month, day, qualifier):
	all_days = get_days_by_name(year, month, day)
	indexes = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1 }

	if qualifier in indexes:
		return all_days[indexes[qualifier]]
	elif qualifier == "teenth":
		return [t for t in all_days if 12 < t.day < 20][0]
	else:
		raise ArgumentError(qualifier)

	return meet

def get_days_by_name(year, month, dayname):
	days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
	meet = date(year, month, 1)
	selected_days = []
	one_day = timedelta(days=1)
	while meet.month == month:
		if meet.isoweekday() == days[dayname]:
			selected_days.append(meet)
		meet += one_day
	return selected_days