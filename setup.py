from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "sys", "commands"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "YBPMT",
    options = options,
    version = "v1.0",
    description = 'Mayor Release',
    executables = executables
)