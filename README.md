

## Dependencies

The project requires the following Python packages:

- `Django>=4.2`
- `djangorestframework>=3.14`
- `mysqlclient>=2.3` (only if using MySQL)


##  Installation & Setup

Follow these commands step by step to set up and run the project:

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <project-folder>

# 2. Create a virtual environment
python -m venv env

# 3. Activate the virtual environment
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py makemigrations
python manage.py migrate

# 6. Run the development server
python manage.py runserver


## API Endpoints
- GET /students/ → list all
- GET /students?rollno=101 → filter by roll number
- GET /students?department=CSE → filter by department
- GET /students?rollno=101&department=CSE → filter by both
