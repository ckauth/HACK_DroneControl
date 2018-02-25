#!/usr/bin/python
import web

urls = (
        '/', 'index', 
        '/images/(.*)', 'images'
)

class index:
    def GET(self):
        return '''<html>
        <head>
        <title>Results</title>
        <meta http-equiv="refresh" content="5">
        </head>
        <body>
        <img src='./images/panorama_img_output.jpg' />
        </body>
        </html>'''

import os
class images:
    def GET(self, name):
        ext = name.split(".")[-1]

        cType = {
                "jpg": "images/jpeg"
                }

        if name in os.listdir('images'):
            web.header("Content-Type", cType[ext])
            return open('images/%s'%name, "rb").read()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
