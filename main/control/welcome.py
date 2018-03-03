# coding: utf-8

import flask

import config

from main import app

"""
NOTE: This will throw an error if there is no index.html, which is generated
with gulp build_frontend. The call to the server should be used only in production,
for development npm run dev inside frontend directory.
"""


@app.route('/')
def welcome():
  return flask.render_template('index.html', html_class='welcome')


@app.route('/sitemap.xml')
def sitemap():
  response = flask.make_response(flask.render_template(
    'sitemap.xml',
    lastmod=config.CURRENT_VERSION_DATE.strftime('%Y-%m-%d'),
  ))
  response.headers['Content-Type'] = 'application/xml'
  return response


@app.route('/_ah/warmup')
def warmup():
  return 'success'
