
# Flask
from flask import Flask, render_template, request, jsonify
import json

# CSV
import pandas as pd

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Fetching dataset for training
url = "https://raw.githubusercontent.com/nipunchamikara/MarksPredictor/main/student_scores.csv"
score_data = pd.read_csv(url)

# Training and Building Model
x_train, x_test, y_train, y_test = train_test_split(score_data["Hours"].values.reshape(-1, 1), score_data["Scores"])
score_model = LinearRegression().fit(x_train, y_train)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        
        try:
            hours = float(json.loads(request.get_data(as_text=True)).get("hours"))
        except TypeError:
            return jsonify({"success": False})

        # Obtaining and rounding result between 0 and 100
        result =  max(min(round(score_model.predict([[hours]])[0], 2), 100), 0)

        return jsonify({
            "success": True,
            "score": result
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=False)