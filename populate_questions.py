import requests
import random
import json

def populate_categories_and_questions():
    # Get token for API
    token_response = requests.get('https://opentdb.com/api_token.php?command=request')
    token_data = token_response.json()
    token = token_data['token']
    print(token)
    # Get categories
    categories_response = requests.get(f'https://opentdb.com/api_category.php?token={token}')
    categories_data = categories_response.json()
    print(categories_data)
    # Initialize arrays and indices
    questions = []
    categories = []
    index_que = 1
    index_cat = 1
    # Populate categories
    for category in categories_data['trivia_categories']:
        # Format appropriately for Category model
        categories.append({
            'pk': index_cat,
            'model': 'questions.category',
            'fields': {
                'name': category['name']
            }
        })

        # Populate 10 questions per category
        questions_response = requests.get(f'https://opentdb.com/api.php?amount=10&category={category["id"]}&token={token}')
        questions_data = questions_response.json()
        for question in questions_data['results']:
            all_questions = []
            for inc_question in question['incorrect_answers']:
                all_questions.append(inc_question)
            all_questions.append(question['correct_answer'])
            # Shuffle questions
            random.shuffle(all_questions)
            # Format appropriately for Question model
            questions.append({
                'pk': index_que,
                'model': 'questions.question',
                'fields': {
                    'category': index_cat,
                    'content': question['question'],
                    'difficulty': question['difficulty'],
                    'questions': all_questions,
                    'correct_answer': question['correct_answer'],
                    'question_type': question['type']
                }
            })
            index_que += 1
        
        index_cat += 1
    print(categories)
    print(questions)

    # Dump data to JSON files
    categories_object = json.dumps(categories, indent=4)
    questions_object = json.dumps(questions, indent=4)

    with open('categories.json', 'w') as catfile:
        catfile.write(categories_object)
    with open('questions.json', 'w') as quefile:
        quefile.write(questions_object)

populate_categories_and_questions()