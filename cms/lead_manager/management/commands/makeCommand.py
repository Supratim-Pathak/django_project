import os
from django.core.management.base import BaseCommand, CommandError
from cms.settings import INSTALLED_APPS


class Command(BaseCommand):
    help = '\t\t\t\t-*-*-*-*-*-*-Makes coustom Command-*-*-*-*-*-*-\n\n\n'+'(This command takes optional arguments --name YourAppName CommandName)'

    def add_arguments(self, parser):
        parser.add_argument('--name', nargs='+', type=str)

    def handle(self, *args, **options):
        
        app_name = options.get('name')[0]
        file_name = options.get('name')[1]
        full_path = f"{app_name}/management/commands/{file_name}.py"
        
        code = ['from django.core.management.base import BaseCommand, CommandError\n','\n','class Command(BaseCommand):\n\t',f'help = \'Help Text For Command\'\n','\n\t','def add_arguments(self, parser):\n\t\t','parser.add_argument(\'--arguments\', nargs=\'+\', type=int)\n\t','def handle(self, *args, **options):\n\t\tprint("Hi , I Am All Yours Baby ♥ ♥ ♥ ♥ ♥ !!!")']
        
        if app_name in INSTALLED_APPS:
            
            if os.path.isfile(full_path)==False:
                with open(full_path, 'w') as file:
                    file.writelines(code)
                print(f"{file_name} Command Created")
            else:
                print(f"{file_name} Command Already Created")
            
        else:
            print("Invalid AppName")
        