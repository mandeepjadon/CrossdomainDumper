import requests
from optparse import OptionParser
import sys


print """"
   _____ _____   ____   _____ _____ _____   ____  __  __          _____ _   _    _____  _    _ __  __ _____  
  / ____|  __ \ / __ \ / ____/ ____|  __ \ / __ \|  \/  |   /\   |_   _| \ | |  |  __ \| |  | |  \/  |  __ \ 
 | |    | |__) | |  | | (___| (___ | |  | | |  | | \  / |  /  \    | | |  \| |  | |  | | |  | | \  / | |__) |
 | |    |  _  /| |  | |\___ \\___ \| |  | | |  | | |\/| | / /\ \   | | | . ` |  | |  | | |  | | |\/| |  ___/ 
 | |____| | \ \| |__| |____) ____) | |__| | |__| | |  | |/ ____ \ _| |_| |\  |  | |__| | |__| | |  | | |     
  \_____|_|  \_\\____/|_____|_____/|_____/ \____/|_|  |_/_/    \_|_____|_| \_|  |_____/ \____/|_|  |_|_|     
                                                                                                             
                                                                                                             
                                                                                                                           
Author : Mandeep Jadon (@1337tr0lls)

"""

def Check_CrossDomain(hostname):
    if "http" in hostname:                                              ## checking if http is present in the domain , if not add it 
        Url=hostname
    else:
        Url="http://"+hostname
    try:
        url = requests.get(Url+"/crossdomain.xml",timeout=4)
        print "Now Testing "+Url
        if "cross-domain-policy" in url.text:                            ## Checks for the keywords as some page redirects to a home/different/error page for this Url
            print hostname+" has a crossdomain.xml"
            crossdomain=open("crossdomain.txt",'a')                      ## Makes crossdomain.txt in the current dir
            crossdomain.write("###########  Policy for "+ Url +"  ############ \n\n\n")
            for text in url.text:
                crossdomain.write(text)
            crossdomain.write("\n\n\n\n")
            crossdomain.close()
    except requests.exceptions.ConnectionError as e:
        print "error occurred for "+ hostname
        #print e                                                         ## Uncomment for Verbose errors 
    except requests.exceptions.RequestException as e:
        print "error occurred for "+ hostname
        #print e                                                          ## Uncomment for Verbose errors 
    except KeyboardInterrupt:
        print "Ctrl-c received! Exiting ..."
        sys.exit()

def main():
    parser = OptionParser()
    parser.add_option("-f","--file",dest="DomainNames", help=" -f or --file is the filename containing the urls seperated by a newline ")
    (options,args) = parser.parse_args()
    if (options.DomainNames==None) :
        print parser.usage
    else:
        DomainNames = options.DomainNames
        File = open(DomainNames)
        for url in File.readlines():
            Check_CrossDomain(url.strip("\n"))


if __name__ == "__main__":
    main()
