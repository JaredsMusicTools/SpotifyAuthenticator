#!/usr/bin/env python3.8

from flask import Flask, Response

class EndpointAction(object):

  def __init__(self, action):
    self.action = action
    self.response = Response(status=200, headers={})

  def __call__(self, *args):
    self.action()
    return self.response


class FlaskAppWrapper(object):
  app = None

  def __init__(self, name, application):
    self.app = application
    self.name = name

  def run(self):
    self.app.run()

  def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, endpoint_type=None):
    self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler),methods=endpoint_type)

