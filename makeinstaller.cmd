set pyzbar=%USERPROFILE%\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyzbar
pyinstaller.exe --add-binary %pyzbar%\libiconv.dll;. --add-binary %pyzbar%\libzbar-64.dll;. --onefile QRscan.py
pause