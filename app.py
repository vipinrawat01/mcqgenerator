from flask import Flask,request, render_template
import spacy
import random
from collections import Counter
nlp = spacy.load('en_core_web_sm')
from PyPDF2 import PdfReader

app = Flask(__name__)

def generate_mcqs(text, num_questions=5):
    
    doc = nlp(text)

    #extract senteces from the text
    sentences = [sent.text for sent in doc.sents]

    #random select sentences to form questions
    selected_sentences = random.sample(sentences,(min(num_questions,len(sentences))))

    mcqs = []
    #generate mcqs for each selected sentences

    for sentence in selected_sentences:
        sent_doc = nlp(sentence)

        entities = [ent.text for ent in doc.ents]
        nouns = [chunk.text for chunk in doc.noun_chunks]
    
        #extract nouns or entities from sentence
        nouns = [token.text for token in sent_doc if token.pos_ == "NOUN"]
        
        if len(nouns)< 2:
            continue
        noun_counts = Counter(nouns)
    
        if noun_counts:
            subject = noun_counts.most_common(1)[0][0]
            # print(subject)

            answer_choices = [subject]

            question_stem = sentence.replace(subject,"_______")
            # print(question_stem)
            distractors = entities + nouns
            distractors = list(set(distractors))
            distractor_fill =["global","best","efficient","widely"] 
            # Ensure the correct answer is included in the distractor
    # Combine the correct answer with the distractors
            options = distractors + [selected_sentences]
            random.shuffle(options)

            while len(distractors) < 3:
                for distract in distractor_fill:
                    distractors.append(distract)
                    if (len(distractors) == 3):
                        break
                           
            random.shuffle(distractors)
            for distractor in distractors[:3]:
                answer_choices.append(distractor)
                
            random.shuffle(answer_choices)

            #when we want to covert index number into letter this is the ascii code
            correct_answer = chr(64 + answer_choices.index(subject) + 1)

            mcqs.append((question_stem,answer_choices,correct_answer))
    return mcqs


def process_pdf(file):
    text = ""
    pdf_reader = PdfReader(file)
    for page_number in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_number].extract_text()
        text +=page_text
    return text
    

@app.route('/', methods =['POST','GET'])
def index():
    if request.method =='POST':
        text =""
        if 'files[]' in request.files:
            files = request.files.getlist("files[]")
            for file in files:
                if file.filename.endswith('.pdf'):
                    # process pdf files
                    text += process_pdf(file)
                elif file.filename.endswith('.txt'):               
                    #process the txt files
                    text += file.read().decode('utf-8')
        else:
            text = request.form['text']
        num_questions = int(request.form['num_questions'])

        mcqs = generate_mcqs(text, num_questions=num_questions)

        # Ensure each MCQ is formatted correctly as (question_stem, answer_choices, correct_answer)
        mcqs_with_index = [(i + 1, mcq) for i, mcq in enumerate(mcqs)]
        return render_template('mcqs.html', mcqs=mcqs_with_index)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)