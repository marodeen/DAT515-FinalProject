# Project README

## Overview
This project is a simple static website featuring a contact form that allows users to submit their feedback. The application is deployed on an AWS EC2 instance using Docker for containerization.

## Instructions for Building and Deploying

1. **Start the EC2 Instance**
   - Log in to the AWS Management Console.
   - Navigate to the EC2 service.
   - Start the `t3.micro` EC2 instance configured for this project.

2. **SSH into the Instance**
   - Use your terminal to SSH into the EC2 instance.

3. **Navigate to the Project Directory**
   - The project files, in this case, are located on the home directory:
     ```bash
     cd 
     ```

4. **Run Docker Compose**
   - Execute the following command to build and start the application:
     ```bash
     docker compose up
     ```

5. **Access the Application**
   - Open your web browser and navigate to `marodeen.com` to access the website.

