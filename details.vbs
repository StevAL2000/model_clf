Set objShell = CreateObject("WScript.Shell")
currentDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
batFile = currentDir & "\config.bat"
objShell.Run Chr(34) & batFile & Chr(34), 0, True