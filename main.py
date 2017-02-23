#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def build_page(textarea_content, rotation_content):
    header = "<h1>Enter some text to encrypt!</h1>"

    rotation = "<p>Rotation: <input type='number' name='rot' value='" + rotation_content + "'/></p>"
    textarea = "<p>Message: <textarea name='message' style='height: 100px; width: 400px'>" + textarea_content + "</textarea></p>"
    submit = "<br><input type='submit'/>"
    form = header + "<form method='post'>" + textarea + rotation + submit + "</form>"
    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Insert some text to encrypt here!"
        content = build_page(message, "13")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rot = self.request.get("rot")
        coded = caesar.encrypt(message, int(rot))
        escaped_message = cgi.escape(coded)

        content = build_page(escaped_message, rot)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
