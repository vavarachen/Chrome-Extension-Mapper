import requests
from bs4 import BeautifulSoup as bs
import csv
import sys
import json


def _get_plugin_source(plugin_id):
    """
    Retrieve web response from extension_id chrome webstore
    :param plugin_id: (str) extension-id
    :return: (str) response body
    """
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

        plugin_ver = [a.get("content") for a in soup.find_all('meta', {"itemprop": "version"})][0]
    return plugin_name.strip(), plugin_ver.strip()


enriched_rows = []
mapped_plugins = dict({})
with open(sys.argv[1]) as fh:
    csvreader = csv.DictReader(fh)
    for row in csvreader:
        plugin_id = row['plugin_id']
        if plugin_id in mapped_plugins.keys():
            row['plugin_name'], row['plugin_ver'] = mapped_plugins[plugin_id]
            enriched_rows.append(row)
        else:
            print("Now mapping %s" % plugin_id)
            try:
                webstore_source = _get_plugin_source(plugin_id)
            except Exception as err:
                print(plugin_id, err)
            else:
                try:
                    row['plugin_name'], row['plugin_ver'] = _get_plugin_name(webstore_source)
                except Exception as err:
                    print(plugin_id, err)
                else:
                    enriched_rows.append(row)
                    mapped_plugins[plugin_id] = row['plugin_name'], row['plugin_ver']
    print("Identified %d unique extensions" % len(mapped_plugins))
    print(json.dumps(mapped_plugins, indent=2))


try:
    with open(sys.argv[2], 'w') as fh:
        header = list(enriched_rows[0].keys())
        writer = csv.DictWriter(fh, fieldnames=header)
        writer.writeheader()
        for mapped_row in enriched_rows:
            writer.writerow(mapped_row)
except Exception as err:
    print("%s <input.csv> <output.csv>" % sys.argv[0])
    print('''Generate input file by running:\n
    (sourcetype="ProcessRollup*" OR sourcetype="SyntheticProcessRollup") "chrome-extension://"
| rex field=CommandLine "chrome-extension\:\/\/(?<plugin_id>[^/]+)"
| stats dc(aid) by plugin_id''')
    sys.exit(err)
else:
    print("Finished processing %s. Writing output to %s" % (sys.argv[1], sys.argv[2]))
