import ssl
import datetime

# Set the target URL
url = "https://example.com"

# Get the SSL certificate for the URL
cert = ssl.get_server_certificate((url, 443))

# Parse the certificate
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

# Get the expiration date of the certificate
expiration_date = x509.get_notAfter().decode('ascii')

# Convert the expiration date to a datetime object
expiration_datetime = datetime.datetime.strptime(expiration_date, "%Y%m%d%H%M%SZ")

# Print the expiration date
print("Expiration date:", expiration_datetime.strftime("%Y-%m-%d %H:%M:%S"))
