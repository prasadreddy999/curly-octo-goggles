from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='POST':
        sone_json=request.get_json()
        return jsonify({"you sent":sone_json}), 201
    else:
        return jsonify({"about":"hello world"})

if __name__=='__main__':
    app.run(debug=True)


## REST API

