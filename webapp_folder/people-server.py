#!/usr/bin/env python
# -*- coding: latin-1 -*-

Site = 'People . Elkhorn.io'

Timezone = 'Pacific/Honolulu'


  # - System
import os
import cgi
import urllib
import wsgiref.handlers
import datetime
import json, ast
import sys,imp
  # - Appengine
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from urlparse import urlparse
  # -
from google.appengine.ext import ndb
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app

import _html as _html



#----------------------------------------------#
#        Completed Data Stucture               #
#----------------------------------------------#
class People_db(ndb.Model):
    addTime = ndb.DateTimeProperty(auto_now_add=True)
    user = ndb.UserProperty()
    data_id = ndb.StringProperty()
#
    user_id = ndb.StringProperty()
    user_email = ndb.StringProperty()
    flag = ndb.StringProperty()
    visibility = ndb.StringProperty()
    data_type = ndb.StringProperty()
#
    person_id = ndb.StringProperty()
    item_id = ndb.StringProperty()
    item_name = ndb.StringProperty()
    item_type = ndb.StringProperty()
    item_kind = ndb.StringProperty()
    item_inst = ndb.StringProperty()
    item_twit = ndb.StringProperty()
    item_chat = ndb.StringProperty()
    item_social = ndb.JsonProperty()
    item_year = ndb.StringProperty()
    item_loca = ndb.StringProperty()
    item_orig = ndb.StringProperty()
#
    item_status = ndb.StringProperty()
    status_date = ndb.StringProperty()

    @classmethod
    def _get_people_list(self, user_data):
      q = People_db.query(People_db.user == user_data)
      db_data = []
      for item in q.iter():
        db_data.append(item.to_dict(exclude=['addTime', 'user']))
      return json.dumps(db_data)


    @classmethod
    def _save_item(self, item_data, user_data):
      print user_data
      
      date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      data_id = date_time
      
      person_id = date_time
      if person_id and person_id != '':
        db_item = People_db.get_by_id(person_id)
      else:
        person_id = data_id
      if not db_item:
        db_item = People_db(id=person_id)
        db_item.person_id = person_id
        db_item.data_id = data_id
        db_item.data_type = 'person_data'
        db_item.flag = '-'
        db_item.visibility = 'show'
      
        db_item.user_id = user_data.user_id()
        db_item.user_email = user_data.email()
        

        db_item.item_id = self.request.get('item_id')
        db_item.item_name = self.request.get('item_name')
        db_item.item_kind = self.request.get('item_kind')
        db_item.item_type = self.request.get('item_type')
        db_item.item_inst = self.request.get('item_inst')
        db_item.item_twit = self.request.get('item_twit')
        db_item.item_chat = self.request.get('item_chat')
        db_item.item_year = self.request.get('item_year')
        db_item.item_loca = self.request.get('item_loca')
        db_item.item_orig = self.request.get('item_orig')
      
      db_item.user = user_data
      
      db_item.put()
     # time.sleep(1)
      # project_name = file_data.get('project_name')

      return 'saved'


class updatePeople_db(webapp2.RequestHandler):
  def post(self):
    page_address = self.request.uri
    base = os.path.basename(page_address)
    
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    user = users.get_current_user()
    if user:
        item_id = self.request.get('item_id')
        client_email = user.email()
        key_name = item_id + '_' + client_email
        item = People_db(id=date_time)
        
        item.user = user
        item.user_id = user.user_id()
        item.user_email = user.email()
        

        item.item_id = self.request.get('item_id')
        item.item_name = self.request.get('item_name')
        item.item_kind = self.request.get('item_kind')
        item.item_type = self.request.get('item_type')
        item.item_inst = self.request.get('item_inst')
        item.item_twit = self.request.get('item_twit')
        item.item_chat = self.request.get('item_chat')
        item.item_year = self.request.get('item_year')
        item.item_loca = self.request.get('item_loca')
        item.item_orig = self.request.get('item_orig')

        item.put()
        
    self.redirect('/edit_people')






class publicSite(webapp2.RequestHandler):
    def get(self):
      # - URL Parse
        page_address = self.request.uri
        uri = urlparse(page_address)
        path = uri[2] # - uri.path
        layers = path.split('/')
        path_layer = layers[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
          user_email = user.email()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
          user_email = 'No User'
      # - app data
      
        html_file = 'main_layout.html'
        
        page_html = html_file
        
        
      # -
        if path_layer == 'my_info':
            page_html = _html.hi_test
            page_id = 'my_info'
            nav_select = 'my_info'
            user_header = 'on'
            
      # -
        if path_layer == 'edit_people':
            page_html = _html.edit_people
            page_id = 'edit_people'
            nav_select = 'edit_people'
            user_header = 'on'



      # - template
        objects = {

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
            'user_email': user_email,
        
            'page_html': page_html,
        
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/%s' %html_file)
        self.response.out.write(template.render(path, objects))


class accessData(webapp2.RequestHandler):
    def get(self):
      # - URL Parse
        page_address = self.request.uri
        uri = urlparse(page_address)
        path = uri[2] # - uri.path
        layers = path.split('/')
        path_layer = layers[1]
        base = os.path.basename(page_address)
#        item = base.split('?')[1]
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
        
        if path_layer == '_list_people':
            list_data =  ''
          
            self.response.out.write(People_db._get_people_list(user))

        if path_layer == '_add_person':
            item_data =  ''
          
            self.response.out.write(People_db._save_item(item_data, user))



app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    
    ('/my_info', publicSite),
    
    ('/edit_people/?', publicSite),
    ('/_list_people', accessData),
    
    ('/_add_person', updatePeople_db),
    
  
  

], debug=True)
