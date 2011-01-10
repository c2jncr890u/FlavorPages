
import tornado.web

class index( tornado.web.RequestHandler ):
   """/"""

   def get( self ):
      """GET /"""
      self.render( "index.html" )



