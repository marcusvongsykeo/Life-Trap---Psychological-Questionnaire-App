# Life-Trap---Psychological-Questionnaire-App
**DISCLAIMER: In no way should this application or the prescribed book [Reinventing Your Life](https://www.booktopia.com.au/reinventing-your-life-jeffrey-e-young/book/9780452272040.html?source=pla&gclid=EAIaIQobChMIuJbXo5-e6gIVD38rCh3ZAgI9EAQYAyABEgJZ9fD_BwE) substitute any professional support one can receive from a qualified psychologist, counsellor or other mental health professional. This application is intended to be used as a possible guide towards self-reflection and does not constitute a professional psychological evaluation.**

This is a Python application that performs a psychological questionnaire that helps to determine negative behavioral traits in individuals (or Life Traps), based on the ideas presented in the book [Reinventing Your Life](https://www.booktopia.com.au/reinventing-your-life-jeffrey-e-young/book/9780452272040.html?source=pla&gclid=EAIaIQobChMIuJbXo5-e6gIVD38rCh3ZAgI9EAQYAyABEgJZ9fD_BwE) by psychologists Jeffrey E. Young, PhD., and Janet S. Klosko, PhD.

The program includes 11 tests of 10 questions derived from the book [Reinventing Your Life](https://www.booktopia.com.au/reinventing-your-life-jeffrey-e-young/book/9780452272040.html?source=pla&gclid=EAIaIQobChMIuJbXo5-e6gIVD38rCh3ZAgI9EAQYAyABEgJZ9fD_BwE):
- Abandonment
- Mistrust and Abuse
- Vulnerability
- Dependence
- Emotional Deprivation
- Social Exclusion
- Defectiveness
- Failure
- Subjugation
- Unrelenting Standards
- Entitlement

Each Life Trap is scored between 10 and 60; a score ranging from 10-29 indicates that the Life Trap is less relevant to you; a score ranging from 30-60 indicates that the Life Trap is more relevant. Further reading of the book 'Reinventing Your Life', where these tests are derived, is highly recommended in order to fully grasp the ideas of each Life Trap and how to improve negative behaviours which one may identify through use of this application.

There are 4 main functions of this program:

**1. Take Life Trap Test:**
This function performs the questionnaire for however many Life Traps. The scores are saved in the user's profile. The test can be repeated over time and compared with previous scores to see how the relevance of each Life Trap changes over time.

**2. View Life Trap Score:**
This function shows the current scores of the current user for each Life Trap.

**3. View Life Trap Rank:**
This function sorts each Life Trap by their severity based on a metric derived from the book 'Reinventing Your Life', giving a better presentation of how relevant each Life Trap is to the user.

**4. See Life Trap History:**
This function presents all the previous scores up to the latest scores for each Life Trap. Here the user is able to compare their scores as time progresses.


**Life Trap User Database**

Currently all data for each user is stored in the accompanying 'LifeTrapUserData.txt' file, which is accessed through the **USER_DATA_FILE** variable in the 'LifeTrapApp' python script. Each user profile is composed of the following data:

**User Number:** This is the unique integer number used by the program to identify each user.

**User Name:** The name of the user. New users can be added to the database through the application by inputting a new username.

**Life Trap Score:** The score for each Life Trap, based on the scores derived from the Life Trap test. There are a total of 11 different scores for each user.

**Test Date:** The date in which the scores were collected through the Life Trap test. The date is appended to the score data in the **USER_DATA_FILE**. 

Each user can have multiple scores appended to their profile in order to compare changing Life Trap scores over time. Each line of the **USER_DATA_FILE** represents a single user. The user number, user name and score data are seperated by commas (,) on each line with each of the 11 scores seperated by hyphens (-). The test date is appended to the relevant scores with a preceding period (.). The date format is DD/MM/YYYY (cos that's how we do it down unda) Each new set of scores are further appended on the same line with a preceding colon (:)
Here is an example of a user's data with multiple scores from different dates:

`0,John,-20-16-24-29-20-30-35-31-31-28-29-.13052020:-23-16-24-29-20-30-35-31-31-28-29-.03052020:`

The application is in a fully functional state using the python console. I am currently working on a GUI which can package the program as a .EXE using the TkInter library.
