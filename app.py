import flask
from flask_restful import Resource, Api, abort

app = flask.Flask(__name__)
api = Api(app)


todos = [
    {
        'id': 0,
        'title': 'Home related',
        'description': 'Some description here.',
        'isCompleted': False,
    },
    {
        'id': 1,
        'title': 'Python Coding task',
        'description': 'Develop a REST API',
        'isCompleted': False,
    },
    {
        'id': 2,
        'title': 'Others',
        'description': 'Make some notes from the Podcast',
        'isCompleted': False,
    },
]


class TODOs(Resource):
    # GET
    def get(self):
        try:
            data = flask.request.get_json(silent=True)
            if data == None:
                return {
                    'status': 'success',
                    'tasks': todos,
                }

            todo_id = data['id']

            return {
                'status': 'success',
                'task': todos[todo_id],
            }, 200
        except Exception as e:
            abort(400, message=e)

    # POST
    def post(self):
        try:
            data = flask.request.get_json(force=True)
            new_todo = {
                "id": len(todos),
                "title": data['title'],
                "description": data['description'],
                "isCompleted": False,
            }

            todos.append(new_todo)

            return {
                'status': 'success',
                'message': 'Task has been added successfully!',
            }

        except Exception as e:
            abort(400, message=e)

    # # PUT/UPDATE
    def put(self):
        try:
            data = flask.request.get_json(force=True)
            index = data['id']

            todos[index] = data

            return {
                'status': 'success',
                'message': 'Task has been updated successfully!',
            }

        except Exception as e:
            abort(400, message=e)

    # DELETE
    def delete(self):
        try:
            data = flask.request.get_json(force=True)
            index = data['id']

            todos.pop(index)

            return {
                'status': 'success',
                'message': 'Task has been deleted successfully!',
            }

        except Exception as e:
            abort(400, message=e)


api.add_resource(TODOs, '/tasks')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
