
from email.MIMEText import MIMEText
import smtplib
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
        msg = MIMEText(self.get_argument("text",""))
        msg["Subject"] = "New recipe submitted to flavorpages.com"
        msg["From"] = "mailbot@flavorpages.com"
        msg["To"] = "sleepdev@gmail.com"
        s = smtplib.SMTP()
        s.connect("localhost")
        s.sendmail("mailbot@goodlook.me","sleepdev@gmail.com", msg.as_string())
        s.close()
        self.redirect("/thanks")

class recipe( tornado.web.RequestHandler ):
    """
    Recipes are stored in flat directories with the following structure
    /recipe/cf90cw-fav4/
        meta {[key,value]}
        parent {hash}
        children {[hash]}
        text.md
        text.html
    """
    def get( self ):
        id = self.get_argument("id")
        if not os.path.exists('/var/recipes/'+id+'/text.html'):
            subprocess.Popen([  '/var/FlavorPages/app/scripts/Markdown.pl', 
                                '/var/recipes/'+id+'/text.md',
                                '/var/recipes/'+id+'/text.html' ]).wait()
        self.render("recipe.html",id=id)

class thanks( tornado.web.RequestHandler ):
    def get( self ):
        self.render( "thanks.html" )






