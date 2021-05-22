#!/usr/bin/python3
import argparse, re, webbrowser, time, urllib.parse, urllib.request
from lib import progress_bar

def main(): 
    parser = argparse.ArgumentParser(description="Process a string")
    parser.add_argument("genre_intent", metavar="default", type=str, nargs="+",
    help="input to play a specific lofi genre")


    args = parser.parse_args()

    lofi_search =  " ".join([str(x) for x in args.genre_intent]) 
    query = urllib.parse.urlencode({"search_query": lofi_search + " lofi"})
    formattedURL = urllib.request.urlopen("https://www.youtube.com/results?" + query)

    print(f"Searching Youtube for \"{lofi_search} lofi\"")

    for item in progress_bar.createBar(list(range(0, 3))):
        time.sleep(1)

    results = re.findall(r"watch\?v=(\S{11})", formattedURL.read().decode())
    video = "https://www.youtube.com/watch?v=" + "{}".format(results[0])
    print(f"OPENING BROWSER TO {video}")
    webbrowser.open_new(video)

if __name__ == "__main__":
    main()