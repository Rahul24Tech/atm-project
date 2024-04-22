# ATM Site Management

This project is a Django application for managing ATM site data. It allows users to upload site data using Excel files, manage data through an interface, and view site details on web pages.

## Features

- **ATMSite Management**: Manage ATM site data including name, site ID, address, state, city, and contact details.
- **State and City Management**: Manage state and city data to associate with ATM sites.
- **Excel File Upload**: Upload ATM site data using an Excel file with specified columns.
- **Web Interface**: View and manage ATM site data through web pages.

## Prerequisites

- Python 3.x
- Django 4.x
- Openpyxl (for Excel file handling)

## Getting Started

1. Clone the repository:

    ```shell
    git clone https://github.com/yourusername/atm_site_management.git
    cd atm_site_management
    ```

2. Create and activate a virtual environment:

    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```shell
    pip install -r requirements.txt
    ```

4. Set up the Django project:

    - Make migrations and migrate to set up the database:

        ```shell
        python manage.py makemigrations
        python manage.py migrate
        ```

    - Create a superuser:

        ```shell
        python manage.py createsuperuser
        ```

5. Run the development server:

    ```shell
    python manage.py runserver
    ```

6. Access the application:

    - Visit the following URLs:
        - `http://localhost:8000/` for the main page.
        - `http://localhost:8000/admin/` for the admin panel.

## Usage

- **Upload Excel File**: Navigate to `http://localhost:8000/upload/` to upload an Excel file with ATM site data.
- **View ATM Sites**: Navigate to `http://localhost:8000/sites/` to view and manage ATM sites.
- **Admin Panel**: Log in to the admin panel at `http://localhost:8000/admin/` to manage models.

## Excel File Format

The Excel file for uploading ATM site data should have the following columns in the specified order:

- Name
- ID
- Address
- State
- City
- Person Name
- Phone
- Email

## Contributing

Contributions are welcome! If you encounter any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses open-source packages such as Django and Openpyxl. Thank you to the contributors of these projects.
