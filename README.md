# Simple Forum
Simple Forum using Python Flask and Bootstrap CSS

# How to run it (explanation for windows only):
1. Download, extract, and open simple_forum_v1.0+
2. Create a virtual environment in the directory using cmd: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate.bat`
4. Install the dependencies: `pip install -r requirements.txt`
5. Use an IDE and run `run.py`:
   - PyCharm: https://www.jetbrains.com/pycharm/ 
   - VSCode: https://code.visualstudio.com/ 
6. There should be a clickable IP in the IDE, or simply go to any web browser and type in `127.0.0.1:5000`

## Additional info
1. Uses Python 3.9
2. See `accounts.txt` for all the available users
3. Go to `/admin` to go into admin panel, make sure the logged in user is admin or else it will return a 403
