{ pkgs } :{ deps = [
pkgs.python311Full
pkgs.python311Packages.pip
pkgs.python311Packages.setuptools
pkgs.python311Packages.wheel
pkgs.python311Packages.flask  
pkgs.python311Packages.pyTelegramBotAPI
pkgs.python311Packages.openai
    pkgs.python311Packages.python_dotenv
]; }



