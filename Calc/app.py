from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        operation = request.form.get("operation")

        # Always read num1 and num2 from the HTML
        num1 = request.form.get("num1", "").strip()
        num2 = request.form.get("num2", "").strip()

        # ------------------------------
        # SINGLE NUMBER OPERATIONS
        # ------------------------------
        single_ops = ["sin", "cos", "tan", "sqrt", "log", "exp"]

        if operation in single_ops:
            if num1 == "":
                result = "Please enter a number."
            else:
                num = float(num1)

                if operation == "sin":
                    result = math.sin(math.radians(num))
                elif operation == "cos":
                    result = math.cos(math.radians(num))
                elif operation == "tan":
                    result = math.tan(math.radians(num))
                elif operation == "sqrt":
                    result = "Error: negative root" if num < 0 else math.sqrt(num)
                elif operation == "log":
                    result = "Error: log undefined for ≤ 0" if num <= 0 else math.log10(num)
                elif operation == "exp":
                    result = math.exp(num)

        # ------------------------------
        # TWO-NUMBER OPERATIONS
        # ------------------------------
        else:
            if num1 == "" or num2 == "":
                result = "Please enter both numbers."
            else:
                num1 = float(num1)
                num2 = float(num2)

                if operation == "+":
                    result = num1 + num2
                elif operation == "-":
                    result = num1 - num2
                elif operation == "*":
                    result = num1 * num2
                elif operation == "/":
                    result = "Error: cannot divide by 0" if num2 == 0 else num1 / num2
                elif operation == "^":  # power
                    result = num1 ** num2

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)