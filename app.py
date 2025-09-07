from flask import Flask, request, render_template_string
import calculadora # import your functions

app = Flask(__name__)

# Simple HTML form
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora Web</title>
</head>
<body>
    <h2>🔢 Calculadora Web</h2>
    <form method="post" action="/">
        <input type="number" name="a" step="any" placeholder="Primer número" required>
        <input type="number" name="b" step="any" placeholder="Segundo número" required>
        <select name="operation">
            <option value="suma">Sumar (+)</option>
            <option value="resta">Restar (-)</option>
            <option value="multiplicación">Multiplicar (*)</option>
            <option value="división">Dividir (/)</option>
            <option value="potencia">Potencia (x^y)</option>
        </select>
        <button type="submit">Calcular</button>
    </form>
    {% if result is not none %}
        <h3>✅ Resultado: {{ result }}</h3>
    {% endif %}
    {% if error %}
        <h3 style="color:red;">❌ Error: {{ error }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    error = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            operation = request.form["operation"]

            if operation == "suma":
                result = calculadora.suma(a, b)
            elif operation == "resta":
                result = calculadora.resta(a, b)
            elif operation == "multiplicación":
                result = calculadora.multiplicación(a, b)
            elif operation == "división":
                result = calculadora.división(a, b)
            elif operation == "potencia":
                result = calculadora.potencia(a, b)

        except Exception as e:
            error = str(e)

    return render_template_string(html_form, result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)