from app import App
    
def main():


    '''
    file = open("stats.json", "r")
    stats = file.read()
    
    stats_json = json.loads(stats)

    print(stats_json['data']['children'][0]['stats'][0]['metadata']['key'])
    print(stats_json['data']['children'][0]['stats'][0]['value'])


    file.close()
    '''

    windowTitle = "Apex Legends Stat Tracker"
    windowWidth = 700
    windowHeight = 400

    # Create our application
    app = App(windowTitle, windowWidth, windowHeight)

    # Add Widgets
    app.addWidgets()

    # Start our app
    app.start()

    

if __name__ == "__main__":
    main()
