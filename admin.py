from django.contrib import admin
from .models import UserItem
# Register your models here.

@admin.register(UserItem)
class UserAdmin(admin.ModelAdmin):
    list_display = ('item_number','item_name','item_quantity')


    
def show_printers(request):
    try:
        dc = win32ui.CreateDC()
        printername = win32print.GetDefaultPrinter()
        dc.CreatePrinterDC(onenote)
        dc.SetMapMode(win32con.MM_TWIPS)
        scale_factor = 20
        dc.StartDoc('Win32print test')
        pen = win32ui.CreatePen(0, int(scale_factor), 0)
        dc.SelectObject(pen)
        font = win32ui.CreateFont({
            "name": "Lucida Console",
            "height": int(scale_factor * 10),
            "weight": 400,
        })
        dc.SelectObject(font)
        dc.TextOut(scale_factor * 72,
                   -1 * scale_factor * 72,
                   "Testing...")
        dc.MoveTo((scale_factor * 72, scale_factor * -72))
        dc.LineTo((scale_factor * 6 * 72, scale_factor * 3 * -72))
        dc.EndDoc()
    except:
        print(traceback.print_exc())
        
        
   https://stackoverflow.com/questions/57052994/how-to-create-a-print-dialog-box-in-python3
