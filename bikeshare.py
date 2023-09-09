import time
from unittest import expectedFailure
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' } 
months = ['january', 'february','fab',
              'march',
              'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday','wednesday','thursday','friday','saturday','all'] 


def get_filters():
 
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input('Choose a city name: {chicago, new york city, washington}: ' ).lower()

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while city not in CITY_DATA.keys():
        print('Enter a valid city, please: ')
        city = input('Choose a city name: {chicago, new york city, washington}; ' ).lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    
    while True:    
         month = input('choose month: (all, january, february , march , april , may ,june): ').lower()
         if month in months:
             break
         else:
             print('unexpected/invalid input!')
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('choose a day: ').lower()
        if day in days:
            break
        else:
            print('unexpected/invalid input!')
                
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
 
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])                                   
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name  
    df['start hour'] =df['Start Time'].dt.hour
                                      
    if month != 'all':
        months = ['january', 'febuary', 'march', 'april','may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]    
        
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
 
    
    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is:     {}'.format(df['month'].mode()[0]))
    
    # TO DO: display the most common day of week   
    print('the most common day is:  {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour     
    print('the most common start hour is : {}'.format(df['start hour'].mode()[0]))                                                                 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common used start station: {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('the most common used end station: {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+","+df['End Station']
    print('the most common route is: {} '.format(df['route'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ',(df['Trip Duration'].sum()).round())


    # TO DO: display mean travel time
    print('average travel time: ',(df['Trip Duration'].mean()).round())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_info(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())


    # TO DO: Display counts of gender
    if city != 'washington': 
            print(df['Gender'].value_counts().to_frame())

        # TO DO: Display earliest, most recent, and most common year of birth
            print('Most common year of birth:',int(df['Birth Year'].mode()[0]))
            print('Most recent year of birth:',int(df['Birth Year'].max()))
            print('Most earliest year of birth:',int(df['Birth Year'].min()))
    else:
        print('there is no data for this city')
       
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    
    

def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_info(df,city)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting........")
            break
        except Exception as e:
            print(str(e))       

if __name__ == "__main__":
	main()
