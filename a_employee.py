from flask import Flask, render_template, redirect, url_for, request
from employee import Employee

employee = []

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def employees_page():
    if request.method == "POST":
        new_employee_id = request.form.get("employee-id","")
        new_employee_name = request.form.get("name","")
        new_employee_last_name = request.form.get("last-name","")

        new_employee = Employee(name=new_employee_name, employee_id=new_employee_id)
        employee.append(new_employee)

        return redirect(url_for("employees_page"))
    
    return render_template("index.html", employee=employee)

if __name__ == "__main__":
    app.run(debug=True)


