from cx_Freeze import setup, Executable
setup(name="vishal",
      version="0.1",
      description="ok",
      executables=[Executable(r"stone-paper-scisor1.py",base = "Win32GUI")]
      )
#this base="Win32GUI" hides the console window
