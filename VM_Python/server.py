import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def index():
    seasonOne = ["Pilot","Diversity Day","Health Care","The Alliance","BasketBall","Hot Girl"]
    seasonTwo = ["The Dundies","Sexual Harrassment","Office Olympics","The Fire","Halloween","The Fight","The Client","Performance Review","Email Surveillance","Christmas Party","Booze Cruise","The Injury","The Secret","The Carpet","Boys and Girls","Valentine's Day","Dwight's Speech","Take Your Daughter To Work Day","Michael's Birthday","Drug Testing","Conflict Resolution","Casino Night"]
    seasonThree = ["Gay Witch Hunt","The Convention","The Coup","Grief Counseling","Initiation","Diwali","Branch Closing","The Merger","The Convict","A Benihana Christmas","Back From Vaction","Traveling Salesmen","The Return","Ben Franklin","Phyllis' Wedding","Business School","Cocktails","The Negotiation","Safety Training","Product Recall","Women's Appreciation","Beach Games","The Job"]
    seasonFour = ["Fun Run","Dunder Mifflin Infinity","Launch Party","Money","Local Ad","Branch Wars","Survivor Man","The Depostition","Dinner Party","Chair Model","Night Out","Did I Stutter","Job Fair","Goodbye Toby"]
    seasonFive = ["Weight Loss","Buisness Ethics","Baby Shower","Crime Aid","Employee Transfer","Customer Survey","Business Trip","Frame Toby","The Surplus","Moroccan Christmas","The Duel","Prince Family Paper","Stress Relief","Lecture Circuit:Part 1","Lecture Circuit:Part 2","Blood Drive","Golden Ticket","New Boss","Two Weeks","Dream Team","Michael Scott Paper Company","Heavy Competition","Broke","Casual Friday","Cafe Disco","Company Picnic"]
    seasonSix = ["Gossip","The Meeting","The Promotion","Niagara","Mafia","The Lover","Koi Pond","Double Date","Murder","Shareholder Meeting","Scott's Tots","Secret Santa","The Banker","Sabre","The Manager and the Salesman","The Delivery","St.Patrick's Day","New Leads","Happy Hour","Secretary's Day","Body Language","The Cover-Up","The Chump","Whistleblower"]
    seasonSeven = ["Nepotism","Counseling","Andy's Play","Sex Ed","The Sting","Costume Contest","Christening","Viewing Party","WUPHF.com","China","Classy Christmas","Ultimatum","The Seminar","The Search","PDA","Threat Level Midnight","Tod Packer","Garage Sale","Training Day","Michael's Last Dundies","Goodbye Michael","The Inner Circle","Dwight K. Schrute (Acting) Manager","Search Committee"]
    seasonEight = ["The List","The Incentive","Lotto","Garden Party","Spooked","Doomsday","Pam's Replacement","Gettysburg","Mrs.California","Christmas Wishes","Trivia","Pool Party","Jury Duty","Special Project","Tallahassee","After Hours","Test the Store","Last Day in Florida","Get The Girl","Welcome Party","Angry Andy","Fundraiser","Turf War","Free Family Portrait Studio"]
    seasonNine = ["New Guys","Roy's Wedding","Andy's Ancestry","Work Bus","Here Comes Treble","The Boat","The Whale","The Target","Dwight Christmas","Lice","Suit Warehouse","Customer Loyalty","Junior Salesman","Vandalism","Couples Discount","Moving On","The Farm","Promos","Stairmageddon","Paper Airplane","Livin' the Dream","A.A.R.M.","Finale"]

    epName = "NonePicked"
    sz = random.randint(1,9)
    if(sz == 1):
        ep = random.randint(0,5)
        epName = seasonOne[ep]
    elif(sz == 2):
        ep = random.randint(0,21)
        epName = seasonTwo[ep]
    elif(sz == 3):  
        ep = random.randint(0,22)
        epName = seasonThree[ep]
    elif(sz == 4):          
        ep = random.randint(0,13)
        epName = seasonFour[ep]
    elif(sz == 5):
        ep = random.randint(0,25)
        epName = seasonFive[ep]
    elif(sz == 6):  
        ep = random.randint(0,23)
        epName = seasonSix[ep]
    elif(sz == 7):  
        ep = random.randint(0,23)
        epName = seasonSeven[ep]
    elif(sz == 8):  
        ep = random.randint(0,23)
        epName = seasonEight[ep]
    elif(sz == 9):  
        ep = random.randint(0,22)
        epName = seasonNine[ep]
    
    return render_template('home.html', sz=str(sz), ep=str(ep+1), epName=epName, epPic= str("/static/" + "TheOfficeMain"+ ".jpg"))
   # return str( "Season " + str(sz) + " Episode " + str(ep+1) + ": " + epName)

@app.route('/home/')
    
def home():
    return render_template('home.html',)


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=80)
