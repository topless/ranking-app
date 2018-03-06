# coding: utf-8

from __future__ import absolute_import

from google.appengine.ext import ndb

from api import fields
import model


class Division(model.Base):
  name = ndb.StringProperty(default='', required=True)
  weight = ndb.IntegerProperty()
  is_male = ndb.BooleanProperty(default=True)

  FIELDS = {
    'name': fields.String,
    'weight': fields.Integer,
    'is_male': fields.Boolean
  }

  FIELDS.update(model.Base.FIELDS)
