from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import joblib

app = Flask(__name__)

# -----------------------------
# Load AI Model
# -----------------------------
model = tf.keras.models.load_model(
    "model/ipl_score_predictor.keras",
    compile=False
)

# -----------------------------
# Load Scaler
# -----------------------------
scaler = joblib.load("model/scaler.pkl")
# -----------------------------
# Load Label Encoders
# -----------------------------
label_encoders = joblib.load("model/label_encoders.pkl")
print(type(label_encoders))
print(label_encoders.keys())

print("Bat Teams:", label_encoders["bat_team"].classes_)
print("Bowl Teams:", label_encoders["bowl_team"].classes_)
print("Venues:", label_encoders["venue"].classes_[:5])
print("Batsmen:", label_encoders["batsman"].classes_[:5])
print("Bowlers:", label_encoders["bowler"].classes_[:5])

# -----------------------------
# Dropdown Data
# -----------------------------
bat_teams = list(label_encoders["bat_team"].classes_)
bowl_teams = list(label_encoders["bowl_team"].classes_)
venues = list(label_encoders["venue"].classes_)
batsmen = list(label_encoders["batsman"].classes_)
bowlers = list(label_encoders["bowler"].classes_)


@app.route("/")
def home():
    return render_template(
        "index.html",
        bat_teams=bat_teams,
        bowl_teams=bowl_teams,
        venues=venues,
        batsmen=batsmen,
        bowlers=bowlers,
        prediction=None
    )


@app.route("/predict", methods=["POST"])
def predict():

    try:

        bat_team = request.form["bat_team"]
        bowl_team = request.form["bowl_team"]
        venue = request.form["venue"]
        batsman = request.form["batsman"]
        bowler = request.form["bowler"]

        runs = float(request.form["runs"])
        wickets = float(request.form["wickets"])
        overs = float(request.form["overs"])
        striker = float(request.form["striker"])

        # -----------------------------
        # Input Validation

        if overs < 5 or overs > 20:
            return render_template(
                "index.html",
                bat_teams=bat_teams,
                bowl_teams=bowl_teams,
                venues=venues,
                batsmen=batsmen,
                bowlers=bowlers,
                prediction="❌ Overs must be between 5 and 20."
            )

        if wickets < 0 or wickets > 10:
            return render_template(
                "index.html",
                bat_teams=bat_teams,
                bowl_teams=bowl_teams,
                venues=venues,
                batsmen=batsmen,
                bowlers=bowlers,
                prediction="❌ Wickets must be between 0 and 10."
            )

        if striker > runs:
            return render_template(
                "index.html",
                bat_teams=bat_teams,
                bowl_teams=bowl_teams,
                venues=venues,
                batsmen=batsmen,
                bowlers=bowlers,
                prediction="❌ Striker runs cannot exceed current runs."
            )

        # -----------------------------
        # Encoding
        # -----------------------------

        bat_team = label_encoders["bat_team"].transform([bat_team])[0]
        bowl_team = label_encoders["bowl_team"].transform([bowl_team])[0]
        venue = label_encoders["venue"].transform([venue])[0]
        batsman = label_encoders["batsman"].transform([batsman])[0]
        bowler = label_encoders["bowler"].transform([bowler])[0]
        data = np.array([[
            bat_team,
            bowl_team,
            venue,
            runs,
            wickets,
            overs,
            striker,
            batsman,
            bowler
        ]])

        data = scaler.transform(data)

        prediction = model.predict(data, verbose=0)

        score = int(round(prediction[0][0]))

        return render_template(
            "index.html",
            bat_teams=bat_teams,
            bowl_teams=bowl_teams,
            venues=venues,
            batsmen=batsmen,
            bowlers=bowlers,
            prediction=score
        )

    except Exception as e:

        return render_template(
            "index.html",
            bat_teams=bat_teams,
            bowl_teams=bowl_teams,
            venues=venues,
            batsmen=batsmen,
            bowlers=bowlers,
            prediction=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)