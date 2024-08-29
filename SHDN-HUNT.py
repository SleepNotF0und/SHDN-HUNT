import shodan



#COLORS
bcolors = {
    'HEADER' : '\033[95m',
    'OKBLUE' : '\033[94m',
    'OKCYAN' : '\033[96m',
    'OKGREEN' : '\033[92m',
    'WARNING' : '\033[93m',
    'FAIL' : '\033[91m',
    'ENDC' : '\033[0m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m'
}


#BANNER
print("\n\n      ___           ___           ___           ___  ")
print("     /\  \         /\__\         /\  \         /\__\     ")
print("    /::\  \       /:/  /        /::\  \       /::|  |    ")
print("   /:/\ \  \     /:/__/        /:/\:\  \     /:|:|  |    ")
print("  _\:\~\ \  \   /::\  \ ___   /:/  \:\__\   /:/|:|  |__  ")
print(" /\ \:\ \ \__\ /:/\:\  /\__\ /:/__/ \:|__| /:/ |:| /\__\ ")
print(" \:\ \:\ \/__/ \/__\:\/:/  / \:\  \ /:/  / \/__|:|/:/  / ")
print("  \:\ \:\__\        \::/  /   \:\  /:/  /      |:/:/  /  ")
print("   \:\/:/  /        /:/  /     \:\/:/  /       |::/  /   ")
print("    \::/  /        /:/  /       \::/__/        /:/  /    ")
print("     \/__/         \/__/         ~~            \/__/     ")
print("      ___           ___           ___           ___      ")
print("     /\__\         /\__\         /\__\         /\  \     ")
print("    /:/  /        /:/  /        /::|  |        \:\  \    ")
print("   /:/__/        /:/  /        /:|:|  |         \:\  \   ")
print("  /::\  \ ___   /:/  /  ___   /:/|:|  |__       /::\  \  ")
print(" /:/\:\  /\__\ /:/__/  /\__\ /:/ |:| /\__\     /:/\:\__\ ")
print(" \/__\:\/:/  / \:\  \ /:/  / \/__|:|/:/  /    /:/  \/__/ ")
print("      \::/  /   \:\  /:/  /      |:/:/  /    /:/  /      ")
print("      /:/  /     \:\/:/  /       |::/  /     \/__/       ")
print("     /:/  /       \::/  /        /:/  /                  ")
print("     \/__/         \/__/         \/__/                   ")
print(bcolors['BOLD'] +"Coded By Hazem Yasser | hackerone.com/0xr3dhunt\n\n" + bcolors['ENDC'])



#SHODAN API KEY
My_API = input(bcolors['FAIL'] +"API KEY$--> "+ bcolors['ENDC']) 
API = shodan.Shodan(My_API)

#Query Input
Query = input(bcolors['FAIL'] +"QUERY$--> "+ bcolors['ENDC'])

#Query Result 1
try:
    Result1 = API.search_cursor(Query)   
except shodan.APIError as error:
    print(bcolors['FAIL'] +"!!! Error !!!"+ bcolors['ENDC'])


#Get the Domains Name Only
Hostnames = [ get_domain['hostnames'] for get_domain in Result1 ]

Get_Domains = []
for host in Hostnames:
    for string in host:
        Get_Domains.append('.'.join(string.split('.')[-2:]))


#PRINT DOAMINS ONLY
print(bcolors['FAIL']+"\n==========DOMAINS========="+bcolors['ENDC'])
print(bcolors['BOLD']+ str(set(Get_Domains)).replace('}','').replace('{','').replace("'","").replace(',','\n') +bcolors['ENDC'])
print(bcolors['FAIL']+"==========================\n\n"+bcolors['ENDC'])


#SAVE IPs In FILE.txt
print(bcolors['OKGREEN']+"!!! RESULT SAVED IN RESULT.txt !!!"+bcolors['ENDC'])
with open('Result.txt', 'w+') as file:file.write(str(set(Get_Domains)).replace(',','\n').replace("'","").replace("}","").replace("{",""))
    
#======================================================================================================================================
#======================================================================================================================================

'''
#Get IPs Only & Query Result 2
Result2 = API.search_cursor(Query,  retries=10)   
IPs = [ ip['ip_str'] for ip in Result2 ]
print(bcolors['BOLD']+ str(IPs).replace("[","").replace("]","").replace("'","").replace(",","\n")+bcolors['ENDC'])


#Print the Count of the Result
print(bcolors['FAIL']+"\n====================================="+bcolors['ENDC'])
print(bcolors['FAIL']+"         TOTAL IPs RESULTS: " + str(len(IPs)) +bcolors['ENDC'])
print(bcolors['FAIL']+"=====================================\n"+bcolors['ENDC'])


#SAVE IPs In FILE.txt
print(bcolors['OKGREEN']+"!!! RESULT SAVED IN RESULT.txt !!!"+bcolors['ENDC'])
with open('Result.txt', 'w+') as file:file.write(str(IPs).replace(',','\n').replace("'","").replace("]","").replace("[",""))
'''
