Project for Machine Learning Study
=====================================

# enable virtual env
install python 3

## macOS

```.vscode/setting.json```

```json
{
    "python.pythonPath": "env/bin/python"
}
```

run venv

```
$ python3 -m venv env
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
run venv
```
PS> python -m venv env
PS> .\env\Scripts\activate
```


# pip install
```
(env)$ pip install numpy
```