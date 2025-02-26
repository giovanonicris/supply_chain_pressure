import pandas as pd
from io import BytesIO
import requests

# URL of the GSCPI Excel file
url = 'https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/gscpi_data.xlsx'

# Download the file
response = requests.get(url)
if response.status_code == 200:
    data = BytesIO(response.content)
    
    # Load Excel file and list all sheet names
    xls = pd.ExcelFile
#######

# import requests
# import pandas as pd
# from io import BytesIO

# # URL of the GSCPI data file
# gscpi_url = 'https://www.newyorkfed.org/medialibrary/research/interactives/gscpi/downloads/gscpi_data.xlsx'

# def download_gscpi_data():
#     response = requests.get(gscpi_url)
#     if response.status_code == 200:
#         data = BytesIO(response.content)
        
#         # List available sheets before reading
#         xls = pd.ExcelFile(data)
#         print("Available sheets:", xls.sheet_names)  # Debugging step
        
#         # Pick the first sheet dynamically
#         sheet_name = xls.sheet_names[0]
        
#         # Read the sheet
#         df = pd.read_excel(xls, sheet_name=sheet_name)
        
#         # Save to CSV
#         output_file = 'gscpi_data.csv'
#         df.to_csv(output_file, index=False)
#         print(f"GSCPI data successfully saved to {output_file}")
#     else:
#         print(f"Failed to download GSCPI data: Status code {response.status_code}")
#         exit(1)

# if __name__ == "__main__":
#     download_gscpi_data()
