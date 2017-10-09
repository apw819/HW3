from flask import Flask, request, render_template
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/part2a', methods= ['POST', 'GET'])
def yourname():
    return render_template('blank_template.html')


@app.route('/part2b', methods= ['POST', 'GET'])
def compliment():
	part2b = request.args
	return render_template('blank_template_two.html', result=part2b)
    # return render_template('blank_template_two.html', result = part2b) 


if __name__ == '__main__':
    app.run()