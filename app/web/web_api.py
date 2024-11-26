from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/users/get_user_data/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    # Make a request to the REST API to get user data
    try:
        response = requests.get(f'http://127.0.0.1:5000/get_user_data/{user_id}')
        data = response.json()

        if response.status_code == 200:
            id = data["data"][0]
            user_name = data["data"][1]
            email = data["data"][3]
            phone = data["data"][5]
            cell = data["data"][4]
            return render_template('success_template.html', user_name=user_name, email=email, phone=phone, cell=cell, id=id)

        else:
            error_message = data.get('reason')
            return render_template('error_template.html', error_message=error_message), 404
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_message="No se pudo conectar a la API REST"), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)