from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__, template_folder='C:/Users/caleb/Templates.1')

# Define flashcards at the beginning
flashcards = [
    {"question": "What does 'T' stand for in TNM staging and how many stages are present?", "answer": "Tumor, 4"},
    {"question": "What does 'N' stand for in TNM staging and how many stages are present?", "answer": "Node, 3"},
    {"question": "What does 'M' stand for in TNM staging and how many stages are present?", "answer": "Metastasis, 1"},
    {"question": "How many grades of cancer are there?", "answer": "4, with 4 being the most aggressive."},
    {"question": "What is a Primary Tumor?", "answer": "A tumor that is identified by the tissue it came from"},
    {"question": "What are key functions of normal cells?", "answer": "Specific morphology, specific function, adherence, and well managed growth"},
    {"question": "What are key functions of benign tumor cells?", "answer": "Specific morphology, specific function, adherence, orderly growth"},
    {"question": "What are key functions of malignant tumor cells?", "answer": "Anaplasia, no useful function, harmful to tissue, loose adherence, migration, and complete loss of regulation."},
    {"question": "What does Anaplasia mean?", "answer": "Abnormal morphology"},
    {"question": "What is a Secondary Tumor?", "answer": "A tumor that consists of cells made from a primary tumor after metastasis"},
]

# Define quiz questions
quiz_questions = [
    {
        "question": "A patient with lung cancer is experiencing persistent cough, hemoptysis, and unexplained weight loss. Which of the following nursing assessments should be prioritized?",
        "options": {
            "A": "Assess the patient's pain level",
            "B": "Evaluate the patient's nutritional status",
            "C": "Monitor respiratory status and lung sounds",
            "D": "Check the patient's vital signs"
        },
        "correct_answer": "C"
    },
    {
        "question": "A nurse is preparing a patient for a biopsy to confirm a suspected diagnosis of breast cancer. Which of the following nursing interventions is the most important before the procedure?",
        "options": {
            "A": "Ensure the patient has signed the consent form",
            "B": "Explain the procedure in detail",
            "C": "Administer pre-procedure medications",
            "D": "Instruct the patient to fast for 12 hours"
        },
        "correct_answer": "A"
    },
    {
        "question": "A patient receiving chemotherapy presents with severe neutropenia. What is the priority nursing intervention?",
        "options": {
            "A": "Initiate contact precautions",
            "B": "Administer prescribed antibiotics",
            "C": "Educate the patient on infection signs",
            "D": "Monitor the patient's temperature"
        },
        "correct_answer": "A"
    }
]

@app.route('/flashcards', methods=['GET'])
def flashcards_page():
    return render_template('flashcards.html', flashcards=flashcards)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        choice = request.form.get('menu_choice')
        if choice == '1':
            return redirect(url_for('cancer_menu'))
        elif choice == '0':
            return redirect(url_for('feedback'))
        else:
            return render_template('home.html', error="Invalid Response")
        
    return render_template('home.html')

@app.route('/cancer', methods=['GET', 'POST'])
def cancer_menu():
    if request.method == 'POST':
        cancer_choice = request.form.get('cancer_choice')
        if cancer_choice == '1':
            return redirect(url_for('flashcards_page'))  # Redirect to flashcards
        elif cancer_choice == '2':
            return redirect(url_for('quiz'))  # Redirect to the quiz page
        elif cancer_choice == '3':
            return redirect(url_for('home'))
    return render_template('cancer_menu.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        selected_answers = request.form.to_dict()  # Get all answers submitted
        score = 0

        for question in quiz_questions:
            if selected_answers.get(question['question']) == question['correct_answer']:
                score += 1

        return render_template('quiz_result.html', score=score, total=len(quiz_questions))
    
    # Shuffle questions for randomness
    random.shuffle(quiz_questions)
    return render_template('quiz.html', questions=quiz_questions)

def notes():
    return render_template('notes.html')

@app.route('/feedback', methods=['GET'])
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
