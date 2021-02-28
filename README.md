# python-rest
Sanic webserver in Python, SQLite as database and Vue as frontend

## Getting started
```
1. open terminal
2. create a virtual environment (see Read more)
3. py -m pip install sanic databases[sqlite]
   if error: see Read more
2. py main.py
3. go to http://127.0.0.1:5000
```

## Frontend
```
1. cd frontend
2. npm install
3. npm run dev
```

## Packages used
[Sanic](https://sanic.readthedocs.io/en/latest/index.html)
[databases](https://www.encode.io/databases/)

## Read more
### Create a virtual environment and manage it
1. py -m venv sanic
2. 
  Windows -> sanic\Scripts\activate.bat
  Unix or MacOS -> source sanic/bin/activate

[Official docs on virtual environments](https://docs.python.org/3/tutorial/venv.html)

### Getting error: "Microsoft Visual C++ 14.0 is required"?
Install [vs_buildtools](https://aka.ms/vs/16/release/vs_buildtools.exe)

Check C++ build tools and enable optional: 
[x] "MSVC - VS 2019 C++ x64/x86..",
[x] "C++ CMake.."
