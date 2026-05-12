from flask import Flask, render_template, request

app = Flask(__name__)

USD = 90.0
RUB = 1.0
KZT = 0.20
EUR = 98.0

rates = {
    "USD": USD,
    "RUB": RUB,
    "KZT": KZT,
    "EUR": EUR
}

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    ans = ""

    if request.method == "POST":
        amount_text = request.form.get("amount")
        from_currency = request.form.get("from_currency")
        to_currency = request.form.get("to_currency")

        try:
            amount = float(amount_text)

            amount_in_rub = amount * rates[from_currency]
            result = amount_in_rub / rates[to_currency]

            ans = f"{amount} {from_currency} = {round(result, 2)} {to_currency}"

        except (ValueError, KeyError):
            ans = "Неверное значение"

    return render_template("index.html", ans=ans)


if __name__ == "__main__":
    app.run(debug=True)
