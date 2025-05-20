#PROJECT 2 Emoji Mood Responder
mood_dict={"happy":{"emoji":":)","msg":"Keep smiling and spread happiness"},
           
           "sad":{"emoji":":(","msg":"Its okay to feel down,Tomorrow will be a new day!"},
           
           "excited":{"emoji":":D","msg":"Awesome enjoy each and every moment of happiness"},
           
           "cry":{"emoji":":'(","msg":"Let the tears fall,healing begins with feeling"},

           "angry":{"emoji":">:( ","msg":"Take a breath… your peace matters more"},

           "surprised":{"emoji":":O","msg":"Wow! Life sure knows how to keep it interesting!"},

           "cool":{"emoji":"B)","msg":"Stay cool and confident,you've got this"},

           "tired":{"emoji":"-_-","msg":"Get some rest,you deserve it more than you know"},

           "love":{"emoji":"<3","msg":"You are deeply loved and truly appreciated"},

           "anxious":{"emoji":":/","msg":"Breathe easy,you're doing better than you think"},

           "shocked":{"emoji":"=O","msg":"Life just threw a twist,embrace the surprise!"},

           "wink":{"emoji":";)","msg":"A little wink goes a long way,stay playful!"},

           "nervous":{"emoji":":S","msg":"It's okay to be nervous,courage begins with fear"},

           "embarrassed":{"emoji":">.<","msg":"It’s okay, we all have those moments — smile it off"},

           "calm":{"emoji":"_","msg":"Peace surrounds you,stay grounded and centered"},

           "curious":{"emoji":":?","msg":"Questions lead to discovery,keep wondering!"}}

user_feel=input("Please say how do u feel?").lower()
if user_feel in mood_dict:
    emoji=mood_dict[user_feel]["emoji"]
    msg=mood_dict[user_feel]["msg"]
    print(f"'{user_feel}'  {emoji}  ~{msg}")
else:
    print("o_O sorry! i dont recognize this mood.. try with another!")