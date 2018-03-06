# coding: utf-8

from __future__ import absolute_import

import flask_restful
import flask
import model
from api import helpers
import auth
from main import api_v1


@api_v1.resource('/division/', endpoint='api.division.list')
class DivisionListAPI(flask_restful.Resource):
  def get(self):
    division_dbs, cursors = model.Division.get_dbs()
    return helpers.make_response(division_dbs, model.Division.FIELDS, cursors)

  # NOTE: Use to create divisions. Destructive operation
  @auth.admin_required
  def post(self):
    data = flask.request.get_json()
    for division in data:
      division_db = model.Division(
        name=division['name'],
        weight=int(division['weight']) if 'weight' in division else 0,
        is_male=bool(division['is_male']) if 'is_male' in division else True
      )
      division_db.put()
    return data
