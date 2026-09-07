from octo.handler.command import Command


class StartApp(Command):
    """Create a django app inside the app/"""

    def __init__(self):
        super().__init__()
        self.use_django = False

    def handle(self):
        # === import =====================================
        import os
        import subprocess

        from colorama import Fore, Style, init

        from octo.base import BASE_DIR as octo_dir
        from octo.base import _error_structure

        init()
        # === Logic ======================================
        APP_DIR = os.getcwd() + "/app"

        if not os.path.exists(APP_DIR):
            raise ValueError(Fore.RED + _error_structure + Style.RESET_ALL)

        os.chdir(APP_DIR)

        if len(self._argv) > 2:
            app_name = self._argv[2]
            subprocess.run(
                [
                    "django-admin",
                    "startapp",
                    f"{app_name}",
                    f"--template={octo_dir}/conf/app_template",
                ]
            )
        else:
            print(
                Fore.RED
                + "\n"
                + "You must enter the application name"
                + Fore.GREEN
                + "\n"
                + "octo startapp app_name"
                + Style.RESET_ALL
            )
