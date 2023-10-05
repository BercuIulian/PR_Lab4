import socket
from bs4 import BeautifulSoup

def send_request(path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5000))  # Replace with the correct port
        request = f'GET {path} HTTP/1.1\r\nHost: localhost\r\n\r\n'
        s.sendall(request.encode())
        response = s.recv(4096)  # Adjust the buffer size as needed
        return response.decode()

def parse_product_details(response):
    soup = BeautifulSoup(response, 'html.parser')
    product_details = {}
    
    # Parse product details from the HTML
    product_details['name'] = soup.find('h1').text
    product_details['author'] = soup.find('p', class_='author').text
    product_details['price'] = float(soup.find('p', class_='price').text.strip('$'))
    product_details['description'] = soup.find('p', class_='description').text
    
    return product_details

# Make requests to different pages
pages = ['/', '/about', '/contacts', '/product-listing']

product_details_dict = {}

for page in pages:
    response = send_request(page)
    if page.startswith('/product/'):
        product_id = int(page.split('/')[-1])
        product_details = parse_product_details(response)
        product_details_dict[product_id] = product_details

# Print the parsed product details
for product_id, details in product_details_dict.items():
    print(f'Product ID: {product_id}')
    print('Product Details:')
    for key, value in details.items():
        print(f'{key}: {value}')
    print()
