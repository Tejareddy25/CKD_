import pickle as pkl
from flask import Flask, render_template, request

app = Flask(__name__)
model = pkl.load(open("RF.pkl", "rb"))

def predict_class(age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia):
    # Create a feature vector from user input
    user_input = [[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia]]
    
    # Make predictions using the trained model
    prediction = model.predict(user_input)
    
    if prediction[0] == 1:
        result = "Likely to have chronic kidney disease"
    else:
        result = "Not likely to have chronic kidney disease"
    
    return result

@app.route('/')
def index():
    return render_template('iiindex.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect user input for feature values
    age = float(request.form["age"])
    blood_pressure = float(request.form["blood_pressure"])
    specific_gravity = float(request.form["specific_gravity"])
    albumin = float(request.form["albumin"])
    sugar = float(request.form["sugar"])
    red_blood_cells = float(request.form["red_blood_cells"])
    pus_cell = float(request.form["pus_cell"])
    pus_cell_clumps = float(request.form["pus_cell_clumps"])
    bacteria = float(request.form["bacteria"])
    blood_glucose_random = float(request.form["blood_glucose_random"])
    blood_urea = float(request.form["blood_urea"])
    serum_creatinine = float(request.form["serum_creatinine"])
    sodium = float(request.form["sodium"])
    potassium = float(request.form["potassium"])
    haemoglobin = float(request.form["haemoglobin"])
    packed_cell_volume = float(request.form["packed_cell_volume"])
    white_blood_cell_count = float(request.form["white_blood_cell_count"])
    red_blood_cell_count = float(request.form["red_blood_cell_count"])
    hypertension = float(request.form["hypertension"])
    diabetes_mellitus = float(request.form["diabetes_mellitus"])
    coronary_artery_disease = float(request.form["coronary_artery_disease"])
    appetite = float(request.form["appetite"])
    peda_edema = float(request.form["peda_edema"])
    aanemia = float(request.form["aanemia"])
    
    result = predict_class(age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema, aanemia)
    
    return render_template('rrresult.html', result=result)

if __name__ == '__main__':
    app.run()
