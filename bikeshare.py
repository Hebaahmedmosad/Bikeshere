import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}











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
        city=input('choose a city (chicago, new york city or washington)').lower()
        if city not in CITY_DATA:
            print("please choose a correct city")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = input("please choose Month (all, january, ... june)").lower()
        if month not in months and month!='all':
            print('please choose correct month or all month')
        else:
            break



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=input('please choose a weekday or word ( all )for all days').lower()
        if day not in days and day!='all':
            print('please choose correct day or all days')
        else:
            break

    print('-'*40)
    return city, month, day


def raw_data(df):
    i = 1
    answer = input('Would you like to display the first 5 rows of data? yes / no').lower()

    while True:
        if answer == 'no':
            break
        print(df[i:i+4])
        answer = input('Would you like to display another 5 rows of data? yes / no').lower()
        i=i+5



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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = df['month'].mode()[0]

    print('Most Popular Month:', most_month)

    # display the most common day of week
    most_day = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', most_day)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    most_combination_station=df.groupby(['Start Station','End Station'])

    print('Most frequent combination of Start Station and End Station trip:\n', most_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type :')
    print(df['User Type'].value_counts())
    if 'Gender' in df:
        # Display counts of gender
        print('counts of gender:\n',df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:

        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
