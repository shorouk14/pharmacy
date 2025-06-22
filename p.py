from flask import Flask, render_template, request

app = Flask(__name__)

# This is a simplified example - in a real app you would use a proper drug interaction database
def check_drug_interaction(drug1, drug2):
    # Example interaction database (very simplified)
    interactions = {
        ('aspirin', 'ibuprofen'): "These drugs may increase the risk of bleeding when taken together.",
        ('simvastatin', 'grapefruit'): "Grapefruit may increase the side effects of simvastatin.",
        ('warfarin', 'vitamin k'): "Vitamin K can decrease the effectiveness of warfarin."
    }
    
    # Check both possible orderings of drug names
    if (drug1.lower(), drug2.lower()) in interactions:
        return interactions[(drug1.lower(), drug2.lower())]
    elif (drug2.lower(), drug1.lower()) in interactions:
        return interactions[(drug2.lower(), drug1.lower())]
    else:
        return f"No known interactions found between {drug1} and {drug2}."

@app.route('/')
def home():
    return render_template('html.html')

@app.route('/check_interaction', methods=['POST'])
def check_interaction():
    drug1 = request.form['drug1']
    drug2 = request.form['drug2']
    result = check_drug_interaction(drug1, drug2)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)