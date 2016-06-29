from urllib2 import Request, urlopen, URLError

def removeWhiteSpacesAndQuotes(element):
    if element[0] == " ":
        element = element[1:]

    # yes, I have to do this twice.
    if element[0] == " ":
        element = element[1:]

    if element[len(element) - 1] == " ":
        element = element[:-1]
    if element[len(element) - 1] == '"':
        element = element[:-1]
    return element

def googleRequest(addressArr):
    apikey1 = "&key=AIzaSyCNtzDEyqEfwGPFiK_ZHfMmAndsFZNzxbw"
    baseURL = "https://maps.googleapis.com/maps/api/geocode/json?address="
    address = addressArr[0][1:-1].replace(" ","%20")
    index = 1

    while index < len(addressArr):
        element = removeWhiteSpacesAndQuotes(addressArr[index])
        address = address + "+" + element
        index += 1

    fullURL = baseURL + address + apikey1

    try:
        print "Trying..."
        request = Request(fullURL)
        response = urlopen(request)
        location = response.read()
        return location;
    except URLError, e:
        print 'No kittez. Got an error code:', e
