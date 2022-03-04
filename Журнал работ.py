from flask import Flask, render_template
from data import db_session
from data.models import User, Jobs

app = Flask(__name__)

db_session.global_init(f"db/mars_explorer.sqlite")

db_sess = db_session.create_session()


@app.route('/')
def works_log():
    job_lst = list()
    for job in db_sess.query(Jobs).all():
        job_lst.append(job)

    return render_template('work.html', jobs=job_lst)


app.run(port=5000, debug=True)
