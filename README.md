# DeliciousBite

![DeliciousBite_logo](./Menu/static/Menu/images/DeliciousBite_logo.png)

## Overview
DeliciousBite is a comprehensive restaurant menu management system built using Django, a high-level Python web framework. It offers a seamless platform for restaurant owners and managers to showcase their menu items, provide detailed descriptions, and engage with customers effectively. With DeliciousBite, users can effortlessly browse through a variety of dishes, access nutritional information, and even generate QR codes for quick access to the restaurant's online menu. The application boasts a user-friendly interface, making it convenient for both restaurant staff and customers to interact with the menu and explore the culinary offerings. Whether you're a small cafe or a fine dining establishment, DeliciousBite provides the tools you need to elevate your online presence and streamline menu management.

## QR Code
![DeliciousBite QR Code](./QR_code/qr.png)

## Features
- **Menu List**: Displays a list of menu items ordered by date created.
- **Menu Item Detail**: Provides detailed information about each menu item.
- **About Page**: Presents information about the restaurant and its philosophy.

## Technologies Used
- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities.
- **qrcode**: A library for generating QR codes.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as `URL` in `generate_qr.py`.
5. Run the script `generate_qr.py` to generate a QR code for the specified URL.
6. Run the Django server using `python manage.py runserver`.

## Usage
1. Access the home page by navigating to the root URL.
2. View details of a specific menu item by clicking on it from the menu list.
3. Explore the about page to learn more about the restaurant.

## Additional Setup Steps
- Ensure the Django database is configured and migrations are applied.
- Customize the about page content in `views.py` to match your restaurant's information.

## QR Code Generation
- Use the `generate_qr.py` script to generate a QR code for the application.
- Adjust the URL variable in the script (`URL = "http://127.0.0.1:8000/"`) to change the URL encoded into the QR code.

## Admin Interface
- Access the Django admin interface by navigating to `/admin`.
- Use the following default admin user credentials:
  - Username: `admin`
  - Password: `pass123`
- Once logged in, the admin user can create more users and add data to the database using the interface.

## Room for Improvement
- The appearance and GUI of the application can be enhanced further to improve user experience.
- Consider incorporating modern design principles, responsive layouts, and intuitive navigation for a more visually appealing interface.

## Note
- Views are implemented as class-based views rather than functions, providing flexibility and organization in handling requests and responses.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.

