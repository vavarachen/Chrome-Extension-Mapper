import requests
from bs4 import BeautifulSoup as bs
import csv
import sys


def _get_plugin_source(plugin_id):
    url = r'https://chrome.google.com/webstore/detail/'
    try:
        resp = requests.get(url + str(plugin_id))
    except Exception:
        raise
    else:
        if resp.ok:
            return resp.text
        else:
            raise ValueError(resp.status_code, resp.reason)


def _get_plugin_name(html_source):
    plugin_name = "Unknown"
    plugin_ver = "-1"
    try:
        soup = bs(html_source, 'html.parser')
    except Exception:
        raise
    else:
        plugin_name = soup.find_all('title')[0].text.strip()
        plugin_name.strip("<title>")
        plugin_name.split('-')[0]

        plugin_ver = [a.get("content") for a in soup.find_all('meta', {"itemprop": "version"})]
    return plugin_name.strip(), plugin_ver[0].strip()


mapped_plugins = []
with open(sys.argv[1]) as fh:
    csvreader = csv.DictReader(fh)
    for row in csvreader:
        plugin_id = row['plugin_id']
        count = row['dc(aid)']
        try:
            webstore_source = _get_plugin_source(plugin_id)
        except Exception as err:
            print(plugin_id, err)
        else:
            try:
                plugin_name, plugin_ver = _get_plugin_name(webstore_source)
            except Exception as err:
                print(plugin_id, err)
            else:
                mapped_plugins.append({'plugin_id': plugin_id, 'plugin_name': plugin_name,
                                       'plugin_version': plugin_ver, 'count': count})


print("Processed %d plugins" % len(mapped_plugins))

try:
    with open(sys.argv[2], 'w') as fh:
        header = list(mapped_plugins[0].keys())
        writer = csv.DictWriter(fh, fieldnames=header)
        writer.writeheader()
        for mapped_plugin in mapped_plugins:
            writer.writerow(mapped_plugin)
except Exception as err:
    print("%s <input.csv> <output.csv>" % sys.argv[0])
    print('''Generate input file by running:\n
    (sourcetype="ProcessRollup*" OR sourcetype="SyntheticProcessRollup") "chrome-extension://"
| rex field=CommandLine "chrome-extension\:\/\/(?<plugin_id>[^/]+)"
| stats dc(aid) by plugin_id''')
    sys.exit(err)
else:
    print("Finished writing output.")
