import urllib.request, urllib.error, urllib.parse,urllib.request,urllib.parse,urllib.error,http.client,http.cookiejar
import re,json

def getAttendance(username,password):
    def trimAttendance(html):
        no_of_subjects=len(re.findall('<td>\w*</td>',html))
        data=[]
        for row in range(no_of_subjects): data += [[0]*6]
        for i in range(no_of_subjects):
            part=html[html.index('<tr')+16:html.index('</tr')]
            for j in range(5):
                part2=part[part.index('<td')+4:part.index('</td>')]
                if part2=='&nbsp;':
                    part2='N/A'
                elif part2.startswith('alig'):
                    part2=part[part.index('>',50)+1:part.index('</')]
                    if part2.startswith('<fo'):
                        part2=part2[part2.index('>')+1:]
                    if j==1 or j==4:
                        if (j==1 and part2!="N/A") or (j==4 and (data[i][1]=="N/A" and part2!="N/A")):
                            data[i][5]=part[part.index("'")+1:part.index("'>")]
                        else:
                            data[i][5]='N/A'
                data[i][j]=part2
                part=part[part.index('</td')+5:]
            html=html[html.index('</tr')+5:]
        return data


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
    url = 'https://webkiosk.juet.ac.in/StudentFiles/Academic/StudentAttendanceList.jsp'
    resp = opener.open(url,timeout=60)
    result=resp.read()
    result=result.decode("utf-8")
    print(result)
    result=result[result.index('<tb')+8:result.index('</tb')]
    no_of_subjects=len(re.findall('<td>\w*</td>',result))
    data=trimAttendance(result)
    response=[]
    for i in data:
        # print(i[0])
        response.append({'subject':i[0],'attendance':{'lectut':i[1],'lecture':i[2],
            'tutorial':i[3],'practical':i[4]},'link':i[5]})
    with open('data.json', 'w') as f:
        json.dump(response, f, sort_keys=True, indent=4, separators=(',', ': '))
    
            # else:
            #     print("alr")

getAttendance('161B083','8192161998')

def checkattendance(data):
    for i in data:
        for j in range(1,5):
            if i[j].isdigit() and int(i[j])<=80:
                print(i[j],i[0])