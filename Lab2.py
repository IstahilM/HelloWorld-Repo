'''
Istahil Mohamed
9/6/24
This program will be calculating human age to dog
'''


human_age = float (input("please enter your age"))
dog_age = human_age * 7
dog_age_days = dog_age * 360
dog_years = dog_age_days // 360
dog_years_remainder = dog_age_days % 360
dog_months = dog_years_remainder // 30
dog_days = dog_years_remainder % 30


print(' Your age in dog years is: ' , dog_years, 'years' , dog_months, 'months' , dog_days, 'days')


'''
Istahil Mohamed
9/6/24
This program will be calculating human age to cat age
'''

human_age = float (input ("please enter your age:"))
cat_age = (human_age / 9)
cat_age_days = cat_age * 360
cat_years = cat_age_days // 360
cat_years_remainder = cat_age_days %360
cat_months = cat_years_remainder //30
cat_days = cat_years_remainder % 30
print(' Your age in cat years is: ', cat_years, 'years' , cat_months, 'months' , cat_days, 'days')


'''
Istahil Mohamed
9/6/24
This program will be calculating humna age to horse age
'''

human_age = float (input ("please enter your age") )
horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)
horse_age_days = horse_age * 360
horse_years = horse_age_days // 360
horse_years_remainder = horse_age_days % 8360
horse_months = horse_years_remainder //30
horse_days = horse_years_remainder % 830
print('Your age in horse years is:', horse_years, 'years', horse_months, 'months', horse_days, 'days')
horse_age__days = horse_age * 360


