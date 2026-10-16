Option Explicit
Dim sh, fso, project, py, cmd
Set sh = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
project = "D:\ArcSafeStudio"
If Not fso.FileExists(project & "\main.py") Then
  MsgBox "ArcSafe Studio folder was not found at D:\ArcSafeStudio." & vbCrLf & "Please keep the project files inside that folder.", vbExclamation, "ArcSafe Studio"
  WScript.Quit 1
End If
If fso.FileExists(project & "\venv\Scripts\python.exe") Then
  py = """" & project & "\venv\Scripts\python.exe"""
Else
  py = "python"
End If
' Start both local servers hidden, then open the browser.
cmd = "cmd /c cd /d """ & project & """ && " & py & " -m uvicorn main:app --host 127.0.0.1 --port 8000"
sh.Run cmd, 0, False
WScript.Sleep 1800
cmd = "cmd /c cd /d """ & project & """ && " & py & " -m http.server 5500 --bind 127.0.0.1"
sh.Run cmd, 0, False
WScript.Sleep 1200
sh.Run "http://127.0.0.1:5500/index.html", 1, False
