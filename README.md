Project for Machine Learning Study
=====================================

# Enable Python venv

First of all install python 3.

```
$ cd /your/project/path
$ python3 -m venv env
```

## macOS

```.vscode/setting.json```

```json
{
    "python.pythonPath": "${workspaceFolder}/env/bin/python"
}
```

run venv

```
$ . env /bin/activate 
```

## Windows
```.vscode/setting.json```

```json
{
    "python.pythonPath": "${workspaceFolder}\\env\\Scripts\\python.exe",
    "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
}
```
activate venv
```
PS> python -m venv env
PS> .\env\Scripts\activate
```

# Install Python packages
```
(env)$ pip install numpy
```
