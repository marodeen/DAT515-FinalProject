# Design Document

## Overview
The project involves the development of a simple static website featuring a contact form that allows users to submit their feedback. The primary purpose of this application is to demonstrate our ability to integrate various technologies learned during the DAT515 course, including web development, containerization, and cloud computing. By implementing a functional contact form with back-end processing, we aim to showcase our understanding of both front-end and back-end development while leveraging modern cloud services.

## Architecture
The application follows a modular architecture, consisting of several key components that interact seamlessly to deliver a user-friendly experience. At the front end, the website is designed using HTML, CSS, and the Bootstrap framework, which provides a responsive and visually appealing interface. When a user submits the contact form, the data is sent to the Flask application running on the server.

The Flask app handles the form submission by processing the incoming data and storing it in an SQLite3 database. Upon successful data storage, the application generates a JSON response to inform the user that their submission was successful. This response is displayed on a dedicated confirmation page, enhancing user experience by providing immediate feedback.

The interactions between the components can be summarized as follows:
1. The user accesses the static website hosted on an Nginx server.
2. The user fills out and submits the contact form.
3. The form data is sent as a POST request to the Flask application.
4. The Flask app processes the data and stores it in the database.
5. The app emails the user, responds with a JSON confirmation message, and redirects the user to a confirmation page.

## Technologies
The application utilizes several cloud computing technologies and services, including:
- **Amazon Web Services (AWS)**: Specifically, we use the EC2 service to host our web server and application, taking advantage of the free tier for cost-effective deployment.
- **Docker**: Employed for containerization, Docker allows us to package the Nginx server and Flask application into separate containers, simplifying deployment and ensuring consistency across environments.
- **Flask**: A lightweight Python web framework used to handle the back-end functionality, including form processing and database interactions.
- **SQLite3**: A file-based database that stores the form submissions, providing a simple and efficient way to manage data for our application.
- **Nginx**: A high-performance web server that serves the static content of the website and acts as a reverse proxy for the Flask application.

## Deployment
The deployment strategy for the application involves several key steps to ensure a smooth and efficient setup. We begin by provisioning a `t3.micro` EC2 instance on AWS, which serves as the host for our application. The Nginx web server is configured to serve the static HTML and CSS files while forwarding requests to the Flask application.

We utilize Docker Compose to manage the deployment of the application, allowing us to define and run multi-container Docker applications easily. The `docker-compose.yml` file specifies the necessary services, including the Nginx server and the Flask app, ensuring that they can communicate with each other seamlessly.

Additionally, we configure the Nginx server with a reverse proxy to route form submission requests to the Flask application running on port 5001. This setup enables efficient processing of incoming data while keeping the application secure and responsive.

To enhance security, we implement HTTPS using SSL certificates obtained from Let's Encrypt, ensuring that data transmitted between the user and the server is encrypted. Overall, this deployment strategy leverages modern cloud technologies to create a scalable, reliable, and secure web application.

