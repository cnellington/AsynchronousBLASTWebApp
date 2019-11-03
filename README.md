# Ginkgo Backend Challenge
#### Description
A simple React-Django webapp to query DNA sequences against a databank of .fasta files.
#### Features
* Persistent anonymous user sessions
* Asynchronous query processing
* Constantly updating results
* REST-ful backend api
* Intuitive build tools
---
### Setup
This setup is for linux machines. It requires ```python, npm, and virtualenv```
1. Navigate to the directory you'd like to use
2. ```git clone https://github.com/cnellington/GinkgoBackendChallenge.git```
3. Start a new python3 virtual environment with ```virtualenv venv```
4. ```pip install -r requirements.txt```
5. ```npm install package.json```
6. Edit the runserver and django-q commands in ```conf/supervisord.conf``` to have a path to your ```gingoapp/manage.py```
7. Give the build command permissions with ```chmod -x build.sh```
8. Run ```./build.sh``` to build the application! (There might be a few errors the first time)
9. Create a new admin with ```python ginkgoapp/manage.py createsuperuser```
10. Go to ```localhost:8000/admin/``` in your brower and log in
11. Add all of your .fasta files under the Protein object. Save them, and they should be labeled "unprocessed"
12. Run ```python ginkgoapp/manage.py populate_proteins``` to process all of the .fasta files
13. Run ```./build.sh``` again, and your server should be ready to go!
14. If running on an external server, you'll need to edit ```conf/config.json``` to have the correct properties. 
