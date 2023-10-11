# Network Traffic Visualization using Google Maps and Packet Capture

This project utilizes the GeoLiteCity database to translate IP addresses into geographic locations. The GeoLiteCity database can be found [here](GeoLiteCity.dat).

## Prerequisites
- Python 3.x
- `dpkt` library
- `pygeoip` library
- GeoLiteCity Database

## Usage Instructions
1. **Download GeoLiteCity Database:**
   Download the GeoLiteCity database from the provided link and place it in the project directory named `GeoLiteCity.dat`. This database is crucial for translating IP addresses into geographic coordinates.

2. **Obtain a .pcap File:**
   You need a .pcap file containing network traffic data. Using tools like Wireshark, you can use an existing .pcap file or capture your network traffic.

3. **Run the Script:**
   Execute the following command in your terminal or command prompt:
python [name of the script.py]

When prompted, enter the full path to the .pcap file.

4. **Generate KML Data:**
The script will process the .pcap file and generate KML (Keyhole Markup Language) coordinates for network traffic.
![image](https://github.com/Andresa1897/PcapFileCaptureVisualization/assets/98703359/96be134b-3cdf-4017-8eb0-37ef587cdbb3)


5. **Copy KML Coordinates:**
The script will provide you with KML coordinates in the terminal. Copy these coordinates.

6. **Visualize on Google Maps:**
- Go to [Google My Maps](https://www.google.com/maps/d/).
- Create a new map.
- Select "Import" and choose "Import KML file."
- Paste the copied KML coordinates into the provided area.
- Click "Import" to visualize the network traffic on Google Maps.



## Important Notes
- **Source IP Address:** In the code, replace 'xx.xxx.xxx.xxx' with the actual source IP address you want to visualize, along with the destination IP addresses from the .pcap file.
- **Valid .pcap File:** Ensure the .pcap file contains valid network traffic data for accurate visualization.
- **Customization (Optional):** Customize the KML header in the main function if you want to modify the appearance of the generated KML data.
- Example of Visualization ![ExampleOfVisualization](https://github.com/Andresa1897/PcapFileCaptureVisualization/assets/98703359/f0e48c20-f20a-49c9-91af-aa4aecc0effc)

