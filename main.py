from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        send_email(name, email, message, subject)
        return render_template("index.html")
    return render_template('index.html')

@app.route("/<path:subpath>")
def portfolio(subpath):
    return render_template("portfolio-details.html", path=subpath)

def send_email(name, email, message, subject):
    email_message = f"Subject:{subject}\n\n{name}\n{email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="haiderbhatt1.297@gmail.com", password="rysehhflvvtplyiy")
        connection.sendmail(from_addr=email, to_addrs="haiderbhatt1.297@gmail.com", msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
