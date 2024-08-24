# Norman Site

A Django-based website for a political candidate.

## Setup Instructions

### Using Virtual Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/Normantshuma1/Capstone10
   cd norman_site
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t norman_site .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 norman_site
   ```

## Secrets and Environment Variables

Please note that you need to configure the `.env` file with the necessary secrets (e.g., `SECRET_KEY`, `DATABASE_URL`). Ensure these are not committed to the repository.

## Documentation

You can find the project documentation in the `docs` folder.
