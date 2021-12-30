import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago':'chicago.csv','new york city':'new_york_city.csv','washington':'washington.csv'}
#I have made the month list items data write a string, because I want to put the word 'all' and handle case so that there are no errors due to unexpected input.and the same with day.
MONTHS={'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6,'all':'all'}
DAYS=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
city=""
month=""
day=""



def get_filters():
    
    """
    Take inputs from the user(city,month and day)
    Returns the entered city, month, and day values after being validated
    
    """
    
    city=input("Enter a city: ").lower()
    while city not in  CITY_DATA:
        city=input("Invalid city.These are the available cities chicago,new york city and washington.please choose from them: ").lower()
        
    month=""    
    while month  not in  MONTHS:   
        month=input('Enter a month (Enter all for no filter by month): ').lower()
        
    day=""   
    while day not in DAYS:    
        day=input("Enter a day (Enter all for no filter by day): ").lower()

    print('-'*40)
    return( city, month, day)


def load_data(city, month, day): 
    
    """
    load the data ,Create some extra columns and filter data. 
    It returns the filtered data.
    
    """ 
    #load the data
    data = pd.read_csv(CITY_DATA[city])
    data['Start Time']=pd.to_datetime(data['Start Time'])
    
    #Create some extra columns
    data['month']=data['Start Time'].dt.month
    data['day_of_week'] =data['Start Time'].dt.day_name()
    data['hour']=data['Start Time'].dt.hour
    data["trip"]=' {} ===>> {}'.format( data["Start Station"] , data["End Station"] ) 
    
    #I want multiple filter options per day, month, or both.
    if month !='all':
        data = data[data['month'] == MONTHS[month]]
        
    if day !='all':
        data = data[data['day_of_week'] == day.title()]
    return data



def time_stats(data):
    
    """Shows statistics for the month with the most bike trips, as well as the day and hour"""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_hour=data['hour'].mode() 
    print('most common hour is:\n{}'.format(common_hour))
    
    #Because I want to execute this code when there is no filter for the month or for the day, I used conditional commands.
    if month == 'all' :
        common_month=data['month'].mode()
        print('most common month/s : {}'.format(common_month))

    if day == 'all' :              
        common_day=data['day_of_week'].mode()                  
        print('most common day/s : {} '.format(common_day))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_popular_startstation=data['Start Station'].mode()
    print('most popular start station:\n{}'.format(most_popular_startstation))
    
    most_popular_endstation=data['End Station'].mode()
    print('\nmost popular end station:\n{}'.format(most_popular_endstation))
    
    most_popular_trip=data["trip"].mode()          
    print('\nmost popular trip:\n{} '.format(most_popular_trip))    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(data):
    """Displays some statistics about Duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time=data["Trip Duration"].sum()
    print( 'total travel time is: {}'.format(total_travel_time))
    
    avrage_travel_time=data["Trip Duration"].mean()
    print('avrage travel time is: {} '.format(avrage_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type=data['User Type'].value_counts()
    print('user types are:\n{}'.format(user_type)) 
    
    #Since there is no gender cell and year of birth in the washington city data, I use the try and except methods.
    try:
        count_of_gender=data['Gender'].value_counts()
        print('\ncount_of_genders:\n{}'.format(count_of_gender))
        
        most_common_yearofbirth=data['Birth Year'].mode()
        print('\nmost common year of birth:{}'.format(most_common_yearofbirth))
        
        most_earliest_yearofbirth=data['Birth Year'].max()
        print('\nearliest year of birth:{}'.format(most_earliest_yearofbirth))
        
        most_recent_yearofbirth=data['Birth Year'].min()      
        print('\nmost recent year of birth:{}'.format(most_recent_yearofbirth))
        
    except:
        print("\nno data for gender and birth day in Washington ")

        
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
     
        
        
def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)
        
        time_stats(data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(data)
        
        n=5
        x=0
        lingth=data.size
        while  n < lingth : 
            show_data=input('\nWould you like to see some data y or n.\n').lower() 
            if show_data == 'y':
                print(data.iloc[x:n])
                n+=5   
                x+=5
            else: break
        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
               break


if __name__ == "__main__":
	main()