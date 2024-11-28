import sys

def update(state: list) -> list:
    errors = []
    print(f'Updating {len(state)} ClouDNS entries...')
    for entry in state:
        print(f'Updating ClouDNS URL {entry["updateUrl"]} for {entry["domain"]}')
        try:
            if sys.version_info[0] < 3:
                import urllib
                page = urllib.urlopen(entry["updateUrl"])
                page.close()
            else:
                import urllib.request
                page = urllib.request.urlopen(entry["updateUrl"])
                page.close()
        except Exception as e:
            print(f'Error updating URL {entry["updateUrl"]} for {entry["domain"]}: {e}')
            errors.append({"url": entry["updateUrl"], "domain": entry["domain"], "error": str(e)})
        print(f'Updated ClouDNS URL {entry["updateUrl"]} for {entry["domain"]}')
    print(f'Updated {len(state)} ClouDNS entries with {len(errors)} errors')
    return errors