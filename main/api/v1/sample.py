# coding: utf-8

from __future__ import absolute_import

import flask_restful

from main import api_v1


@api_v1.resource('/sample/', endpoint='api.sample')
class SampleAPI(flask_restful.Resource):
  def get(self):
    return {"data": "some data", "date": "today"}
