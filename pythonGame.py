import random
from flask import Flask,jsonify
app = Flask(__name__)

all_tip= [
"tip",'tip2','tip3','tip4','tip5','tip6','tip7','tip8','tip9','tip10']
all_questions=[{}]

@app.route('/tip')
def get_tip():
    tip= {}
    tip['id']=random.randint(0,len(all_tip)-1)
    tip['text']= all_tip[tip['id']]
    return jsonify(tip)

@app.route('/question')
def get_question():
    return ''

@app.route('/answer')
def answer_quest(id):
    return ''
if __name__ == '__main__':
    app.run(debug=True)
