# encoding=utf8

import sae
from bottle import Bottle, route, run, template, request, response, post, get, static_file, debug
import sae.const
import MySQLdb
import time

#get db connection
def get_conn():
    # 'charaset' should be set to the encoding of the corresponding database  
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from diary0")
    data = cursor.fetchall()
    conn.close()
    return data

def writeDiary(receivedDiary): 
    conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("insert into diary0 (ts, diary) values (%s, %s)",
                   (time.strftime('%Y-%m-%d %H:%M:%S'), receivedDiary))
    conn.commit()
    conn.close()

# template.
d_tpl = '''
           <html>
           <head>
           <style>
           body {
               background-image: url("http://i.imgur.com/i3OA2PJ.jpg");
               background-repeat: repeat;
               background-position: rigt top;
               margin-right: 200px;
           }
           </style>
           </head>
           <body text="white">
           Welcome!<br><br>
           <form action="/" method="post">
            Input your online diary here: <input name="newdiary" type="text" />
            <input value="Submit" name="do_submit" type="submit">
            </form>
            <p>Hi there, here's your current diary collection:</p>
            <p>
            % for line in d:
            {{str(line[0])}}<br>{{str(line[1])}}<br><br>
            % end
            </p>
            </body>
           </html>'''

#create a Bottle object 'app', and map all functions to app's URL    
app = Bottle()
debug(True)

@app.get('/')
def web_index():
    return template(d_tpl, d = get_conn())

@app.get('/static/<filename:path>')
def sever_static(filename):
    return static_file(filename, root = '')    
    
@app.post('/')
def newDiary():
    #getValue = request.POST.decode('utf-8')
    nd = request.POST.get('newdiary')
    if nd:
        writeDiary(nd)
    return template(d_tpl, d = get_conn())

application = sae.create_wsgi_app(app)


