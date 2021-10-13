## Quick start for beginning

---

- # Download Project

- Clone the repository or download and extract the `.zip` file, for local deployment, from github:
![ques51](https://user-images.githubusercontent.com/28010398/137069077-cec9f655-3f76-460c-a391-4b186ac73758.png)

- Project uses Python==3.8.11

---
# 1. Installation

- # Dockerfile (Recommended)

- `cd` into the `longevity-task1-main` directory, where the `Dockerfile` , `.dockerignore`, etc. are present and run the following commands: 

  ``` 
  docker build -t django_drf .
  docker run -it -p 8000:8000  -v src:/code --name django_drf_app django_drf
  ```
- You need to run `docker build` only the first time of setting up.

- Use the following command to stop the container:
  ```
  docker stop django_drf_app
  ```
- Use the following command to start the container again:
  ```
  docker start -i django_drf_app
  ```

- Note :  More information about `Docker` goto [here.](https://docs.docker.com/get-started/)

- # Windows

- `cd` into the `longevity-task1-main` directory, where the `requirements.txt` , `.dockerignore`, etc. are present.

- create a python virtual environment using `conda` or `venv`
  ``` 
  conda create --name drf_venv python=3.8
  conda activate drf_venv
  pip install -r requirements.txt
  ```
  or
  ``` 
  pip install virtualenv
  virtualenv drf_venv
  drf_venv\Scripts\activate
  pip install -r requirements.txt
  ```

- # Linux

- `cd` into the `longevity-task1-main` directory, where the `requirements.txt` , `.dockerignore`, etc. are present.

  ``` 
  pip3 install --upgrade pip
  python3 -m pip install --user virtualenv
  python3 -m venv env
  source env/bin/activate
  python3 -m pip install --upgrade setuptools
  apt-get update
  apt-get install -y --no-install-recommends python3-dev python3-tk
  pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.33.2
  pip3 install wheel
  pip3 install -r requirements_docker.txt
  ```

---

# 2. Setup (Skip this step if you're using Docker)

- To setup the local project and get your api running run the following commands:
 
  ```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py seed
  python manage.py runserver 8000
  ```
---

# 3. Run and test the api

- The api will be up and running at http://localhost:8000. You can login at http://localhost:8000/admin using admin username and password specified in the `.env` file under the `lg_api` folder.
- In order to access the api endpoints, you would require an authentication token string which can be gotten by making a `POST` request to the localhost:8000/auth/ with the username and passwords. Three demo users are prepopulated for the use of api. The emails are: "user1@gmail.com, user2@gmail.com, user3@gmail.com". Passwords for all three: `"user@123"`.
![ques52](https://user-images.githubusercontent.com/28010398/137075130-58bf6d10-0d78-42a2-a45f-8bb7a1b232fb.png)

- The obtained auth token string will be used in the request headers to access the GetRisks API:
![ques53](https://user-images.githubusercontent.com/28010398/137075538-e8e0a8d4-b757-41c5-86d8-c010d604062c.png)

- To access the GetRisks send a `GET` request to http://localhost:8000/market/getrisks/. Do it for different users/auth token strings and different response will be returned.

- Swagger support is integrated with the api and can be accessed under http://localhost:8000/redoc, http://localhost:8000/swagger 

Note :  More information about `swagger` goto [here.](https://drf-yasg.readthedocs.io/en/stable/)

---
