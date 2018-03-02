# coding: utf-8

import flask

import config

from main import app


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
