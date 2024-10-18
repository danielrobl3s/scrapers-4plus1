from cdriver import Driver
import time
from bs4 import BeautifulSoup
from lxml import etree
import random
from csv import DictWriter


def check_links_first(links):
    
   for link in links:
       try:
           with open(link.replace("/propertyrecord-search/Hayden_ID/", "")+"_links.txt", 'r') as f:
               f.read()

               links.remove(link)
       except:
            pass
       

# List of links to scrape
links = [
      "/propertyrecord-search/Hayden_ID/Burdock-Loop",
      "/propertyrecord-search/Hayden_ID/E-Arena-Loop",
      "/propertyrecord-search/Hayden_ID/E-Avon-Cir",
      "/propertyrecord-search/Hayden_ID/E-Bruce-Rd",
      "/propertyrecord-search/Hayden_ID/E-Bruin-Loop",
      "/propertyrecord-search/Hayden_ID/E-Buckles-Rd",
      "/propertyrecord-search/Hayden_ID/E-Burchell-Dr",
      "/propertyrecord-search/Hayden_ID/E-Burnham-Ave",
      "/propertyrecord-search/Hayden_ID/E-Cambridge-Dr",
      "/propertyrecord-search/Hayden_ID/E-Cloverleaf-Dr",
      "/propertyrecord-search/Hayden_ID/E-Dakota-Ave",
      "/propertyrecord-search/Hayden_ID/E-Dempsey-Dr",
      "/propertyrecord-search/Hayden_ID/E-Dodd-Rd",
      "/propertyrecord-search/Hayden_ID/E-English-Point-Rd",
      "/propertyrecord-search/Hayden_ID/E-Evernade-Rd",
      "/propertyrecord-search/Hayden_ID/E-Ezra-Ave",
      "/propertyrecord-search/Hayden_ID/E-Garwood-Rd",
      "/propertyrecord-search/Hayden_ID/E-Grand-Tour-Dr",
      "/propertyrecord-search/Hayden_ID/E-Hayden-Ave",
      "/propertyrecord-search/Hayden_ID/E-Hayden-Haven-Rd",
      "/propertyrecord-search/Hayden_ID/E-Hayden-Lake-Rd",
      "/propertyrecord-search/Hayden_ID/E-Henry-Point-Rd",
      "/propertyrecord-search/Hayden_ID/E-Honeysuckle-Ave",
      "/propertyrecord-search/Hayden_ID/E-Hudlow-Rd",
      "/propertyrecord-search/Hayden_ID/E-Hurricane-Dr",
      "/propertyrecord-search/Hayden_ID/E-Iowa-Ave",
      "/propertyrecord-search/Hayden_ID/E-Jensen-Dr",
      "/propertyrecord-search/Hayden_ID/E-Lacey-Ave",
      "/propertyrecord-search/Hayden_ID/E-Lady-Bug-Ln",
      "/propertyrecord-search/Hayden_ID/E-Lake-Forest-Dr",
      "/propertyrecord-search/Hayden_ID/E-Lancaster-Rd",
      "/propertyrecord-search/Hayden_ID/E-Lobo-Loop",
      "/propertyrecord-search/Hayden_ID/E-Loch-Haven-Dr",
      "/propertyrecord-search/Hayden_ID/E-Loch-Maree-Dr",
      "/propertyrecord-search/Hayden_ID/E-Lupine-Ln",
      "/propertyrecord-search/Hayden_ID/E-Maple-Pl",
      "/propertyrecord-search/Hayden_ID/E-Maroon-Creek-Dr",
      "/propertyrecord-search/Hayden_ID/E-Miles-Ave",
      "/propertyrecord-search/Hayden_ID/E-Northwood-Drm",
      "/propertyrecord-search/Hayden_ID/E-Ohio-Match-Rd",
      "/propertyrecord-search/Hayden_ID/E-Orchard-Ave",
      "/propertyrecord-search/Hayden_ID/E-Point-Hayden-Dr",
      "/propertyrecord-search/Hayden_ID/E-Ripple-Rd",
      "/propertyrecord-search/Hayden_ID/E-Round-up-Cir",
      "/propertyrecord-search/Hayden_ID/E-Ryan-Dr",
      "/propertyrecord-search/Hayden_ID/E-St-James-Ave",
      "/propertyrecord-search/Hayden_ID/E-Stratford-Dr",
      "/propertyrecord-search/Hayden_ID/E-Sunset-Beach-Rd",
      "/propertyrecord-search/Hayden_ID/E-Syringa-Rd",
      "/propertyrecord-search/Hayden_ID/E-Tobler-Rd",
      "/propertyrecord-search/Hayden_ID/E-Upper-Hayden-Lake-Rd",
      "/propertyrecord-search/Hayden_ID/E-Viceroy-Ave",
      "/propertyrecord-search/Hayden_ID/E-Waverly-Loop",
      "/propertyrecord-search/Hayden_ID/E-Willow-Tree-Ln",
      "/propertyrecord-search/Hayden_ID/E-Woodstone-Dr",
      "/propertyrecord-search/Hayden_ID/N-Ainsworth-Dr",
      "/propertyrecord-search/Hayden_ID/N-Amethyst-Dr",
      "/propertyrecord-search/Hayden_ID/N-Armonia-Way",
      "/propertyrecord-search/Hayden_ID/N-Ash-St",
      "/propertyrecord-search/Hayden_ID/N-Audubon-Dr",
      "/propertyrecord-search/Hayden_ID/N-Avalanche-Ln",
      "/propertyrecord-search/Hayden_ID/N-Avondale-Loop",
      "/propertyrecord-search/Hayden_ID/N-Baack-Rd",
      "/propertyrecord-search/Hayden_ID/N-Barcelona-St",
      "/propertyrecord-search/Hayden_ID/N-Bateman-St",
      "/propertyrecord-search/Hayden_ID/N-Belgrave-Loop",
      "/propertyrecord-search/Hayden_ID/N-Berkshire-St",
      "/propertyrecord-search/Hayden_ID/N-Biztown-Loop",
      "/propertyrecord-search/Hayden_ID/N-Bligh-Ct",
      "/propertyrecord-search/Hayden_ID/N-Blossom-Dr",
      "/propertyrecord-search/Hayden_ID/N-Bob-Worst-Ln",
      "/propertyrecord-search/Hayden_ID/N-Boot-Hill-Rd",
      "/propertyrecord-search/Hayden_ID/N-Boysenberry-Loop",
      "/propertyrecord-search/Hayden_ID/N-Bradbury-Dr",
      "/propertyrecord-search/Hayden_ID/N-Brantley-Rd",
      "/propertyrecord-search/Hayden_ID/N-Brookside-Dr",
      "/propertyrecord-search/Hayden_ID/N-Camp-Ct",
      "/propertyrecord-search/Hayden_ID/N-Castle-Way",
      "/propertyrecord-search/Hayden_ID/N-Cattle-Dr",
      "/propertyrecord-search/Hayden_ID/N-Cedar-Grove-Ln",
      "/propertyrecord-search/Hayden_ID/N-Chalet-Rd",
      "/propertyrecord-search/Hayden_ID/N-Chateaux-Dr",
      "/propertyrecord-search/Hayden_ID/N-Chicken-Point-Rd",
      "/propertyrecord-search/Hayden_ID/N-Circle-Dr",
      "/propertyrecord-search/Hayden_ID/N-Clarkview-Pl",
      "/propertyrecord-search/Hayden_ID/N-Cloverleaf-Dr",
      "/propertyrecord-search/Hayden_ID/N-Corsair-St",
      "/propertyrecord-search/Hayden_ID/N-Courcelles-Pkwy",
      "/propertyrecord-search/Hayden_ID/N-Crabapple-Ct",
      "/propertyrecord-search/Hayden_ID/N-Crimson-Dr",
      "/propertyrecord-search/Hayden_ID/N-Cutlass-St",
      "/propertyrecord-search/Hayden_ID/N-Danielle-Rd",
      "/propertyrecord-search/Hayden_ID/N-Davis-Cir",
      "/propertyrecord-search/Hayden_ID/N-Derting-Rd",
      "/propertyrecord-search/Hayden_ID/N-Diamond-Dr",
      "/propertyrecord-search/Hayden_ID/N-Dogwood-Ln",
      "/propertyrecord-search/Hayden_ID/N-Drawbridge-Ct",
      "/propertyrecord-search/Hayden_ID/N-Eastshore-Dr",
      "/propertyrecord-search/Hayden_ID/N-Easy-St",
      "/propertyrecord-search/Hayden_ID/N-Emerald-Dr",
      "/propertyrecord-search/Hayden_ID/N-Ferndale-Dr",
      "/propertyrecord-search/Hayden_ID/N-Finucane-Dr",
      "/propertyrecord-search/Hayden_ID/N-Forest-Rd",
      "/propertyrecord-search/Hayden_ID/N-Friar-Dr",
      "/propertyrecord-search/Hayden_ID/N-Gibson-Rd",
      "/propertyrecord-search/Hayden_ID/N-Government-Way",
      "/propertyrecord-search/Hayden_ID/N-Heston-Loop",
      "/propertyrecord-search/Hayden_ID/N-Hillview-Dr",
      "/propertyrecord-search/Hayden_ID/N-Jannel-St",
      "/propertyrecord-search/Hayden_ID/N-Jennifer-Ln",
      "/propertyrecord-search/Hayden_ID/N-Justice-Way",
      "/propertyrecord-search/Hayden_ID/N-Kelly-Rae-Dr",
      "/propertyrecord-search/Hayden_ID/N-Kensington-Ave",
      "/propertyrecord-search/Hayden_ID/N-LA-Costa-Ct",
      "/propertyrecord-search/Hayden_ID/N-Lakeview-Dr",
      "/propertyrecord-search/Hayden_ID/N-Liverpool-Loop",
      "/propertyrecord-search/Hayden_ID/N-Loveland-Way",
      "/propertyrecord-search/Hayden_ID/N-MacIe-Loop",
      "/propertyrecord-search/Hayden_ID/N-Macie-Loop",
      "/propertyrecord-search/Hayden_ID/N-Magic-Ct",
      "/propertyrecord-search/Hayden_ID/N-Maple-St",
      "/propertyrecord-search/Hayden_ID/N-McCall-Falls-Dr",
      "/propertyrecord-search/Hayden_ID/N-Meadow-Way",
      "/propertyrecord-search/Hayden_ID/N-Melrose-St",
      "/propertyrecord-search/Hayden_ID/N-Murcia-Ln",
      "/propertyrecord-search/Hayden_ID/N-Partridge-Way",
      "/propertyrecord-search/Hayden_ID/N-Pebble-Creek-Dr",
      "/propertyrecord-search/Hayden_ID/N-Pinetree-Rd",
      "/propertyrecord-search/Hayden_ID/N-Pinewood-Way",
      "/propertyrecord-search/Hayden_ID/N-Point-Hayden-Dr",
      "/propertyrecord-search/Hayden_ID/N-Prescott-Dr",
      "/propertyrecord-search/Hayden_ID/N-Prince-William-Loop",
      "/propertyrecord-search/Hayden_ID/N-Ptarmigan-Dr",
      "/propertyrecord-search/Hayden_ID/N-Ramsey-Rd",
      "/propertyrecord-search/Hayden_ID/N-Ramsgate-Ln",
      "/propertyrecord-search/Hayden_ID/N-Raspberry-Ln",
      "/propertyrecord-search/Hayden_ID/N-Reed-Rd",
      "/propertyrecord-search/Hayden_ID/N-Ridgeway-Ln",
      "/propertyrecord-search/Hayden_ID/N-Ridgewood-Dr",
      "/propertyrecord-search/Hayden_ID/N-Rimrock-Rd",
      "/propertyrecord-search/Hayden_ID/N-Rocking-R-Rd",
      "/propertyrecord-search/Hayden_ID/N-Ruby-Dr",
      "/propertyrecord-search/Hayden_ID/N-Rude-St",
      "/propertyrecord-search/Hayden_ID/N-Sally-St",
      "/propertyrecord-search/Hayden_ID/N-Salmonberry-Loop",
      "/propertyrecord-search/Hayden_ID/N-Seaside-St",
      "/propertyrecord-search/Hayden_ID/N-Secretariat-Ln",
      "/propertyrecord-search/Hayden_ID/N-Shamrock-St",
      "/propertyrecord-search/Hayden_ID/N-Shenandoah-Dr",
      "/propertyrecord-search/Hayden_ID/N-Sherwood-Ct",
      "/propertyrecord-search/Hayden_ID/N-Snowflake-Ln",
      "/propertyrecord-search/Hayden_ID/N-Stinson-Loop",
      "/propertyrecord-search/Hayden_ID/N-Stonehaven-Dr",
      "/propertyrecord-search/Hayden_ID/N-Strahorn-Rd",
      "/propertyrecord-search/Hayden_ID/N-Summerfield-Loop"
]

base_url = "https://www.realtor.com"

check_links_first(links)

# Loop through each link
for link in links:
    try:
        # Initialize the WebDriver for each link
        driver = Driver.get(base_url + link)
        time.sleep(random.randint(10, 35))  # Random delay to avoid being blocked

        # Get the page source BEFORE closing the driver
        html = driver.page_source

        # Use BeautifulSoup and lxml to parse the HTML
        soup = BeautifulSoup(html, "lxml")
        dom = etree.HTML(str(soup))

        # Extract all relevant <a> tags using XPath
        a_tags = dom.xpath("//a[starts-with(@href, 'https://www.realtor.com/realestateandhomes-detail/')]/@href")

        # Save the extracted links to a file
        filename = f"{link.replace('/propertyrecord-search/Hayden_ID/', '')}_links.txt"
        with open(filename, "a") as f:
            for tag in a_tags:
                f.write(f"'{tag}', \n")

    except Exception as e:
        print(f"An error occurred with {link}: {e}")

    finally:
        # Ensure the driver is always closed properly
        driver.close()
        time.sleep(10)  # Short delay between requests
