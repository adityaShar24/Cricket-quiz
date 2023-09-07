# Cricket Quiz

This web application is built using the Flask framework, designed to provide a robust and efficient backend for a cricket-themed quiz game. This application serves as the brain of the quiz, handling the logic behind question retrieval, scoringgti, and user interactions.


Cricket Quiz is a Python-based quiz application that tests your knowledge of cricket. This README provides an overview of the project, its structure, and how to get started.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Quiz Models](#quiz-models)
- [User Model](#user-model)
- [Middlewares](#middlewares)
- [Controllers](#controllers)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## About

Cricket Quiz is a fun and interactive quiz application that challenges your knowledge of cricket. Test your expertise on various cricket-related questions and improve your understanding of the game.

## Key Features

- **User Registration and Authentication:** Register and log in to your account to participate in the quiz.

- **Multiple-choice Questions:** Answer multiple-choice questions on cricket.

- **Interactive Quiz:** Experience an engaging and interactive quiz format.

- **Scoring and Feedback:** Receive your quiz score and detailed feedback on your performance.

- **Random Questions:** Questions are randomly selected to keep the quiz exciting.

- **User-Friendly Interface:** The application provides a user-friendly interface for answering questions.

- **MongoDB Database:** Utilizes MongoDB for data storage.

## Technologies Used

- **Flask**: A micro web framework for building web applications.
- **MongoDB**: A NoSQL document database used for storing user, room, and message data.
- **Flask-JWT-Extended**: A Flask extension that adds support for JSON Web Tokens (JWT) for user authentication.
- **Flask-Caching** :  Flask extension for caching and performance improvement.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- MongoDB set up and running.

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/adityaShar24/Cricket-Quiz.git

2. Navigate to project directory:

    ```shell
    cd Cricket-Quiz

3. Start The Apllication:

    ```shell
    cd python app.py
    

### Usage

- Register a user account.
- Log in to your account.
- Start the quiz, answer questions, and submit your answers.
- Receive your quiz score and feedback.

### Quiz Models

##### The project includes the following quiz-related models:

- **quiz_models.py**: Defines the Question and Answer models for quiz questions and user answers.


### User Model

#### The user-related model is defined in:

- **user_model.py**: Defines the User model for user registration and authentication.

### Middlewares

- Middlewares for user registration and authentication are defined in:

- **user_middleware.py**: Middleware for user registration and login.
- **quiz_middleware.py**: Middleware for quiz-related actions.

### Controllers
#### Controllers for user registration, login, and quiz-related actions are defined in:

- **user_controller.py**: User-related controllers.
- **quiz_controller.py**: Quiz-related controllers.

### Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.