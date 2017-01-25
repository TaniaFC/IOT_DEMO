import web
from web import form 
import pymysql
'''import pyfirmata 
from time import sleep
import os'''

urls=(
    '/','Arduino'    
)

app = web.application(urls, globals())
render = web.template.render('Templates',base='base')

class Arduino:
   
    
    control = form.Form(
        form.Button("Encender/Apagar",type="submit",description="Encender/Apagar")
    )

    def GET(self):
        data = 0
        control = 0
        conn = pymysql.connect(host='wp433upk59nnhpoh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', port=3306, user='thcu5mxhm5bl35ry', passwd='pb9opvshqinr8sd8', db='k0gkgerhx1mejkf4')
        cur = conn.cursor()

        formulario = self.control()
        cur.execute("SELECT * FROM data WHERE id=1")
        conn.commit()        
        for row in cur:
            data=row[2]
        cur.execute("SELECT value FROM control WHERE id=1")
        for row in cur:
            control=row[0]
        cur.close()
        conn.close()
        #return values
        return render.index(data,control, formulario)

    def POST(self):
        control = 0
        conn = pymysql.connect(host='wp433upk59nnhpoh.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', port=3306, user='thcu5mxhm5bl35ry', passwd='pb9opvshqinr8sd8', db='k0gkgerhx1mejkf4')
        cur = conn.cursor()
        formulario= self.control()
        if not formulario.validates():
            pass 
        else:
            cur.execute("SELECT * FROM control WHERE id=1")
            control=''
            for row in cur:
                control=row[2]

            if control == 1:
                control = 0
            else:
                control = 1
            cur.execute("UPDATE control SET value= "+ str(control) +" WHERE id=1")
            conn.commit() 
            raise web.seeother('/')
if __name__=='__main__':
    web.config.debug= True
    app.run()






