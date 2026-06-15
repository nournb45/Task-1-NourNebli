# Task-1-NourNebli
# Simple Python Chatbot

## Description

This is a simple command-line chatbot built in Python. The chatbot responds to a predefined set of user inputs using a dictionary and the `.get()` method. If the user enters an unrecognized message, the chatbot returns a default response.

The conversation continues until the user types `goodbye`.

---

## Features

* Responds to common greetings such as `hello` and `hi`.
* Answers basic questions like:

  * "How are you?"
  * "What is your name?"
* Provides a default response for unknown inputs.
* Exits gracefully when the user types `goodbye`.
* Demonstrates the use of Python dictionaries and the `.get()` method.

---

## Technologies Used

* Python 3

---

## How It Works

The chatbot stores responses in a Python dictionary:

```python
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hello! How can I assist you today?",
    "how are you?": "I'm just a program, but I'm functioning as expected! How can I help you?",
    "what is your name?": "I am an AI assistant created to help you with your questions."
}
```

When the user enters a message, the chatbot searches for it in the dictionary using:

```python
responses.get(user_input, default_response)
```

If the input exists, the corresponding response is displayed. Otherwise, a default message is returned.

---

## Installation

1. Make sure Python 3 is installed on your computer.
2. Clone or download this project.
3. Open a terminal in the project folder.

---

## Usage

Run the chatbot with:

```bash
python project1.py
```

Example:

```text
You: hello
AI: Hello! How can I assist you today?

You: what is your name?
AI: I am an AI assistant created to help you with your questions.

You: goodbye
AI: Goodbye! Have a great day!
```

---

## Learning Objectives

This project demonstrates:

* Dictionaries in Python
* User input handling
* String methods (`lower()`, `strip()`)
* The `while` loop
* The `.get()` dictionary method
* Basic chatbot logic

---

## Future Improvements

* Add more responses and intents.
* Support multiple ways of asking the same question.
* Remove punctuation automatically.
* Add time and date responses.
* Implement keyword matching.
* Integrate with an AI API for more advanced conversations.

---

## Author

Created as a beginner Python chatbot project for learning and practice.
