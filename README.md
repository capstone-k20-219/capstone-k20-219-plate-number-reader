# Automatic number plate recognizer (ANPR)
This is a simple program to simulate a plate-number-extracting camera which is widely used in modern parking lots.  
The program has 2 modes: 1 for vehicle checking in and 1 for vehicle checking out.  

Please follow these steps to run this program on your local machine:
* **Step 1:** Pull this repository to your local machine.
* **Step 2:** Install the packages using this command **pip install -r requirements.txt**.
* **Step 3:** Change .env.example file to .env.
* **Step 4:** Add the Firebase real-time database URL to the .env file. You can find this URL in your Firebase real-time database.
* **Step 5:** Add your credentials.json file to the repository. You can find this file in your Firebase project settings.
* **Step 6:** Run the command **[python | python3 | py] main.py checkin** to use the checkin mode and **[python | python3 | py] main.py checkout** to use the checkout mode.

**Note:** If you haven't had a Firebase real-time database, please create one in advance with the following 3 nodes:
  * plateNumberIn - string type
  * plateNumberOut - string type
  * qrCode - string type
