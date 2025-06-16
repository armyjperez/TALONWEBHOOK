from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample ZIP segmentation data
zip_segments = {
    "35209": "Creative Explorer",
    "35022": "Technical Trailblazer",
    "35211": "Service-Oriented Achiever",
    "35221": "Community-Driven Helper",
    "35228": "Ambitious Goal-Seeker"
}

# Sample career match logic
interest_to_career = {
    "medical": "68W - Combat Medic Specialist",
    "tech": "17C - Cyber Operations Specialist",
    "law": "31B - Military Police",
    "mechanic": "91B - Wheeled Vehicle Mechanic",
    "aviation": "15T - UH-60 Helicopter Repairer",
    "leadership": "11X - Infantry (Leadership Track)",
    "creative": "25V - Combat Documentation/Production Specialist",
    "teamwork": "92Y - Unit Supply Specialist"
}

# Sample EVP messaging logic
evp_priority_message = {
    "college": "With Army Tuition Assistance and scholarships, your degree is more affordable than ever.",
    "career": "The Army provides real-world training and guaranteed career paths in high-demand fields.",
    "purpose": "If you're looking to make a difference, the Army offers meaningful missions and service.",
    "family": "The Army provides healthcare, housing allowances, and benefits to support your loved ones.",
    "travel": "You’ll have opportunities to see the world while building your future."
}

# Sample persona type alignment
persona_lookup = {
    "medical": "Empathetic Helper",
    "tech": "Innovative Thinker",
    "law": "Protective Leader",
    "mechanic": "Hands-On Problem Solver",
    "aviation": "Focused Technician",
    "leadership": "Confident Motivator",
    "creative": "Visual Storyteller",
    "teamwork": "Collaborative Partner"
}

@app.route('/talon-webhook', methods=['POST'])
def talon_webhook():
    data = request.get_json()

    zip_code = data.get('zip', '00000')
    interest = data.get('interest', 'general')
    evp = data.get('evp_priority', 'career')

    # Determine ZIP segment
    zip_segment = zip_segments.get(zip_code, "Motivated Explorer")

    # Determine career match
    career_match = interest_to_career.get(interest.lower(), "Various Army Career Options")

    # EVP messaging
    evp_message = evp_priority_message.get(evp.lower(), "We’ll help align your goals with benefits that matter.")

    # Persona match
    persona_type = persona_lookup.get(interest.lower(), "Versatile Talent")

    response = {
        "zip_segment": zip_segment,
        "career_match": career_match,
        "evp_message": evp_message,
        "persona_type": persona_type
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
