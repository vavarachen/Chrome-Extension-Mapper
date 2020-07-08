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
| lookup aid_master aid
| table aid, ComputerName, plugin_id, UserName, Version, City, Country, Continent, OU
```
# Install
```commandline
$ pip install -r requirements.txt
```

# Execution
Note, the script is expecting 'plugin_id' as the column value for Chrome extension ID.
```command-line
$ python chrome_plugin_lookup.py plugins_ids_input.csv mapped_chrome_plugins_output.csv
```

# Example
```commandline
chrome_plugin_lookup.py sample/chrome_plugins.csv sample/mapped_chrome_plugins.csv
Now mapping amdbbknpahfhdafplabjenapaacedach
Now mapping aomjjhallfgjeglblehebfpbcfeobpgk
Now mapping bbjllphbppobebmjpjcijfbakobcheof
Now mapping cfhdojbkjhnklbpkdaibdccddilifddb
Now mapping chlffgpmiacpedhhbkiomidkjlcfhogd
Now mapping ckjefchnfjhjfedoccjbhjpbncimppeg
Now mapping dajhhgiioackgdldomhppobgjbinhimh
Now mapping dcngeagmmhegagicpcmpinaoklddcgon
Now mapping ddaloccgjfibfpkalenodgehlhkgoahe
ddaloccgjfibfpkalenodgehlhkgoahe (404, 'Not Found')
Now mapping ebkbgkjhepceaoccefbchcencgmggpci
Now mapping efaidnbmnnnibpcajpcglclefindmkaj
Now mapping fdjamakpfbbddfjaooikfcpapjohcfmg
Now mapping fkepacicchenbjecpbpbclokcabebhah
Now mapping fpckohnjiaonmklkjnlplokplhhijalm
Now mapping gighmmpiobklfepjocnamgkkbiglidom
Now mapping gjalhnomhafafofonpdihihjnbafkipc
Now mapping hddjhjcbioambdhjejhdlobijkdnbggp
Now mapping hehijbfgiekmjfkfjpbkbammjbdenadd
Now mapping hpoiplhbnkgnpjkkilfahkkcimachkkj
Now mapping ilikenhndcpmliapkmmhoimckaokmihm
Now mapping jccfboncbdccgbgcbhickioeailgpkgb
jccfboncbdccgbgcbhickioeailgpkgb (404, 'Not Found')
Now mapping jjkchpdmjjdmalgembblgafllbpcjlei
Now mapping jlhmfgmfgeifomenelglieieghnjghma
Now mapping kapenncbbdmooanjhhaokalmincfphkf
Now mapping kgpdpdnaoephdehalonapacdgjhamnbc
Now mapping knipolnnllmklapflnccelgolnpehhpl
Now mapping kpoecbkildamnnchnlgoboipnblgikpn
Now mapping lmjegmlicamnimmfhcmpkclmigmmcbeh
Now mapping mcbpblocgmgfnpjjppndjkmgjaogfceg
Now mapping mhjfbmdgcfjbbpaeojofohoefgiehjai
mhjfbmdgcfjbbpaeojofohoefgiehjai (404, 'Not Found')
Now mapping nckgahadagoaajjgafhacjanaoiihapd
Now mapping ncopbgfhmondhmdfjcgecnhoekbghpfc
Now mapping ndjpnladcallmjemlbaebfadecfhkepb
Now mapping nfhhihlhepgakhgnijobelmpacmhgnid
Now mapping ngpampappnmepgilojfohadhhmbhlaek
Now mapping oeopbcgkkoapgobdbedcemjljbihmemj
Now mapping ohfgljdgelakfkefopgklcohadegdpjf
Now mapping ohgndokldibnndfnjnagojmheejlengn
Now mapping olljnkilmblncgcghhaodkpdcnokhpah
Now mapping ophjlpahpchlmihnnnihgmmeilfjmjjc
Now mapping pkpoicdhlhooickgibfkpebpfpfkhgln
Now mapping ppnbnpeolgkicgegkbkbjmhlideopiji
Identified 39 unique extensions
{
  "amdbbknpahfhdafplabjenapaacedach": [
    "ChemDraw Web Clipboard - Chrome Web Store",
    "2.0.0.52"
  ],
  "aomjjhallfgjeglblehebfpbcfeobpgk": [
    "1Password extension (desktop app required) - Chrome Web Store",
    "4.7.5.90"
  ],
  "bbjllphbppobebmjpjcijfbakobcheof": [
    "IBM Security Rapport - Chrome Web Store",
    "2.2.107"
  ],
  "cfhdojbkjhnklbpkdaibdccddilifddb": [
    "Adblock Plus - free ad blocker - Chrome Web Store",
    "3.9"
  ],
  "chlffgpmiacpedhhbkiomidkjlcfhogd": [
    "Pushbullet - Chrome Web Store",
    "358"
  ],
  "ckjefchnfjhjfedoccjbhjpbncimppeg": [
    "Token signing - Chrome Web Store",
    "0.0.30"
  ],
  "dajhhgiioackgdldomhppobgjbinhimh": [
    "HttpWatch - Chrome Web Store",
    "13.0.6"
  ],
  "dcngeagmmhegagicpcmpinaoklddcgon": [
    "Web PKI - Chrome Web Store",
    "2.15.0"
  ],
  "ebkbgkjhepceaoccefbchcencgmggpci": [
    "Nuance PDF Create - Chrome Web Store",
    "1.0.0.4"
  ],
  "efaidnbmnnnibpcajpcglclefindmkaj": [
    "Adobe Acrobat - Chrome Web Store",
    "15.1.2.0"
  ],
  "fdjamakpfbbddfjaooikfcpapjohcfmg": [
    "Dashlane - Password Manager - Chrome Web Store",
    "6.2027.0"
  ],
  "fkepacicchenbjecpbpbclokcabebhah": [
    "iCloud Bookmarks - Chrome Web Store",
    "2.1.2"
  ],
  "fpckohnjiaonmklkjnlplokplhhijalm": [
    "Private Browsing by Safely - Chrome Web Store",
    "3.0.0"
  ],
  "gighmmpiobklfepjocnamgkkbiglidom": [
    "AdBlock \u2014 best ad blocker - Chrome Web Store",
    "4.15.0"
  ],
  "gjalhnomhafafofonpdihihjnbafkipc": [
    "Szafir SDK Web - Chrome Web Store",
    "0.0.10"
  ],
  "hddjhjcbioambdhjejhdlobijkdnbggp": [
    "McAfee DLP Endpoint Chrome Extension - Chrome Web Store",
    "11.0.300.0"
  ],
  "hehijbfgiekmjfkfjpbkbammjbdenadd": [
    "IE Tab - Chrome Web Store",
    "13.1.7.1"
  ],
  "hpoiplhbnkgnpjkkilfahkkcimachkkj": [
    "HPE Functional Testing Agent - Chrome Web Store",
    "14.3.3896.4"
  ],
  "ilikenhndcpmliapkmmhoimckaokmihm": [
    "WordWeb Dictionary Lookup - Chrome Web Store",
    "0.0.1.6"
  ],
  "jjkchpdmjjdmalgembblgafllbpcjlei": [
    "McAfee Endpoint Security Web Control - Chrome Web Store",
    "10.6.0.001"
  ],
  "jlhmfgmfgeifomenelglieieghnjghma": [
    "Cisco Webex Extension - Chrome Web Store",
    "1.9.0"
  ],
  "kapenncbbdmooanjhhaokalmincfphkf": [
    "OpenText Documentum Client Manager - Chrome Web Store",
    "0.0.1.4"
  ],
  "kgpdpdnaoephdehalonapacdgjhamnbc": [
    "HP Functional Testing Agent - Chrome Web Store",
    "12.54.4731.5"
  ],
  "knipolnnllmklapflnccelgolnpehhpl": [
    "Google Hangouts - Chrome Web Store",
    "2019.411.420.3"
  ],
  "kpoecbkildamnnchnlgoboipnblgikpn": [
    "IBM Aspera Connect - Chrome Web Store",
    "3.9.7.4"
  ],
  "lmjegmlicamnimmfhcmpkclmigmmcbeh": [
    "Application Launcher for Drive (by Google) - Chrome Web Store",
    "3.2"
  ],
  "mcbpblocgmgfnpjjppndjkmgjaogfceg": [
    "Take Webpage Screenshots Entirely - FireShot - Chrome Web Store",
    "0.98.98"
  ],
  "nckgahadagoaajjgafhacjanaoiihapd": [
    "Google Hangouts - Chrome Web Store",
    "2019.411.420.3"
  ],
  "ncopbgfhmondhmdfjcgecnhoekbghpfc": [
    "Browsium Client Extension - Chrome Web Store",
    "4.3.12"
  ],
  "ndjpnladcallmjemlbaebfadecfhkepb": [
    "Office - Chrome Web Store",
    "2.2.0"
  ],
  "nfhhihlhepgakhgnijobelmpacmhgnid": [
    "Browsium Catalyst Client Extension - Chrome Web Store",
    "3.1.2.4"
  ],
  "ngpampappnmepgilojfohadhhmbhlaek": [
    "IDM Integration Module - Chrome Web Store",
    "6.36.5"
  ],
  "oeopbcgkkoapgobdbedcemjljbihmemj": [
    "Checker Plus for Gmail\u2122 - Chrome Web Store",
    "22.2.4"
  ],
  "ohfgljdgelakfkefopgklcohadegdpjf": [
    "Smallpdf - Edit, Compress and Convert PDF - Chrome Web Store",
    "0.18.2"
  ],
  "ohgndokldibnndfnjnagojmheejlengn": [
    "Citavi Picker - Chrome Web Store",
    "2020.5.06.08"
  ],
  "olljnkilmblncgcghhaodkpdcnokhpah": [
    "Unfriend Finder - Chrome Web Store",
    "3.3.4"
  ],
  "ophjlpahpchlmihnnnihgmmeilfjmjjc": [
    "LINE - Chrome Web Store",
    "2.3.8"
  ],
  "pkpoicdhlhooickgibfkpebpfpfkhgln": [
    "Softomotive Automation - Chrome Web Store",
    "1.0.0.17"
  ],
  "ppnbnpeolgkicgegkbkbjmhlideopiji": [
    "Windows 10 Accounts - Chrome Web Store",
    "1.0.2"
  ]
}
Finished processing Chrome-Extension-Mapper/sample/chrome_plugins.csv. Writing output to Chrome-Extension-Mapper/sample/mapped_chrome_plugins.csv

Process finished with exit code 0
```