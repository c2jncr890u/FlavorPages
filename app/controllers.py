
from email.MIMEText import MIMEText
import os.path
import random
import smtplib
import string
import subprocess
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

def pick_id():
    id = ''.join(random.choice(string.letters) for _ in range(12))
    while os.path.exists('/var/recipes/'+id):
        id = ''.join(random.choice(string.letters) for _ in range(12))
    return id

class newrecipe( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "newrecipe.html" )
    def post( self ):
        text = self.get_argument("text")
        id = pick_id()
        os.mkdir("/var/recipes/"+id)
        file("/var/recipes/"+id+"/text.md",'w').write( text )  
        subprocess.Popen([  '/var/FlavorPages/app/scripts/Markdown.pl', 
                            '/var/recipes/'+id+'/text.md', ], 
                            stdout=file('/var/recipes/'+id+'/text.html') 
        ).wait()
        self.redirect("/recipe/"+id)

class recipe( tornado.web.RequestHandler ):
    """
    Recipes are stored in flat directories with the following structure
    /recipe/cf90cw-fav4/
        text.md
        text.html
    """
    def get( self, id ): 
        self.render("recipe.html",id=id)

class thanks( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "thanks.html" )






