import os, sys
def check_ping():
    hostname = "google.com"
    response = os.system("ping " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

if __name__ == '__main__':
	pingstatus = check_ping()
	print (pingstatus)
