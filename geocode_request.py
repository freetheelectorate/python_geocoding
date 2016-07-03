from urllib2 import Request, urlopen, URLError


def googleRequest(addressArr):
    apikey1 = "&key=AIzaSyCNtzDEyqEfwGPFiK_ZHfMmAndsFZNzxbw"
    baseURL = "https://maps.googleapis.com/maps/api/geocode/json?address="
    address = ""

    for element in addressArr:
        address = address + ",%20" + element.strip().strip('"').lower().replace(" ","%20")

    fullURL = baseURL + address + apikey1

    try:
        print "Trying..."
        request = Request(fullURL)
        response = urlopen(request)
        location = response.read()
        print address + " was succesful..?"
        return location;
    except URLError, e:
        print 'No kittez. Got an error code:', e
        with open('failure_geocode.txt', 'r+') as out_file:
            out_file.write("Entry: Address: " + address + ", error: " + e + "\n")
