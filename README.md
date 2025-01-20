# osu! Beatmap Downloader
A lightweight tool for mass downloading beatmapsets for rhythm game Osu!.

# Prerequisites
## **Setup Python**  
   
   Ensure Python is installed and added to your system's PATH environment variables. This allows you to run `python` commands in the terminal.

## **Package Installation**  
   Install the required dependencies using `requirements.txt`. It's recommended to use a virtual environment to avoid polluting your environment:  
   ```bash
   # optional 
   python -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate      # On Windows

   # mandatory
   pip install -r requirements.txt
   ```

## **OAuth Configuration**  
   To use the API for searching beatmaps, you need to set up an OAuth client:
   
   
   Go to your [osu! account settings](https://osu.ppy.sh/home/account/edit#oauth), and click **New OAuth Application**.\
   Provide any name for your application and save it, and copy the generated **Client ID** and **Client Secret**.
   
   Paste these values into the **config.json file in the corresponding fields.**
   
> ### Optional Configurations 
> You can specify custom paths in config.json for saving various data (e.g., beatmap IDs). If the specified file or folder doesn't exist, the script will create it automatically.
> If the specified file or folder does not exist, the script will create it automatically.

> All specified path in config.json are in relative paths format

---
# Usage
### Copy your osu!.db file (in your osu! folder) to the directory specified in config.json.

Run the main script using:
``bash
python main.py``

Once the terminal progress bar completes, the downloaded beatmapsets will be available in the **download folder configured in config.json.**

---

> A huge set of ranked mapset ids (around 28,000 mapsets) has been prefetched into beatmapset_ids.txt in this repository, so you don't have to refetch it

> You can also customize the query type by editing the urlretrieve query in download.py
## Contributions

This project leverages several useful open-source tools and libraries that have greatly contributed to its functionality:

- **[jaasonw/osu-db-tools](https://github.com/jaasonw/osu-db-tools)**: provides essential tools for reading and working with the osu!db binary files.
  
- **[tybug/ossapi](https://github.com/tybug/ossapi)**: A Python wrapper for the osu! API, which simplifies the process of integrating osu! API functionality into Python.

> If you have any question please contact **aquatic0** on discord or **hsuehchihchung@gmail.com**

[<img src = "https://github.com/Aquatictw.png?size=70"/>](https://aquatictw.com)
