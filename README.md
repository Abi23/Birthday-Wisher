# Monday Motivation #
Email motivational quotes on a specific day of the week. This code can be edited to send other messages like birthday wishes by replacing the quotes.txt


## Setup Instructions ##

- Create a secret.json file with the following key-value pairs

    - from_email: The email you want to send the message from.
    - from_password: The app password not your email password. Generate app password from your email provider.
    - to_email: The email you want to send it to.

        ```
        {
            "from_email": "example@gmail.com",
            "from_password": "",
            "to_email": "friend@yahoo.com"
        }
        ```

- Non Gmail Accounts:

    - If your 'from email' is not gmail, please edit and add the correct SMTP server and port. 
