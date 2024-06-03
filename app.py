from src.Pipeline.Predication_Pipeline import customData, predicationPipeline

from flask import Flask, request,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method =="GET":
        return render_template("form.html")
    else:
        data=customData(

            carat = float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = float(request.form.get('cut')),
            color = float(request.form.get('color')),
            clarity = float(request.form.get('clarity')),
        )

        final_data = data.get_as_dataframe()

        predication_Pipeline = predicationPipeline

        pred = predication_Pipeline.predict(final_data)

        result =round(pred[0],2)

        return render_template("result.html",final_result =result)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)    

