
import controllers

import tornado.web
import tornado.httpserver
import tornado.ioloop

import sys


settings = dict(
   cookie_secret  =  file("/var/FlavorPages/app/secrets/cookie_secret").read().strip(),
   template_path  =  "/var/FlavorPages/app/views"
)

application = tornado.web.Application( [

    ( "/",                          controllers.index       ),
    ( "/about",                     controllers.about       ),
    ( "/contact",                   controllers.contact     ),
    ( "/newrecipe",                 controllers.newrecipe   ),    
    ( "/recipe/([a-zA-Z]{12})",          controllers.recipe      ),
    ( "/privacy",                   controllers.privacy     ), 
    ( "/thanks",                    controllers.thanks      ), 
    ( "/terms",                     controllers.terms       ),
          
], **settings )



#requires one command line argument, specifying the port to run on 
if __name__ == "__main__":
   assert len(sys.argv)==2 

   http_server = tornado.httpserver.HTTPServer(application, xheaders=True )

   listen_port = int(sys.argv[1])
   http_server.listen( listen_port )

   tornado.ioloop.IOLoop.instance().start()


