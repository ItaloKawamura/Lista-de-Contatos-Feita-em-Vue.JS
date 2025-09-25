from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({'contacts': database.get_all_contacts()}), 200

@app.route('/contacts', methods=['POST'])
def create_contact():
    contato = request.get_json()
    print(contato)
    return jsonify({'contacts': database.add_contact(contato)}), 200

@app.route('/contacts/<email>', methods=['PUT'])
def update_contact(email):
    data = request.get_json()
    updated = database.update_contact(email, data)
    if not updated:
        return jsonify({'error': 'Contact not found'}), 404
    return jsonify({'message': 'Contact updated successfully', 'contact': updated}), 200

@app.route('/contacts/<email>', methods=['DELETE'])
def delete_contact(email):
    deleted = database.delete_contact(email)
    if not deleted:
        return jsonify({'error': 'Contact not found'}), 404
    return jsonify({'message': 'Contact deleted successfully'}), 200

if __name__ == "__main__":
    app.run(debug=True)