import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error,http.client,http.cookiejar
def checklogin(username,password):    
    url = 'https://webkiosk.juet.ac.in/CommonFiles/UserAction.jsp'
    form_fields = {
        "txtInst": "Institute",
        "InstCode": "JUET",
        "txtuType": "Member Type",
        "UserType": "S",
        "txtCode": "Enrollment No",
        "MemberCode": username,
        "txtPin": "Password/Pin",
        "Password": password,
        "BTNSubmit": "Submit"
        }
    form_data = urllib.parse.urlencode(form_fields).encode("utf-8")
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    resp = opener.open(url, form_data,timeout=600)
    body=(resp.read().decode("utf-8"))

    if "For assistance, please contact to System Administrator" in body:
        return 400
    else:
        return 200
# if checklogin("161B083","819216199")==200:
#     print("yes")
# else:
#     print("No")
