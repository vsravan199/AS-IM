from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html') 
@app.route('/data' , methods = ['POST'])
def data():
    F = request.form.get('Please enter Frequency range from 1 to 5', type=int)
    EI = request.form.get('Please enter Environmental_Impact range from 1 to 5', type=int)
    R = request.form.get('Please enter Regulatory range from 1 to 5', type=int)
    SC = request.form.get('Please enter Stakeholders_Concern range from 1 to 5', type=int)
    result = (F+EI+R+SC)
    if result >= 16 :
       Risk = 'Risk is High and required actions with time frames'
    if result == 12 and result < 16 :
       Risk = 'Risk is Moderate and required actions'
    if result < 12 :
       Risk = 'Risk is Limited'
    return render_template('result.html', output = Risk)         
if __name__=='__main__':
    app.run(debug=True)