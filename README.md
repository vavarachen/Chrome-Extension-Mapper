# Chrome-Extension-Mapper
Simple script to map Chrome extension IDs to extension name and app store URL

# CS Falcon Query
If you are a CS Falcon NGAV shop, you can run the following CS Splunk query to identify Chrome extensions *in use*.  In other words, if the user is not using Chrome, you will not have the data.  The resulting CSV file export can be fed to the 'chrome_plugin_lookup.py' script.

```
(sourcetype="ProcessRollup*" OR sourcetype="SyntheticProcessRollup") "chrome-extension://"
    [| inputlookup aid_master 
    |  where ProductType==1 and event_platform="Win"
    |  table aid]
| rex field=CommandLine "chrome-extension\:\/\/(?<plugin_id>[^/]+)"
| stats values(plugin_id) as "ChromePlugins" by aid
| lookup aid_master aid
```
