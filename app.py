import flask
from flask_restful import Resource, Api, abort

app = flask.Flask(__name__)
api = Api(app)


todos = [
    'Do the shopping',
    'Develop a testing API today',
    'Write an article on Medium',
    'Start development of the website',
    'Start a new podcast',
]


class TODOs(Resource):
    # GET
    def get(self):
        try:
            data = flask.request.get_json(silent=True)
            if data == None:
                return {
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
            task = data['task']

            todos.append(task)

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
            updated_task = data['task']

            print(index, updated_task)
            todos[index] = updated_task

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
