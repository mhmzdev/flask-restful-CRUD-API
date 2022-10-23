## flask-restful CRUD API
A very simple example of TODO App CRUD operations via REST API in flask-restful that could be used for testing purposes.

### Running locally
```
git clone https://github.com/mhmzdev/flask-restful-CRUD
cd flask-restful_CRUD
pip install -r requirements.txt
python app.py
```

Open http://localhost:8080/tasks at your browser to see if you are getting all tasks

### Deployed
It's deployed on Heroku at https://flask-restful-tasks.herokuapp.com/tasks


### Available methods
Below is the end-point that remains the same for all the methods to keep things simple.

Local Endpoint: http://localhost:8080/tasks

Deployed Endpoint: https://flask-restful-tasks.herokuapp.com/tasks

### ⬇️ GET

Simply make a REQUST at the end-point given

Response:
```
{
    "status": "success",
    "tasks": [
        {
            "id": 0,
            "title": "Home related",
            "description": "Some description here.",
            "isCompleted": false
        },
        {
            "id": 1,
            "title": "Python Coding task",
            "description": "Develop a REST API",
            "isCompleted": false
        },
        {
            "id": 2,
            "title": "Others",
            "description": "Make some notes from the Podcast",
            "isCompleted": false
        }
    ]
}
```

To get a specific task, send payload as following to GET method
```
{
    "id": 0
}
```
Response:
```
{
    "status": "success",
    "task": {
        "id": 0,
        "title": "Home related",
        "description": "Some description here.",
        "isCompleted": false
    }
}
```

### ⬆️ POST

Request payload:
```
{   
    "title": "Some title",
    "description": "Some description"
}
```

Response:
```
{
    'status': 'success',
    'message': 'Task has been added successfully!',
}
```

### 🔄 PUT
Request payload:
```
{
    "id": 0,
    "title": "Some new title",
    "description": "Some new description",
    "isCompleted: true,
}
```

Response:
```
{
    'status': 'success',
    'message': 'Task has been updated successfully!',
}
```

### ❌ DELETE
Request payload:
```
{
    "id": 0
}
```

Response:
```
{
    'status': 'success',
    'message': 'Task has been deleted successfully!',
}
```