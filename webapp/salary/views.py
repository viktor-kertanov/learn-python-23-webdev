from flask import Blueprint, render_template

from webapp.salary.salary_queries import top_salary

blueprint = Blueprint('salary', __name__, url_prefix="/salary")

@blueprint.route('/get-all')
def pagination():
    title = "Testing pagination"
    salaries = top_salary(200)
    return render_template("salary/salary.html",
                            webpage_title=title,
                            salaries=salaries)