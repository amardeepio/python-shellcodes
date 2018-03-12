
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def disk_report():
   
    q = subprocess.Popen("df -h ", shell=True,
                    stdout=subprocess.PIPE)
    p = subprocess.Popen("uname -a ",shell=True,stdout=subprocess.PIPE)

    r = subprocess.Popen("ps -eF",shell=True,stdout=subprocess.PIPE)
    
    return q.stdout.readlines() + p.stdout.readlines()+ r.stdout.readlines()



def create_pdf(input,output="disk_report.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11*inch)

    textobject.textLines('''
    the report generated on  : %s
    ''' % date)
    textobject.textLines('''
    created by amardeep:
    ''' )

    textobject.textLines('''
        the user name is :
        ''')
    for line in input:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.showPage()
    c.save()
report = disk_report()
create_pdf(report)