import urllib

from flask import Flask, render_template_string, request, redirect
from openid.consumer import consumer
from openid.cryptutil import randomString


app = Flask(__name__)

HTML_TEMPLATE = """<!doctype html>
<title>Wargaming OpenID AUTH</title>
{% if error %}
<p style="color: red">Error: {{ error }}</p>
{% endif %}
{% if nickname %}
  <h1>Hello {{ nickname }}!</h1>
  <p>nickname: {{ nickname }}</p>
  <p>account_id: {{ account_id }}</p>
  <a href="/logout">Logout</a>
{% else %}
  <h1><a href="/login">Please login</a></h1>
{% endif %}
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, **request.cookies)


@app.route("/login")
def login():
    if 'SESSION_ID' not in request.cookies:
        session_id = randomString(16, '0123456789abcdef')
    else:
        session_id = request.cookies['SESSION_ID']

    oidconsumer = consumer.Consumer({'id': session_id}, None)
    oidrequest = oidconsumer.begin(u'http://ru.wargaming.net/id/openid/')

    print(oidrequest.shouldSendRedirect())
    redirect_url = oidrequest.redirectURL(
        realm='http://127.0.0.1:5000/',
        return_to='http://127.0.0.1:5000/auth_cb',
    )
    print(oidrequest.shouldSendRedirect())
    response = redirect(redirect_url)
    response.set_cookie('SESSION_ID', session_id)
    return response


@app.route("/auth_cb")
def auth_cb():
    oidconsumer = consumer.Consumer({'id': request.cookies['SESSION_ID']}, None)
    result = oidconsumer.complete(request.args, 'http://127.0.0.1:5000/auth_cb')
    if result.status == consumer.SUCCESS:
        account_id, nickname = urllib.parse.urlparse(
            request.args['openid.identity']).path.split('/')[2].split('-')
        response = redirect('/')
        response.set_cookie('account_id', account_id)
        response.set_cookie('nickname', nickname)
        return response
    return render_template_string(HTML_TEMPLATE, error=result)


@app.route('/logout')
def logout():
    response = redirect('/')
    for cookie in request.cookies:
        response.delete_cookie(cookie)
    return response


if __name__ == '__main__':
    app.run('127.0.0.1', 5000)
