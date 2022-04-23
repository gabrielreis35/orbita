### Documentation files
    .
    ├── core                                # Files config django
    │   ├── asgi.py                
    │   ├── settings.py                   
    │   ├── urls.py                   
    │   └── wsgi.py                         
    ├── docs                                # Documentation files
    │   ├── make-commands.md                # Documentation of using the make command
    │   ├── structure.md                    # All project folder and file structure
    │   └── README.md                       # Presentation of the project and how to use it
    ├── nginx-conf                          # Nginx configuration files
    │   └── nginx-dev.conf                  # Nginx configuration file development
    ├── .dockerignore                       # Ignore files/folders from docker trace
    ├── .gitignore                          # Ignore files/folders from git trace
    ├── .gitlab-ci.yml                      # Automation running in gitlab
    ├── dev.Dockerfile                      # File to generate development docker image
    ├── docker-compose.dev.db.yml           # AFile to generate upload the database container
    ├── docker-compose.dev.yml              # File to generate upload django container
    ├── help.py                             # Help file for reading makefile commands in terminal "make help"
    ├── Makefile                            # File to facilitate project command execution
    ├── manage.py                           # Django default file
    ├── README.md                           # Presentation of the project and how to use it
    ├── requirements.dev.txt                # Libraries used in the development project
    ├── reset_passwords.dev.py              # Reset passwords for all project users
    ├── superuser.dev.py                    # Create an admin user when starting the project for the first time
    └── ...