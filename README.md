### Project Overview
Stock 'N Shop is a grocery store management application designed to streamline store operations. This 3-tier application leverages Python, Flask, HTML, CSS, JavaScript, and MySQL to provide a user-friendly interface for managing inventory, sales, and customer information.

### Technical Stack
Technical Stack
Front-end: HTML, CSS, JavaScript, Bootstrap
Back-end: Python, Flask
Database: MySQL

### Project Structure
stock_n_shop/
├── backend/
│   ├── orders_dao.py
│   ├── products_dao.py
│   ├── servers.py
│   └── sql_connection.py
│   └── uom_dao.py
├── ui/
│   ├── index.html
│   ├── manageproducts.html
│   ├── order.html
│   └── customers.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── requirements.txt
├── README.md

### Getting Started
Clone the repository:
Bash
git clone https://github.com/amanda-dandure/stock_n_shop.git
Install dependencies:
Bash
pip install -r requirements.txt

### Database
Create a MySQL database: Set up a MySQL database and create a user with appropriate privileges.
Configure database settings: Update the database connection details in the sql_connection.py file.


### Contributing
Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes.
Commit your changes with descriptive commit messages.
Push your changes to your branch.  
Create a pull request to the main branch.

### License
MIT License Copyright (c) 2024 Amanda Dandure Permission is with this granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 


### Additional Notes
Consider using a version control system like Git to track changes and collaborate effectively.
Implement security measures to protect sensitive data.
Consider using a testing framework (e.g., pytest) to ensure code quality.
Explore cloud deployment options (e.g., Heroku, AWS) for scalability.



### Installation Instructions

Download mysql for windows: https://dev.mysql.com/downloads/installer/

`pip install mysql-connector-python`


