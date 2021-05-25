import time
import pandas as pd
import numpy as np
'''
Resources used to achive That script:
*-practice Problem 1,2,3

*-https://stackoverflow.com/questions/3395138/using-multiple-arguments-for-string-formatting-in-python-e-g-s-s

*-https://www.w3schools.com/python/python_ml_mean_median_mode.asp

*Honestly i have checked several GitHub repBositries to build User_stats function

* i checked the discourse forum

*https://appdividend.com/2019/01/25/pandas-boolean-indexing-example-python-tutorial/#:~:text=Pandas%20boolean%20indexing%20is%20a,column%20labels%20or%20integer%20locations.
'''
#Global Variables
#I have used Cities,months,days lists to  avoid typos
#And also to use them in other functions to shorten my codes
cities = ['ch','nyc','wa']
months = ['all', 'jan', 'feb', 'mar', 'apr', 'may', 'jun']
days = ['sat', 'sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'all']

CITY_DATA = { 'ch': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filt0er by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please enter one of the Availble cities, Enter ch for Chicago, nyc For New York City , wa For Wahington : ')
        city = city.lower()
        if city in cities:
            print('You Have picked : ' + city)
            break
        else:
            print('Please enter a valid city ch,nyc or wa ')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please pick a month using intials mar for March feb for february: ')
        month = month.lower()
        if month in months:
            print('you have chose ' + month)
            break
        else:
            print('please enter a valid month or all...')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day by entering the first 3 letters of any day sat for saturday or choose all of the days by entering all : ')
        #day = day.lower()
        if day in days:
            print('you have picked ' + day)
            break

        else:
            print('please enter a valid day...')

    print('-_- ,'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading the csv files into pandas dataframes by using the ch,nyc,wa abreviations
    #This block of code I got from problemset 3 ;)

   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    #day_name() -- dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #I used Stackover flow
    #https://stackoverflow.com/questions/43120291/most-frequent-occurence-in-a-pandas-dataframe-indexed-by-datetime
    #to get .idmax() but it s not working tho it worked in the problemset
    # TO DO: display the most common month .idxmax(),.mode(),df.iloc[df['column_name'].idxmax()],dataframe['name'].value_counts().argmax()
    com_month = df['month'].value_counts().idxmax()
    print('The Most Common Month is : ' + str(com_month))

    # TO DO: display the most common day of week
    com_day = df['day_of_week'].value_counts().idxmax()
    print('The most Common day of week : ' + str(com_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].value_counts().idxmax()
    print('The Most Common Start Hour is : ' + str(com_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #i will use the Mode[0] method from problem set1 solution for change of idmax() as a change in the code :)
    st_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is : ' + st_station)

    # TO DO: display most commonly used end station
    en_station = df['End Station'].value_counts().idxmax()
    print('Most comman end station is : ' + en_station)

    # TO DO: display most frequent combination of start station and end station trip
    freq_comb =  (df['Start Station'] + " *** " + df['End Station']).mode()[0]
    print('The most frequant combination start & end stations trip : ' + freq_comb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltime = df['Trip Duration'].sum()
    print('The Total travel Time = ' + str(totaltime))

    # TO DO: display mean travel time
    meantime = df['Trip Duration'].mean()
    print('Mean travel time is : ' + str(meantime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userscount = df['User Type'].value_counts().idxmax()
    print(userscount + 'This is the counts of the user types')

    # TO DO: Display counts of gender
    #only chicago and new york has the gender info
    for city in cities:
        if "Gender" in df.columns:
            #df.groupby(['Gender'])['Gender'].count()
            #df['Gender'].value_counts()
            gender = df['Gender'].value_counts().idxmax()
            print("counts of genders : " + gender)
        else:
            print('No Gender info avalible for wa city ')    
        # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            old = df['Birth Year'].min()
            young = df['Birth Year'].max()
            common = df['Birth Year'].mode()[0]
            print('Oldest riders are {}, while the Youngest are {} and those who came the same year {} '.format(old, young, common))
            
        else:
            print('no birth information availible for that city') 

               


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea','yeah','yup'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df[0:3])

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
