<h1> Stock 'N Shop</h1>
<h3>Table of Contents</h3>

* Project Description
* Project Goals
* Technologies Used
* Getting Started
  <ol>
    <li>Clone the Repository</li>
    <li>Install Dependencies</li>
    <li>Database Setup</li>
  </ol>
* Features
  <ol>
    <li>Manage Products</li></li>
    <li>Add New Product</li>
    <li>New Order</li>
  </ol>   
* Authors
* Additional Notes
* Licensing
* Installation Instructions
  
<p> <u>Project Name:</u> Stock 'n Shop <br>Project Description: Stock 'n Shop is an online platform that provides an easy and convenient way for customers to shop for groceries and household items. With Stock 'n Shop, customers can create shopping lists, browse through a variety of products, and place orders for delivery or pickup. </p>

<p><u>Project Goals:</u><br>To create a user-friendly platform that makes grocery shopping more convenient and enjoyable for customers. To provide a wide variety of products at competitive prices.</p>

![1](https://github.com/user-attachments/assets/23e03259-9a53-4457-bb7f-4660acb2c98d)
<hr>
<h3>Build with</h3>
<b>Front-end:</b>
<ul>
  <li>HTML: Provides structure and content for the web page.</li>
  <li>CSS: Styles the web page, controlling its appearance.</li>
  <li>JavaScript: Adds interactivity to the web page.</li>
  <li>Bootstrap: Provides a responsive layout and a set of predefined components.</li>
</ul>
<b>Back-end:</b>
<ul>
  <li>Python: A high-level programming language for building the server-side logic.</li>
  <li>Flask: A lightweight web framework for Python, allowing for the creation of web applications.</li>
</ul>
<b>Database:</b>
<ul>
  <li>MySQL: A relational database management system for storing and retrieving data.</li>
</ul>
<b>APIs:</b>
<ul>
  <li>Python Requests: A library for making HTTP requests in Python.</li>
  <li>JSON: A format for exchanging data between web services and applications.</li>
  <li>MySQL Connector: A Python library for connecting to a MySQL database.</li>
</ul>
<hr>
<h3>Getting Started</h3>
<u>Clone the repository:</u>
Bash
<i>git clone https://github.com/amanda-dandure/stock_n_shop.git</i>
<u>Install dependencies:</u>
Bash
<i>pip install -r requirements.txt</i>
<u>Database</u>
<ol>
  <li>Create a MySQL database: Set up a MySQL database and create a user with appropriate privileges.</li>
  <li>Configure database settings: Update the database connection details in the sql_connection.py file.</li>
</ol>
<hr>
<h3>Features</h3>
<p>The <b>Manage Products</b> page is where you, as the Stock 'n Shop administrator, can view and manage all the products available on the platform. You have the ability to add, edit, or delete products as needed to ensure that the selection of products offered to customers is up-to-date and diverse. <br>
The <b>Add New Product</b> button is where you can create a new product entry for the platform. When you click this button, you will likely be presented with a form that will ask you for information about the new product, such as its name, description, price, and any other relevant details.</p>

![2](https://github.com/user-attachments/assets/7d36a1f6-32d2-4a49-a62e-7e7bef6e3e98)



<p>The <b> New Order </b>page is where customers can place orders for the products they want to purchase. This page will likely contain a form that allows customers to enter their order details, including the products they want to buy and their delivery or pickup preferences. <br>
Once the customer has added the desired products to their order, they will be able to review the order summary, which will show the total price of the order, as well as any applicable taxes or delivery fees. The customer can then choose to confirm the order and proceed to the payment page, where they will be able to enter their payment information and complete the transaction.</p>

![3](https://github.com/user-attachments/assets/7c8ceb43-982e-4960-8155-123e681137c5)
<hr>
<h3>Authors</h3>
<a href="https://github.com/amanda-dandure">Amanda Dandure</a>
<ul>
  <li>Project Lead - responsible for managing, overseeing the development, and ensuring the application aligns with the project's goals.</li>
  <li>Backend Developer - responsible for creating the system's backend architecture, and ensuring data security and integrity.</li>
  <li>Frontend Developer - responsible for designing and implementing the user interface, ensuring the system is easy to use and visually appealing.</li>
</ul>
<hr>
<h3> Additional Notes</h3>
<p>Consider using a version control system like Git to track changes and collaborate effectively. <br>
Implement security measures to protect sensitive data.<br>
Consider using a testing framework (e.g., pytest) to ensure code quality.<br>
Explore cloud deployment options (e.g., Heroku, AWS) for scalability. </p>
<hr>
<h3>Licensing</h3>
This project is licensed under the <a href="https://opensource.org/license/MIT">MIT License</a>.
<hr>

<h3>Installation Instructions (MySQL for Windows):</h3>
1. Download MySQL from [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/).
2. Install the downloaded package.
3. Run `pip install mysql-connector-python` to install the connector library.

