
import tornado.web

class index( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "index.html" )

class about( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "about.html" )

class contact( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "contact.html" )

class terms( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "terms.html" )

class privacy( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "privacy.html" )


class newrecipe( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "newrecipe.html" )
    def post( self ):
        self.redirect( "/" )

