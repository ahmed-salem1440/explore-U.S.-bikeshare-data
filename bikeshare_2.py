import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#craeting months lists and week days list in glopal scope
months=['january', 'february', 'march', 'april', 'may', 'june']
WeekDays = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Please type one of the following cities: chicago, new york city or washington: ').lower()
        if city not in CITY_DATA:
            print('please only type one of this words (chicago, new york city, washington )')
        else:
            break


    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please type a month from the first half of the year or type \'all\' to display all those months:').lower()
        if month not in months and month != 'all':
            print ('please only type one of this words(january, february, march, april, may, june,all) ')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please type a day of the week to display the data of that day or type all to display the data of all days:').lower()
        if day not in WeekDays and day != 'all':
            print('please only type one of this words(saturday, sunday, monday, tuesday, wednesday, thursday, friday,all)')
        else:
            break
    print('-'*40)
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
    #loading the city data file into a data frame using pandas
    df = pd.read_csv(CITY_DATA[city])
    #reading the start date/time data from Start Time column using to_date function in pandas and save it to the same column
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #creating 2 new columns one for the month and another one for the day of the week and both are from Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    #feltring month/s depends on user input
    if month != 'all':
        #returning the month value to the int. value using the months list index
        month = months.index(month)+1
        #refill the data frame with the new filtered by month values
        df=df[df['month']==month]
    #feltring week day/s depends on user input
    if day != 'all':
        #refill the data frame with the new filtered by month and week day values
        df=df[df['day']==day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #start calculating time by time library and .time() function
    start_time = time.time()
    #get the most common month by .mode() method and save it into a new variable
    MostCommonMonth = df['month'].mode()[0]
    # display the most common month
    print('The most common month is:',months[MostCommonMonth-1])#-1 for zero indixing
    #get the most common day by .mode() method and save it into a new variable
    MostCommonDay = df['day'].mode()[0]  
    # display the most common day of week
    print('The most common day is:',MostCommonDay)
    #craeting a new column "hour" and get its values form Start Time column using pandas and to_datetime function
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    #get the most common hour by .mode() method and save it into a new variable
    MostCommonHour = df['hour'].mode()[0]
    # display the most common start hour
    print('The most common hour is:',MostCommonHour)
    #calculate the time duration and display it
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #start calculating time by time library and .time() function
    start_time = time.time()
    #get the most commonly used start station and save it into a new variable
    MostCommonStartStation = df['Start Station'].mode()[0]
    # display most commonly used start station
    print('The most commonly start station used is:',MostCommonStartStation)
    #get the most commonly used end station and save it into a new variable
    MostCommonEndStation =  df['End Station'].mode()[0]
    # display most commonly used end station
    print('The most commonly end station used is:',MostCommonEndStation)
    #get the combination of start station and end station trip
    Combination = pd.DataFrame('from'+ df['Start Station'] + 'to' + df['End Station'])
    #get the most frequent combination of start station and end station trip
    MostCombination = Combination.mode()[0]
    # display most frequent combination of start station and end station trip
    print('The most common combintation is:',MostCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    #start calculating time by time library and .time() function
    start_time = time.time()
    #calculate the total travel duration and save it into a new variable
    TotalTravelDuration = df['Trip Duration'].sum()
    # display total travel time
    print('The total trip duration is : ',TotalTravelDuration,'seconds.')
    #calculate the average travel duration
    AverageDuration = df['Trip Duration'].mean()
    # display mean travel time
    print('The average travel time is :',AverageDuration,'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    #start calculating time by time library and .time() function
    start_time = time.time()

    # Display counts of user types
    print('The counts of user types is:\n',df['User Type'].value_counts())
    
    # Display counts of gender
    #because some cities may have no 'Gender'column, we use if statements to avoid errors
    if 'Gender' in df:
        print('The counts of gender is:\n',df['Gender'].value_counts())
    # calculate earliest, most recent, and most common year of birth
    #because some cities may have no 'Birth Year'column, we use if statements to avoid errors
    if 'Birth Year' in df:
        #calculate the earliest, most recent, and most common year of birth by .min() , .max() and .mode() method
        #we  use int() function because the defult is float so result will be float so we use int() function 
        EarliestBirthYear = int(df['Birth Year'].min())
        MostRecentBirthYear = int(df['Birth Year'].max())
        MostCommonBirthYear = int(df['Birth Year'].mode()[0])
        # display earliest, most recent, and most common year of birth, we use int() function bacause the defult is float
        print('The earliest year of birth is: ',int(EarliestBirthYear))
        print('The most recent year is: ',int(MostRecentBirthYear))
        print('The most common year of birth is:',int(MostCommonBirthYear))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def DisplayRaws(df):
    #This function displays 5 raws from the data set according to user answer
    #get the user input, .lower()method to avoid errors
    UserInput = input('type "yes" if you want to display the first 5 raws from data set, else type "no"').lower()
    i=0
    while True:
        if UserInput != 'yes' and UserInput != 'no':
            UserInput = input('please type only "yes" or "no".')
        if UserInput == 'no':
            break
        if UserInput == 'yes':
            print(df[i:i+5])
            i+=5
            UserInput = input('do you like to display the next 5 raws? please type yes/no..').lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        DisplayRaws(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
