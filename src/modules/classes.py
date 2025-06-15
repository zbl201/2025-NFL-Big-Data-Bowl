
from PIL import Image, ImageEnhance, ImageDraw

## My Errors
class Error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        

## Player Moments
class PlayerMoment:
    def __init__(self, name, nflId, club, gameId, playId, frameId, x, y):
        self.name = name
        self.nflId = nflId
        self.club = club
        self.gameId = gameId
        self.playId = playId
        self.frameId = frameId
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}_{self.nflId}_{self.club}_{self.gameId}_{self.playId}_{self.frameId}_{self.x}_{self.y}"
    
    
## Frames
class Frame:
    def __init__(self, gameId, playId, frameId, home_abr, visitor_abr):
        self.gameId = gameId
        self.playId = playId
        self.frameId = frameId
        self.home_abr = home_abr
        self.visitor_abr = visitor_abr
        self.player_moments = []
        
        img = Image.open('data/raw/football_field.png')
        resized_img = img.resize((2400,1066))

        enhancer = ImageEnhance.Sharpness(resized_img)
        sharpened_img = enhancer.enhance(2)
        
        self.field = sharpened_img
        
    def add_moment(self, name, nflId, club, frameId, x, y): 
        if frameId!=self.frameId: raise Error("Different frameId.")
        self.player_moments.append(PlayerMoment(name=name,nflId=nflId,club=club,gameId=self.gameId,playId=self.playId,frameId=self.frameId,x=x,y=y))
    
    def to_png(self):
        draw = ImageDraw.Draw(self.field)
        for moment in self.player_moments:
            x = 20*moment.x
            y = 20*(53.3 - moment.y)
            if moment.club==self.home_abr: color = 'blue'
            elif moment.club==self.visitor_abr: color = 'red'
            else: color = 'brown'
            draw.ellipse((x-10, y-10, x+10, y+10),fill=color)
        
        self.field.save(f'debug/frames1/{self.gameId}_{self.playId}_{self.frameId}_field.png')
        
    def __str__(self):
        return f"{self.gameId}_{self.home_abr}_{self.visitor_abr}_{self.playId}_{self.frameId}"
        
        
## Plays
class Play:
    def __init__(self, gameId, playId, home_abr, visitor_abr):
        self.gameId = gameId
        self.playId = playId
        self.home_abr = home_abr
        self.visitor_abr = visitor_abr
        self.frames = []
        
    def add_frameId(self, frameId): 
        self.frames.append(Frame(gameId=self.gameId,playId=self.playId,frameId=frameId,home_abr=self.home_abr,visitor_abr=self.visitor_abr))
        
    def reset_frames(self): 
        self.frames = []
        
    def add_frame(self, Frame): 
        self.frames.append(Frame)
        
    def __str__(self):
        return f"{self.gameId}_{self.home_abr}_{self.visitor_abr}_{self.playId}"
    