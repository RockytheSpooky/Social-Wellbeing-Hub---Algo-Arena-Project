from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mental_health', methods=['GET', 'POST'])
def mental_health():
    response = None
    if request.method == 'POST':
        # Expanded questions for the mental health check
        mood = request.form['mood']
        coping = request.form['coping']
        stress_level = request.form['stress_level']

        mood_dict = {
            "1": "You're feeling happy! That's great! Keep up the positive energy.",
            "2": "You're feeling stressed. It's important to take a moment for yourself and unwind.",
            "3": "You're feeling anxious. Remember, it's okay to take a break and focus on self-care.",
            "4": "You're feeling sad. Reach out to a friend or a loved one – you're not alone.",
            "5": "You're feeling angry. Consider redirecting that energy into something productive, like a workout.",
            "6": "You're feeling lonely. Try connecting with someone you trust, and remember that it's okay to ask for help."
        }

        coping_dict = {
            "1": "You take things one step at a time and focus on the present. This can help alleviate overwhelming feelings.",
            "2": "You tend to focus on distractions like your hobbies or watching TV. Consider incorporating mindfulness into your routine.",
            "3": "You talk to someone to help you process your feelings. This is a great way to get support!",
            "4": "You might bottle up your feelings. It’s important to express yourself and seek help when necessary."
        }

        stress_level_dict = {
            "1": "You're handling stress well today, which is great! Keep prioritizing self-care.",
            "2": "You’re somewhat stressed. Remember to take breaks, practice deep breathing, and avoid overloading yourself.",
            "3": "You're feeling stressed and overwhelmed. It might be time to take a pause and do something relaxing.",
            "4": "You're very stressed. Consider reaching out for professional help or talking to a loved one for support."
        }

        mood_response = mood_dict.get(mood, "Invalid mood")
        coping_response = coping_dict.get(coping, "Invalid coping mechanism")
        stress_level_response = stress_level_dict.get(stress_level, "Invalid stress level")

        response = f"{mood_response} {coping_response} {stress_level_response}"

    return render_template('mental_health.html', response=response)

@app.route('/financial_quiz', methods=['GET', 'POST'])
def financial_quiz():
    response = None
    answers = {
        'answer1': None,
        'answer2': None,
        'answer3': None,
        'answer4': None
    }

    if request.method == 'POST':
        # Get the user's answers
        answers['answer1'] = request.form.get('answer1')
        answers['answer2'] = request.form.get('answer2')
        answers['answer3'] = request.form.get('answer3')
        answers['answer4'] = request.form.get('answer4')

        correct_answers = {
            'answer1': 'c',
            'answer2': 'b',
            'answer3': 'b',
            'answer4': 'c'
        }

        score = 0
        for question, answer in answers.items():
            if answer == correct_answers[question]:
                score += 1

        response = f"You got {score} out of 4 questions correct! Here's how you did:"

        # Give feedback based on the user's score
        if score == 4:
            response += " Excellent! You have a strong understanding of personal finance!"
        elif score == 3:
            response += " Great job! You have a solid grasp of personal finance basics."
        elif score == 2:
            response += " Nice try! You might want to review some financial topics."
        else:
            response += " Looks like there’s some room for improvement. Don't worry, keep learning!"

    return render_template('financial_quiz.html', response=response, answers=answers)


@app.route('/personality_check', methods=['GET', 'POST'])
def personality_check():
    response = None
    if request.method == 'POST':
        # Get the form data
        reaction = request.form['reaction']
        conflict = request.form['conflict']
        relaxation = request.form['relaxation']
        introvert_extrovert = request.form['introvert_extrovert']
        decision_making = request.form['decision_making']

        # Initialize personality scores
        personality_score = {
            'calm': 0,
            'quick': 0,
            'talk': 0,
            'avoid': 0,
            'face': 0,
            'compromise': 0,
            'alone': 0,
            'socialize': 0,
            'active': 0,
            'introvert': 0,
            'extrovert': 0,
            'gut': 0,
            'logical': 0,
        }

        # Assign points to each personality trait based on answers
        personality_score[reaction] += 1
        personality_score[conflict] += 1
        personality_score[relaxation] += 1
        personality_score[introvert_extrovert] += 1
        personality_score[decision_making] += 1

        # Determine the personality type based on the highest score
        highest_trait = max(personality_score, key=personality_score.get)

        # Give a personalized result
        if highest_trait in ['introvert', 'extrovert']:
            personality_type = f"Your personality type is: {highest_trait.capitalize()}!"
        else:
            personality_type = f"Based on your answers, we can say: You're a {highest_trait.capitalize()} personality!"

        response = personality_type

    return render_template('personality_check_v2.html', response=response)

@app.route('/gratitude_journal', methods=['GET', 'POST'])
def gratitude_journal():
    response = None
    if request.method == 'POST':
        gratitude = request.form['gratitude']
        response = f"Thank you for sharing! You're grateful for: {gratitude}"
    return render_template('gratitude_journal.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
