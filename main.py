# Import necessary libraries
import dpkt
import socket
import pygeoip

# Initialize GeoIP database
gi = pygeoip.GeoIP('GeoLiteCity.dat')

# Function to generate KML coordinates for given source and destination IP addresses
def retKML(dstip, srcip):
    # Retrieve geographical information for destination IP
    dst = gi.record_by_name(dstip)
    # Assuming 'xx.xxx.xxx.xxx' is a placeholder for the actual source IP address
    # Retrieve geographical information for source IP (replace 'xx.xxx.xxx.xxx' with the actual IP)
    src = gi.record_by_name('xx.xxx.xxx.xxx')
    try:
        # Extract longitude and latitude for source and destination IPs
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        # Format KML data with coordinates
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''

# Function to generate KML data for all IP pairs in the pcap file
def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            # Extract source and destination IP addresses from the packet
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            # Generate KML data for the IP pair and append to kmlPts
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts

# Main function to read pcap file and generate KML data
def main():
    try:
        # Ask user for pcap file path
        pcap_file_path = input("Enter the full path to the pcap file: ")
        # Open the pcap file and read data using dpkt
        with open(pcap_file_path, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            # KML header with style information
            kmlheader = '<Your KML Header>'  # Add your KML header here
            # KML footer
            kmlfooter = '</Document>\n</kml>\n'
            # Generate KML data for IP pairs in the pcap file
            kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
            print(kmldoc)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Check if the script is run directly
if __name__ == '__main__':
    # Call the main function
    main()