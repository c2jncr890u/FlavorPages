
import tornado.web

class index( tornado.web.RequestHandler ):
   def get( self ):
      self.render( "index.html" )

class about( tornado.web.RequestHandler ):
   def get( self ):
      self.render( "about.html" )

class privacy( tornado.web.RequestHandler ):
   def get( self ):
      self.render( "privacy.html" )

