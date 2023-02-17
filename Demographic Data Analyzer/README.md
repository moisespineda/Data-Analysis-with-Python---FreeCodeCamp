# Demographic-Data-Analyzer
This is a data analysis challenge as part of the FreeCodeCamp's 'Data Analysis with Python' course completion project.
The project name is Demographic Data Analyzer. As part of the challenge, Pandas is used to analyze demographic based on the given dataset of demographic data that was ectracted from the 1994 Census database. 

### By using Pandas, the following questions must be answered:
1. How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
2. What is the average age of men?
3. What is the percentage of people who have a Bachelor's degree?
4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8. What country has the highest percentage of people that earn >50K and what is that percentage?
9. Identify the most popular occupation for those who earn >50K in India.

### Expected answers:
1. Expected race count values to be [27816, 3124, 1039, 311, 271]
2. Expected different value for average age of men is 39.4
3. Expected different value for percentage with Bachelors degree is 16.4%
4. Expected different value for percentage with higher education that earn > 50K is 46.5%
5. Expected different value for percentage without higher education that earn > 50K is 17.4%
6. Expected different value for minimum work hours is 1
7. Expected different value for percentage of rich among those who work fewest hours is 10%
8. Expected different value for highest earning country is 'Iran'
9. Expected different value for highest earning country percentage is 41.9%
10. Expected different value for top occupations in India is 'Prof-speciality'

### Problems encountered during the analysis:
- For question 8, I did not managed to get 'Iran' as the country with highest percentage of people that earn > 50K. Instead I get, 'United States'.
- Due to mentioned problem, the percentage for highest earning country that I manage to get also differ from the expected value. 
- Codes are messy and I'm learning how to be more organized with the analysis.


#### Dataset Source 
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.