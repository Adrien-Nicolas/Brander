# Brander
Brander is a brand style wizard that provides users with a comprehensive set of tools to create their own brand style. 


# API key

First, make sure you have a valid OpenAI key.
The API key must be placed in the location provided for this purpose in the file: 
- [view.py] (./Back/brander/api/view.py)

```python
#------------------Put your API key here----------------------
    openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


# Install dependencies 

Before using anything, be sure to install the necessary requirements for the Back and Front side.

## Back side :

```bash
cd ./Brander/Back/
pip install -r requirement.txt
```

## Front side :

```bash
cd ./Brander/Front/
cat requirements.txt | xargs npm install -g
```


# Launching
## Back
In a terminal :

```bash
export SECRET_KEY=yoursecretkey
cd ./Brander/Back
source env/bin/activate
python3 manage.py runserver 8081
```
## Front
In another terminal :

```bash
cd ./Brander/Front/brander
npm run serve -- --port 8080
```





