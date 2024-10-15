from flask import Blueprint, render_template, request, jsonify
from models import db, IndividualContent
import json

individual = Blueprint('individual', __name__)

global_content = {}

@individual.route('/individual', methods=['GET', 'POST'])
def individual_page():
    if request.method == 'POST':
        return jsonify({"message": "POST request received"})
    
    saved_content = IndividualContent.query.first()
    
    # Default content structure
    default_content = {
        "title": "Individual Tax Planning",
        "description": "Apne personal tax planning ke liye smart solutions",
        "cards": [],
        "left_section": {
            "heading": "Tax Planning Options",
            "checkboxes": []
        },
        "right_section": {
            "heading": "Tax Planning Benefits",
            "subheading": "Aapke liye fayde",
            "points": [],
            "sub_heading": "Humari guarantee",
            "cpa": []
        }
    }
    
    if saved_content:
        content = saved_content.content
        # Ensure all keys from default_content are present in content
        for key, value in default_content.items():
            if key not in content:
                content[key] = value
    else:
        content = default_content

    return render_template('individual.html', **content)

@individual.route('/individual', methods=['GET'])
def get_all_individuals():
    return jsonify({"message": "GET request for all individuals received"})

@individual.route('/individual/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def individual_operations(id):
    if request.method == 'GET':
        return jsonify({"message": f"GET request for individual {id} received"})
    
    elif request.method == 'PUT':
        return jsonify({"message": f"PUT request for individual {id} received"})
    
    elif request.method == 'DELETE':
        return jsonify({"message": f"DELETE request for individual {id} received"})

@individual.route('/save-changes', methods=['POST'])
def save_changes():
    try:
        content = request.json
        existing_content = IndividualContent.query.first()
        if existing_content:
            existing_content.content = content
        else:
            new_content = IndividualContent(content=content)
            db.session.add(new_content)
        db.session.commit()
        return jsonify({"message": "Changes saved successfully"}), 200
    except Exception as e:
        print(f"Error saving changes: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "Error saving changes"}), 500
    
