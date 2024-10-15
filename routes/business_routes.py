from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import db, Business, BusinessContent

business = Blueprint('business', __name__)

default_content = {
    "title": {
        "part1": "Business Tax Planning",
        "part2": "Aapke vyapar ke liye smart solutions"
    },
    "description": "Apne business tax planning ke liye professional solutions",
    "cards": [
        {
            "title": "Revenue Analysis",
            "description": "Aapke revenue ka vishleshan karke optimal tax strategy banayein"
        },
        {
            "title": "Expense Management", 
            "description": "Tax-efficient expense management ke tarike"
        },
        {
            "title": "Growth Planning",
            "description": "Business growth ke liye tax-efficient strategies"
        }
    ],
    "left_section": {
        "heading": "Business Tax Planning Options",
        "questions": [
            {
                "question": "Aap kis industry mein kaam karte hain?",
                "type": "radio",
                "options": []
            },
            {
                "question": "Aapke business mein kitne employees hain?",
                "type": "range",
                "options": [
                    {"value": "1-10", "price": "₹499"},
                    {"value": "11-50", "price": "₹999"},
                    {"value": "51-100", "price": "₹1499"},
                    {"value": "101-500", "price": "₹1999"},
                    {"value": "500+", "price": "₹2499"}
                ]
            },
            {
                "question": "Kya aapko international transactions hain?",
                "type": "radio",
                "options": []
            },
            {
                "question": "Aapko kis type ki tax planning chahiye?",
                "type": "radio",
                "options": []
            },
            {
                "question": "Kya aapke paas existing tax advisor hai?",
                "type": "radio",
                "options": []
            },
            {
                "question": "Aapko kitni jaldi tax planning ki zaroorat hai?",
                "type": "radio",
                "options": []
            }
        ]
    },
    "right_section": {
        "heading": "Business Tax Planning Benefits",
        "subheading": "Aapke business ke liye fayde",
        "points": [
            "Tax liability ko optimize karein",
            "Cash flow management improve karein",
            "Long-term growth ke liye plan karein"
        ],
        "sub_heading": "Humari guarantee",
        "cpa": [
            "100% satisfaction ya paise wapas",
            "Expert business advice 24/7 available"
        ]
    }
}

@business.route('/business', methods=['GET', 'POST'])
def business_page():
    if request.method == 'POST':
        return jsonify({"message": "POST request received"})
    
    saved_content = BusinessContent.query.first()
    
    if saved_content:
        content = saved_content.content
        # Ensure all keys from default_content are present in content
        for key, value in default_content.items():
            if key not in content:
                content[key] = value
    else:
        content = default_content
        new_content = BusinessContent(content=content)
        db.session.add(new_content)
        db.session.commit()

    return render_template('business.html', **content)

@business.route('/business/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def business_operations(id):
    bus = Business.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({"id": bus.id, "company_name": bus.company_name, "revenue": bus.revenue, "employees": bus.employees})
    
    elif request.method == 'PUT':
        data = request.json
        bus.company_name = data['company_name']
        bus.revenue = data['revenue']
        bus.employees = data['employees']
        db.session.commit()
        return jsonify({"message": "Business updated successfully"})
    
    elif request.method == 'DELETE':
        db.session.delete(bus)
        db.session.commit()
        return jsonify({"message": "Business deleted successfully"})

@business.route('/save-business-changes', methods=['POST'])
def save_business_changes():
    # This function is not implemented in the provided code block
    pass
