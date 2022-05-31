
#First of all idk what i'm doing here. So Enjoy my ugly ass codes.

#import modules
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.text import Text
import time
import qrcode
import os

console = Console()

#menu screen
table = Table(title = '''  ██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗
  ██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║   ██║██████╔╝██║     ██║   ██║██║  ██║█████╗  
██║▄▄ ██║██╔══██╗██║     ██║   ██║██║  ██║██╔══╝  
 ╚██████╔╝██║  ██║╚██████╗╚██████╔╝██████╔╝███████╗
  ╚══▀▀═╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
''')
table.add_column('Option', style = 'cyan')
table.add_column('################', style = 'magenta')
table.add_column('Description', style = 'green')
table.add_row('1', 'QRcode Generator', 'Generate a QRcode out of any text/link.')
# table.add_row('2', 'Credits', 'Creator credits.')
table.add_row('2', 'Exit', f'\n[bold blue]Created by Addi[/]\n[bold blue]website:[/] [bold orange]https://www.add1.info/[/]')

#Text customize
# line_1 = console.Text('Please make a choice>> ', style = 'red')
line_2 = Text('Enter: ', style = 'red')

#first function
def table_1():
    console.print(table)
    console.print('')
    

#option1 menu
option1_table = Table(title = '''   ██████╗ ██████╗  ██████╗ ██████╗ ██████╗ ███████╗
  ██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║   ██║██████╔╝██║     ██║   ██║██║  ██║█████╗  
██║▄▄ ██║██╔══██╗██║     ██║   ██║██║  ██║██╔══╝  
  ╚██████╔╝██║  ██║╚██████╗╚██████╔╝██████╔╝███████╗
   ╚══▀▀═╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
''')
option1_table.add_column('How to use it?', style = 'red')
option1_table.add_row('Please enter what you want to convert into a QRcode!')

#credit menu 
credit_table = Table(title = '\n')
credit_table.add_column('Creator', style = 'green')
credit_table.add_row(' - Addi')

#clear screen function
def clear_console():
    os.system('cls')
    
#progress bar function 
def progress_bar():
    for i in track(range(10), description = 'Generating...'):
        time.sleep(0.05)

#qrcode function
    qr = qrcode.QRCode(
        version = 1,
        box_size = 15,
        border = 4)
    qr.make(fit = True)

#application function
def op_1():
        clear_console()
        console.print(option1_table)
        print('')
        usr_choice = input(line_2)
        choices = usr_choice
        qr = qrcode.QRCode(
        version = 1,
        box_size = 15,
        border = 4)
        qr.make(fit = True)
        qr.add_data(choices)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qrcode.png')
        clear_console()
        print('')
        progress_bar()
        print('')
        console.print('#############################[bold]Success[/]###############################', style = 'green')
        print('')
        console.print('                       Thanks you for using!', style = 'bold blue')
        print('')
        console.print('###################################################################', style = 'green')
        print('')
        console.print('Image Saved.', style = 'bold green')
        print('')
        print('')
        console.print('Exiting...', style = 'bold red')
        print('')
        
        
# def op_2():
#         console.print(credit_table)
#         print('')
#         usr_input = input('Type anything to go back to menu: ')
#         print('')
#         if usr_input == True: 
#             clear_console()
#             app()
        
        
def op_3():
        clear_console()
        print('')
        console.print('###################################################################', style = 'green')
        print('')
        console.print('                       Thanks you for using!', style = 'bold blue')
        print('')
        console.print('###################################################################', style = 'green')
        print('')
        print('')
        console.print('Exiting...', style = 'bold red')
        print('')
        quit()
        
def err_handler():
    clear_console()
    console.print('Unkown option! Unkown option! Unkown option! Unkown option! Unkown option! ', style = 'bold red')
    app()
        
#app
def app():
    table_1()
    #asking user choice    
    option = console.input('Please make a choice>> ')
    print('')
    if option == '1':
        op_1()
    # elif option == '2':
    #     op_2()
    elif option == '2':
        op_3()
    else:
        err_handler()


app()