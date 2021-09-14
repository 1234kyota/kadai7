import eel
import desktop
import trans

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def context_translate(context,before_translate,after_translate):
    trans.context_translate(context,before_translate,after_translate)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)