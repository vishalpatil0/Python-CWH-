from cx_Freeze import setup, Executable
		setup(name="vishal",
    		  version="0.1",
     		 description="ok",
     	 options={"build_exe": {"packages": ["pygame","random","os","sys"], "include_files": ["images/","sounds/","ico/"]}},
     	 executables=[Executable(r"Snake.py",
                                base = "Win32GUI",
                                icon="ico/logo.ico",
                                shortcutName="Snake",
				shortcutDir="DesktopFolder")]
      )

    # base ="Win32GUI hides the console window
