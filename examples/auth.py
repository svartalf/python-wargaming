import os

from flask import Flask, render_template_string, request, redirect, make_response
import wargaming

app = Flask(__name__)

wot = wargaming.WoT(os.environ['WARGAMING_API'], language='ru', region='ru')

HTML_TEMPLATE = """<!doctype html>
<title>Wargaming AUTH</title>
{% if error %}
<p style="color: red">Error: {{ error }}</p>
{% endif %}
{% if nickname %}
  <h1>Hello {{ nickname }}!</h1>
  <p>access_token: {{ access_token }}</p>
  <p>nickname: {{ nickname }}</p>
  <p>account_id: {{ account_id }}</p>
  <p>expires_at: {{ expires_at }}</p>
  <a href="/prolongate">Prolongate session</a>
  <a href="/logout">Logout</a>
{% else %}
  <h1><a href="/login">Please login</a></h1>
{% endif %}
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, **request.cookies)


@app.route('/login')
def login():
    wot_login = wot.auth.login(redirect_uri='http://127.0.0.1:5000/auth', nofollow=1)
    print(wot_login['location'])
    return redirect(wot_login['location'])


@app.route('/logout')
def logout():
    wot.auth.logout(access_token=request.cookies['access_token'])
    response = redirect('/')
    for k in request.cookies:
        response.delete_cookie(k)
    return response


@app.route('/auth')
def auth():
    data = dict(request.args.items())
    if data['status'] == 'ok':
        response = make_response(render_template_string(HTML_TEMPLATE, **data))
        for k, v in data.items():
            response.set_cookie(k, v)
        return response
    return make_response(render_template_string(HTML_TEMPLATE, error=data['message']))


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
