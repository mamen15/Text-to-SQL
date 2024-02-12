# Text-to-Query Translator for Data Extraction

## config 
you will find my configuration in : ``` pyvenv.cfg ```
## Description
This project demonstrates a text-to-query translator that allows users to input natural language queries and retrieve data from an SQLite database using Google Gemini. The application utilizes Streamlit to create an interactive web interface.

## Installation
To run this project, ensure you have Python 3 installed on your system. Then, follow these steps:

Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repo.git
```
   
## Navigate to the project directory.
```bash
python3 -m venv venv
```
For Windows:
```bash
venv\Scripts\activate
```
For macOS/Linux:
```bash
Copy code
source venv/bin/activate
```
Install the required Python packages.
```bash
pip install -r requirements.txt
```
Once you have installed the requirements, you can start the Streamlit application by running the following command:

```bash
streamlit run app.py
```
This command will start a local server and open the application in your default web browser. You can then input natural language queries into the provided text box. The application will translate the text into SQL queries using Google Geminai and retrieve the relevant data from the SQLite database.
