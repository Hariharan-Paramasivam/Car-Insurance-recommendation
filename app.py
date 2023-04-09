from flask import Flask, render_template, request
from recommendation import run

app = Flask(__name__)


@app.route('/')
def front():
    return render_template('front.html')


@app.route('/result', methods=['POST','GET'])
def result():
    # Retrieve input values from front.html form
    age = request.form['Age']
    driving_license = request.form['Driving_license']
    previously_insured = request.form['previously_insured']
    vehicle_damage = request.form['vehicle_damage']
    vehicle_age = request.form['vehicle_age']
    vintage = request.form['vintage']
    region_code = request.form['region-code']
    policy_sales = request.form['policy-sales']

    print(f"Age: {age}")
    print(f"Driving License: {driving_license}")
    print(f"Previously Insured: {previously_insured}")
    print(f"Vehicle Damage: {vehicle_damage}")
    print(f"Vehicle Age: {vehicle_age}")
    print(f"Vintage: {vintage}")
    print(f"Region Code: {region_code}")
    print(f"Policy Sales: {policy_sales}")

    pred = run(age,driving_license,previously_insured,vehicle_damage,vehicle_age,vintage,region_code,policy_sales)

    return render_template('result.html',res=pred)




if __name__ == '__main__':
    app.run(debug=True)



