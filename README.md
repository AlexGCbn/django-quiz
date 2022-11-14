# django-quiz

The Django Quiz app has been developed to provide the user with a trivia question.
The game can be played either completely randomly, or by choosing options to filter the difficulty, category and question type.

** The link to the live page can be found [here.](https://alex-django-quiz.herokuapp.com/) **

# Project requirements

### As a user, I want to:
- Play the game with randomized questions.
- Be able to choose a category setting.
- Be able to choose a difficulty setting.
- Be able to choose a question type setting.
- Be able to combine the above.
- See my answer result.


# How to use
The homepage provides instructions on how to use the app.<br>
- You can ignore the form and press the green "Start" button to get a randomized question from the database.<br>
<br>

![Quiz with no options chosen](/media/quiz_no_options.png)<br>
<br>
- You can use the form to choose a Difficulty, Category and/or Question Type option.<br>
<br>
- If you do, when they press "Start" they will get a random question based on those parameters.<br>
<br>

![Quiz with no options chosen](/media/quiz_with_options.png)<br>
<br>
- You can always press the "Django Quiz" link on top to get to the home page.

# Technologies used
- [Django](https://www.djangoproject.com/) -> Framework to build the app
- [Open Trivia API](https://opentdb.com/api_config.php) -> API to get questions and relevant categories
- [ElephantSQL](https://www.elephantsql.com/) -> Free PostgreSQL database used to store data
- [Coverage](https://coverage.readthedocs.io/en/latest/install.html) -> Used to document testing
- The app has no Static files, so no static hosting service was used

# Installation
The app has been deployed to Heroku, so users can follow [this link](https://alex-django-quiz.herokuapp.com/) to access it.

### If you want to develop and use the app in your own environment, follow these steps:
1. You can fork the repository by clicking the "Fork" button on the top right of the repository page, [here.](https://github.com/AlexGCbn/django-quiz)
2. After you have a repository, open it in your IDE of choice.
3. Install dependencies with the command `pip3 install > requirements.txt`
4. Open a terminal in the main folder of the repository (or use your IDE's terminal) and run the command `python3 populate_questions.py`
> The populate_questions.py file will make a request to the Open Trivia API to get all categories and then populate 50 questions per category. You can edit line 30 to change the amount of questions. In the url, change amount to the amount you want. <br>
`https://opentdb.com/api.php?amount=AMOUNT_YOU_WANT&category={category["id"]}&token={token}` <br>
The categories.json and questions.json files already contain data which you can use. Running the command to update them will erase old data and populate it with new.
5. You will need to create an env.py file and set the following environment variables in it:
> SECRET_KEY = YOUR_DJANGO_SECRET_KEY <br>
DATABASE_URL = YOUR_DATABASE_URL

> PostgreSQL on the page [ElephantSQL](https://www.elephantsql.com/) was used when creating the app, yet you can use any RDBMS of choice.
6. Run the migration commands to migrate the models: `python3 manage.py makemigrations` and `python3 manage.py migrate`
7. You will need to load the new categories and questions in the database with the following commands: `python3 manage.py loaddata categories.json` and `python3 manage.py loaddata questions.json`
8. You will need to set new values for ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS in your settings.py file to match your own URLs.
9. The app should now be ready. You can run the server in your IDE with `python3 manage.py runserver`

### If you want to deploy to Heroku:
1. Go to Heroku and sign up/sign in.
2. Create a new app with the desired name.
3. Go to the app's Settings tab and set up your environment variables (the ones mentioned above) in the Config Vars.
4. On the app's Deploy page, you can connect it to your GitHub repository (the one for the app) and set up manual or automatic deployment.
> The app already has a Procfile for Heroku and the requirements.txt file, so Heroku knows which dependencies to install and how to use the app.
5. After a successful deployment, you can open the app with the "Open app" button on the top-right.

# Testing

## Unit testing

Unit testing was conducted with the Django test suite and was documented with the [coverage](https://coverage.readthedocs.io/en/latest/install.html) library. 
Models, views and forms are reported as 100% tested in coverage.

<details><summary>Screenshots</summary>

![Coverage overall](/media/coverage.png)
![Models coverage](/media/coverage_models.png)
![Views coverage](/media/coverage_views.png)

</details>
<br/>


## Manual testing
- Play the game with randomized questions.

| **Action** | **Expected Result** | **Actual Result** |
|------------|---------------------|-------------------|
| Press "Start" without any form options chosen | Get random question | Works as expected |

<details><summary>Screenshots</summary>

![Quiz with no options](/media/quiz_no_options.png)
![Random question 1](/media/random_question_1.png)

</details>
<br/>


- Be able to choose a category setting.

| **Action** | **Expected Result** | **Actual Result** |
|------------|---------------------|-------------------|
| Press "Start" after choosing a category | Get question from category | Works as expected |

<details><summary>Screenshots</summary>

![Quiz categories](/media/categories.png)
![Category picked](/media/category_picked.png)
![Category question 1](/media/category_question.png)

</details>
<br/>


- Be able to choose a difficulty setting.

| **Action** | **Expected Result** | **Actual Result** |
|------------|---------------------|-------------------|
| Press "Start" after choosing a difficulty | Get question from difficulty | Works as expected |

<details><summary>Screenshots</summary>

![Quiz difficulties](/media/difficulty.png)
![Difficulty picked](/media/difficulty_picked.png)
![Difficulty question 1](/media/difficulty_question.png)

</details>
<br/>


- Be able to choose a question type setting.

| **Action** | **Expected Result** | **Actual Result** |
|------------|---------------------|-------------------|
| Press "Start" after choosing a question type | Get question from question type | Works as expected |

<details><summary>Screenshots</summary>

![Quiz question types](/media/question_type.png)
![Question type picked](/media/question_type_picked.png)
![Question type question 1](/media/question_type_question.png)

</details>
<br/>

- Be able to combine the above.

| **Action** | **Expected Result** | **Actual Result** |
|------------|---------------------|-------------------|
| Press "Start" after choosing a combination of settings | Get question from combination | Works as expected |

<details><summary>Screenshots</summary>

![Question combination picked](/media/combination_picked.png)
![Question type question 1](/media/combination_question.png)

</details>

