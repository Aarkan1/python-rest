# python-rest
Sanic webserver in Python, SQLite as database and Vue as frontend

## Getting started
```
1. open terminal
2. create a virtual environment and enable it
2.1 py -m venv sanic
2.2 
  Windows -> sanic\Scripts\activate.bat
  Unix or MacOS -> source sanic/bin/activate
3. py -m pip install sanic databases[sqlite]
  if error: "Microsoft Visual C++ 14.0 is required"
  install https://aka.ms/vs/16/release/vs_buildtools.exe
  check C++ build tools "MSVC - VS 2019 C++ x64/x86.." and "C++ CMake.."
2. py main.py
3. go to http://127.0.0.1:5000
```

## Frontend
```
1. cd frontend
2. npm install
3. npm run dev
```
