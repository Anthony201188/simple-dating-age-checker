from datetime import datetime, timedelta

def get_user_age(date_of_birth): 
    Dob = datetime.strptime(date_of_birth , "%d-%m-%Y" )
    num_of_days = datetime.now() - Dob
    one_year = timedelta(days=365.2425)
    age = num_of_days / one_year
    return age


print(get_user_age("10-10-1980"))
