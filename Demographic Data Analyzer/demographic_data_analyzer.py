import pandas as pd

def calculate_demographic_data(print_data=True):
    df=pd.read_csv("adult.data.csv")

    # How many people of each race are represented in this dataset? 
    race_count=df["race"].value_counts()

    #What is the average age of men?
    men_average_age=df[df["sex"]=="Male"]["age"].mean()

    #What is the percentage of people who have a Bachelor's degree?
    bacherlor_percentage=df[df["education"]=="Bacherlor"].shape[0]/df.shape[0]

    #What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    #Who is?
    higher_education=df[df["education"].isin(["Bacherlor", "Doctorate", "Masters"])]

    #who isn´t?
    lower_education=df[~df["education"].isin(["Bacherlor", "Doctorate", "Masters"])]

    #Advanced education people who earn more that 50K
    higher_education_higher_than_fifty=higher_education[higher_education["salary"]==">50K"]["salary"].value_counts() / higher_education.shape[0] * 100

    #What percentage of people without advanced education make more than 50K?
    lower_education_higher_than_fifty=lower_education[lower_education["salary"]==">50K"]["salary"].value_counts() / lower_education.shape[0] * 100

    #What is the minimum number of hours a person works per week?
    min_work_hours=df["hours-per-week"].min()

    #What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    #Counting...
    num_min_workers=df[(df["hours-per-week"] == min_work_hours) & df["salary"] == ">50K" ]
    #Calculating percentage
    perc_num_min_workers=((len(num_min_workers)) / len(df) ) * 100

    #What country has the highest percentage of people that earn >50K and what is that percentage?
    high_earn=(df[df["salary"]== ">50K"]["native-country"].value_counts() / df["native-country"].value_counts()) * 100
    highest_earning_country=high_earn.idxmax()
    highest_earning_country_perc=high_earn[highest_earning_country]

    #Identify the most popular occupation for those who earn >50K in India.
    top_india_ocupations = df[df['native-country']=='India']
    top_india_ocupations= top_india_ocupations[top_india_ocupations["salary"]=='>50K']["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", men_average_age)
        print(f"Percentage with Bachelors degrees: {bacherlor_percentage}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_higher_than_fifty}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_higher_than_fifty}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {perc_num_min_workers}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_perc}%")
        print("Top occupations in India:", top_india_ocupations)

    return {
        'race_count': race_count,
        'average_age_men': men_average_age,
        'percentage_bachelors': bacherlor_percentage,
        'higher_education_rich': higher_education_higher_than_fifty,
        'lower_education_rich': lower_education_higher_than_fifty,
        'min_work_hours': min_work_hours,
        'rich_percentage': perc_num_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_perc,
        'top_IN_occupation': top_india_ocupations
    }
