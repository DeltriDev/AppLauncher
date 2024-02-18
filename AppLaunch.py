import AppOpener

def LaunchAppsFromText():
    with open('apps.txt') as f:
        lines = f.readlines()
    for i in lines:
        AppOpener.open(i, match_closest=True)