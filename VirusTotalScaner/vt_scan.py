import vt
import sys
from os import system, name

# Change it to your VirusTotal API key
api_key = "<your_api_key>"

def url_lookup():
    try:
        client = vt.Client(api_key)

    except:
        print("ERROR: can't connect with VT API")
        sys.exit(0)
    
    mal_url = input("Provide URL > ")
     
    url = client.get_object("/urls/{}", vt.url_id(mal_url))

    last_stats = url.last_analysis_stats
    print("URL scan--------------------------------------------------------")

    for obj in last_stats:
        print(f"{obj}: {last_stats[obj]}")

    print("----------------------------------------------------------------")
    client.close()

def file_lookup():
    
    try:
        client = vt.Client(api_key)

    except:
        print("ERROR: can't connect with VT API")
        sys.exit(0)

    hash = input("Provide file hash > ")
    file = client.get_object(f"/files/{hash}")

    print("File scan-------------------------------------------------------")
    print(f"SHA-256: {file.sha256}\nMD5: {file.md5}")
    print("----------------------------------------------------------------")

    last_stats = file.last_analysis_stats

    for obj in last_stats:
        print(f"{obj}: {last_stats[obj]}")

    del last_stats
    print("----------------------------------------------------------------")
    print(f"file size: {file.size}\ntag: {file.type_tag}")
    print("----------------------------------------------------------------")   

    client.close()

def main():
    
    if api_key == "<your_api_key>":
        print("Before using this tool you need to change API key in code")
        sys.exit(0)

    # Define system
    print("Checking system type...")
    if name == "nt":
        print("Windows")
        clear_screen = "cls"

    elif name == "posix":
        print("Linux")
        clear_screen = "clear"
    
    print("----------------------------------------------------------------")
    print("1 - File lookup\n2 - URL lookup\n3 - Exit")
    print("----------------------------------------------------------------")
    val = int(input("What to do? > "))
    
    if val == 1:
        system(clear_screen)
        file_lookup()

    if val == 2:
        system(clear_screen)
        url_lookup()
    
    elif val == 3:
        sys.exit(0)

    else:
        print("ERROR: invalid function")
        sys.exit(1)

if '__main__' == __name__:
    main()    

