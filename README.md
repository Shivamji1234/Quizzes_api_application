# Quiz API
This is a RESTful API for creating and participating in timed quizzes.

# Functionalities

* Create a Quiz: Users can create a quiz by sending a POST request to the API with the required fields.
* Get Active Quiz: Users can retrieve the active quiz, which is the quiz currently within its start and end time.
* Get Quiz Result: After the end time of a quiz, users can retrieve the result of the quiz, including the right answer.
* Get All Quizzes: Users can retrieve all quizzes available.

# Path for Users

* http://127.0.0.1:8000/api/quiz/quizzes/
* http://127.0.0.1:8000/api/quiz/quizzes/active/
* http://127.0.0.1:8000/api/quiz/quizzes/:id/result
* http://127.0.0.1:8000/api/quiz/quizzes/all/

# API Endpoints 

The API provides the following endpoints:

* POST /quizzes: Create a new quiz.
* GET /quizzes/active: Retrieve the active quiz.
* GET /quizzes/:id/result: Retrieve the result of a quiz by its ID.
* GET /quizzes/all: Retrieve all quizzes


## For admin directly go to admin panel 
* From there  Create a new quiz.

## To access view API

* Postman to access the Quiz API

# For Create a new quiz
```
{
  "question": "What is the capital of France?",
  "options": ["London", "Paris", "Berlin", "Rome"],
  "right_answer": 1,
  "start_date": "2023-27-05T09:00:00Z",
  "end_date": "2023-27-05T0:00:00Z"
}

```

## API Documentation
The API is well-documented and provides detailed information about the available endpoints, request formats, and responses.

## Error Handling
The API implements error handling for all endpoints and returns appropriate error responses. The responses include relevant status codes and error messages to assist in debugging and handling errors.

## Automatic Quiz Status Updates
The status field of each quiz is automatically updated based on the start and end time. The status can be one of the following values: 'inactive' (before the start time), 'active' (during the available time), or 'finished' (after the end time). This ensures that the API accurately reflects the status of each quiz.

## Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

