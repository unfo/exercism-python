def add_gigasecond(dtm):
	from datetime import timedelta
	return dtm + timedelta(seconds=1000000000)
