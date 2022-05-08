# fairytale_sound_effects
#### Authors: Emma Mascillaro, Rucha Dave

## **Project Summary**:
This repository contains our 2022 Software Design Final project which


## **Instructions:**
### **Dependancies:**

In order to collect, clean, and visualize the our data, we utiziled mutliple Python libraries. 

Audio Transcription:
1. SpeechRecognition - `pip install SpeechRecognition`

Data Cleaning:
1. glob - This should come as part of the Python package

Data Visualizing: 
1. geopandas - `pip install geopandas`
2. numpy - `pip install numpy`
3. matplotlib - `pip install matplotlib`

### **Running Scraping:**
All functions needed to scrap Niche are included in the file *niche_web_scraping.py*. 

In order to run this, run the following command in the terminal to navigate to the web_scraping folder: `cd web_scraping`. Run the *runner_scraping.py* file. This will create a folder called *testing* within the web_scraping folder which will contain a folder called *raw_data*, which will have csv files for all the data scraped. 

In order to run the full list of states and obtain all the data, comment line 133 in *niche_web_scraping.py* and uncomment lines 122-131. This will loop through all the states. Because of the timeout errors due to Niche.com's rules, change the states_list variable to include only the states that haven't been scraped yet every time the error occurs. Then, comment out lines 14 and 18 in the *runner_scraping.py* file to stop from remaking the folders. Rerun *runner_scraping.py* once scraping can be resumed.

### **Cleaning Data:**
All functions needed to clean the data files are included in the file *data_cleaning.py*. 

Option 1. To clean the data just collected, navigate back to the *web_scraping* folder by running `cd ..` twice. Here, open *data_cleaning.py* and uncomment line 475. This will navigate to the *testing* directory. Then, comment line 477, which remove previously created files. Uncomment line 485 to create a folder called *cleaned_data* in the *testing* directory and comment lines 487 - 489, which also remove previous files. Uncomment lines 473 and 493. Now, running *data_cleaning.py* in the terminal will create a folder called *cleaned_data* within the *testing* directory that contains all the cleaned files.

Option 2. To clean the complete set of data, navigate back to the web_scraping folder by running `cd ..` twice. Here, run *data_cleaning.py*. This will delete the cleaned csvs in *cleaned_data* that currently exist and replace them with the recleaned versions of the files in *raw_data*. Uncomment lines 473 and 493. Uncomment lines 487, 488, and 489.

### **Visualizing Data:**
All functions needed to visualize the data files are included in the file *data_visualization.py*.

*Disclaimer: To plot with geopandas, values for all states need to be added, which is not possible when using the self-generated data that is present in the testing file. For this reason, only the first 3 graphs will be seen if plotting with the shorter data. However, using the full raw_data as explained in option 2 will generate all of the plots.*

#### **Setting Up:**
1. Open the GitHub link listed above
2. From here, download the 3 files listed above and move them to the *testing* folder. Inside this folder, move them to the *cleaned_data* folder.

#### **Visualizing:**
Option 1. To visualize the cleaned data for the shorter set that was scraped just now, navigate back to the *web_scraping* directory. Open the file called *data_visualization.py* and uncomment line 15 to navigate to the *testing* folder. Comment out lines 64, 65, 219, 220, 338, and 339. Finally, add `"""` to lines 202 and 333 to comment out the functions that create the US-map graphs, because they cannot be made with data from simply 2 states, as explained above. Navigate back out to *niche_major_finder* and run `python web_scraping\data_visualization.py`.

Option 2. To visualize our complete set of data, simply navigate back to the *niche_major_finder* directory and run `python web_scraping\data_visualization.py`.
