# MCQ Generator

An application that generates multiple-choice questions (MCQs) from textual content. Built with NLP techniques, this tool helps educators quickly create quizzes based on the text from chapters, allowing efficient testing of students' knowledge.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Backend Details](#backend-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **MCQ Generator** is a tool that uses Natural Language Processing (NLP) to generate multiple-choice questions from provided text. It enables teachers to quickly generate quizzes, saving time and improving the efficiency of student assessments.

## Features

- **Automatic MCQ Generation**: Generates multiple-choice questions based on the input text.
- **Question Customization**: Allows customization of the number of options and question difficulty.
- **Answer Explanations**: Provides explanations for each generated answer choice.
- **User-Friendly Interface**: Built with Streamlit, offering an easy-to-use interface for educators.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/YourGitHubUsername/MCQGenerator.git
    cd MCQGenerator
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your browser and navigate to `http://localhost:8501`.
2. Paste the text or chapter content from which you want to generate MCQs.
3. Select the number of questions and options per question.
4. Click "Generate Questions" to see the MCQs, options, and correct answers.

## How It Works

The MCQ Generator utilizes NLP to analyze the provided text and generate relevant questions:

1. **Text Input**: The user inputs chapter content or a passage of text.
2. **NLP Processing**: The app processes the text using NLP techniques to identify key facts and concepts.
3. **Question Generation**: Based on the processed information, the app generates questions and provides multiple-choice options.
4. **Answer Explanations**: The correct answer is highlighted with an explanation.

## Backend Details

The backend processes the text and generates MCQs using NLP:

- `nlp_model.py`: Contains the logic for processing text and generating questions using NLP.
- `app.py`: The main Streamlit app code to provide the frontend interface.
- `mcq_generator.py`: The core file responsible for the generation of MCQs and answer options.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -am 'Add your feature'`).
4. Push the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Vipin Rawat - [GitHub](https://github.com/vipinrawat01)

Feel free to reach out for questions or suggestions!