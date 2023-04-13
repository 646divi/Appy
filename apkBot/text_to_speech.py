import pyttsx3 as p

engine = p.init()

# engine.save_to_file('You selected apps and games','apps_and_games.mp3')
# engine.runAndWait()
engine.save_to_file('You selected Paid games','Paid_and_Mod_games.mp3')
engine.runAndWait()
engine.stop()
