# AI-Based Smart Parking System (Vercel-ready)

A browser-based version of the desktop Smart Parking System. It retains the CSP slot selection and parking manager logic while replacing the CustomTkinter interface with a Flask website.

## Run locally (Windows)

1. Install Python.
2. Open PowerShell in this folder.
3. Run `py -m pip install -r requirements.txt`
4. Run `py app.py`
5. Open http://127.0.0.1:5000

## Deploy to Vercel

1. Upload all files/folders in this project to a GitHub repository.
2. Sign in at https://vercel.com and choose **Add New → Project**.
3. Import the GitHub repository.
4. Let Vercel detect the Python/Flask app and deploy.
5. Open the URL Vercel provides.

## Important limitation

The supplied sample parking data is stored in Python memory and includes two preoccupied sample slots. Vercel can run multiple serverless instances, so this demo is not suitable for real multi-user parking management without a persistent database. Use a database such as Vercel Postgres/Neon/Supabase for shared, persistent records.
