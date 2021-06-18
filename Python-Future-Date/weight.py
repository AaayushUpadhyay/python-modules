import datetime

current_weight = 220
goal_weight = 216
avg_lbs_week = 2

start_date=datetime.date.today()
print(start_date)
end_date=start_date
while current_weight>goal_weight:
	end_date = end_date + datetime.timedelta(days=7)

	current_weight=current_weight-avg_lbs_week
	
print(end_date)
print((end_date-start_date).days//7)