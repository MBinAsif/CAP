from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

# Load the saved model
nlp = spacy.load("C:\\Users\\muham\\OneDrive\\Desktop\\Semester 7\\NLP\\Project\\spacy_car_model")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    buying_price = request.form['buying_price']
    maintenance_price = request.form['maintenance_price']
    no_of_doors = request.form['no_of_doors']
    person_capacity = request.form['person_capacity']
    size_of_luggage = request.form['size_of_luggage']
    safety = request.form['safety']

    # Constructed text representing car features
    sample_text = f"Buying_Price: {buying_price}, Maintenance_Price: {maintenance_price}, No_of_Doors: {no_of_doors}, Person_Capacity: {person_capacity}, Size_of_Luggage: {size_of_luggage}, Safety: {safety}"

    # Process the text using the loaded model
    doc = nlp(sample_text)

    # Get the predicted category and its probabilities
    predicted_category = max(doc.cats, key=doc.cats.get)
    category_probabilities = doc.cats

    return render_template('result.html', category=predicted_category, probabilities=category_probabilities)

if __name__ == '__main__':
    app.run(debug=True)




