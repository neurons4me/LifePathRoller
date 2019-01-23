import random

## 1 user selects starting path
## 2 load lists for paths
## 3 use random to select and pop off element description and add to output list
## 3b add stat changes to output list
## 4 check element for table change
## 5 if table change is needed change active table
## 6 repeat until 12 items in output list

base_stat_value = 10

#todo setup the selection input with proper error handling or move the front end of this to a Django site or use a CLI frontend tool?

# active_table = input("1. Academic Path \n 2. Life Experience Path \n 3. Military Path \n Choose your life path:")
active_table = "AC"

#todo make this table populated from import from csv files
master_tables = {
    "AC": [
["Caught with banned books. Expelled. Move to Life Experience Table.",[0,0,0,0,0,0],"LE"],
["Developed a drug habit. WIS -1",[0,0,0,0,-1,0],"NONE"],
["Joined scientific expedition for month.STR +1",[1,0,0,0,0,0],"NONE"],
["Discovered two new species of plants. Useful in Alchemy. INT +2",[0,0,0,2,0,0],"NONE"],
["Poisoned by large spider in Library. Recover. CON +1",[0,0,1,0,0,0],"NONE"],
["Helped elderly cleric minister to the poor. WIS +1",[0,0,0,0,1,0],"NONE"],
["Took job as delivery boy for campus mail system. DEX +1",[0,1,0,0,0,0],"NONE"],
["Helped create constructs for head wizard. INT +1",[0,0,0,1,0,0],"NONE"],
["Spent month studying nature. WIS +1",[0,0,0,0,1,0],"NONE"],
["Forecasted a major flood and saved numerous lives. WIS +1",[0,0,0,0,1,0],"NONE"],
["Discovered rare tome of obscure subject. INT +1",[0,0,0,1,0,0],"NONE"],
["Contract major illness. Unable to study or attend classes. INT -1",[0,0,0,-1,0,0],"NONE"],
["Took a month to rally for workers rights under a brutal leader. CHA +1",[0,0,0,0,0,1],"NONE"],
["Robbed at knife point. Talked thugs out of it. CHA +1",[0,0,0,0,0,1],"NONE"],
["Forced to avoid crazy Ex while attending classes DEX +1",[0,1,0,0,0,0],"NONE"],
["Tamed a small bear with treats and soft words. WIS +2",[0,0,0,0,2,0],"NONE"],
["Roomed with a student from another realm. CHA +1",[0,0,0,0,0,1],"NONE"],
["Out ran a supposedly tamed bear when it attacked a crowd. DEX +1",[0,1,0,0,0,0],"NONE"],
["Shanghaied. Forced to serve on pirate ship. Move to Military Table.",[0,0,0,0,0,0],"ML"],
["You find a ship wreck, in the desert. Copied strange symbols. INT +1",[0,0,0,1,0,0],"NONE"],
["Earned money transcribing spell books for a month. INT +1",[0,0,0,1,0,0],"NONE"],
["Joined the choir to impress the opposite sex. CHA +1",[0,0,0,0,0,1],"NONE"],
["Death of a close friend brings meaning to your life. WIS +2",[0,0,0,0,2,0],"NONE"],
["Researched venomous snakes. Wrote a paper. WIS +1",[0,0,0,0,1,0],"NONE"],
["Spent month studying Architecture of nearby castle. INT +1",[0,0,0,1,0,0],"NONE"],
["You take a month off to find yourself. CHA +1, WIS -1",[0,0,0,0,-1,1],"NONE"],
["Omens become more clear and meaningful to you. WIS +1",[0,0,0,0,1,0],"NONE"],
["Repaired fishing nets for room and board. DEX +1",[0,1,0,0,0,0],"NONE"],
["Hiked across realm collecting insect samples. CON +1",[0,0,1,0,0,0],"NONE"],
["Elected Academic body president. CHA +1",[0,0,0,0,0,1],"NONE"],
["Worked in a mine as a mineral identifier. STR +1",[1,0,0,0,0,0],"NONE"],
["Shortest route to class was across roof tops. DEX +1",[0,1,0,0,0,0],"NONE"],
["Ran for local political office. CHA +1",[0,0,0,0,0,1],"NONE"],
["Successfully brew homemade healing potion. WIS +1",[0,0,0,0,1,0],"NONE"],
["Grew up hunting with a bow. DEX +1",[0,1,0,0,0,0],"NONE"],
["Received a \"first\" in cantrips. INT +1",[0,0,0,1,0,0],"NONE"],
["Father instilled love of books. Didn't play outside much. INT +2, CON -1",[0,0,-1,2,0,0],"NONE"],
["Introduced to mysticism. WIS +1",[0,0,0,0,1,0],"NONE"],
["Cared for elderly relative. WIS +1",[0,0,0,0,1,0],"NONE"],
["Created overly elaborate mechanism to turn book pages. INT +2",[0,0,0,2,0,0],"NONE"],
["Raised by low level noble parents. Best of all things. Educated. INT +1",[0,0,0,1,0,0],"NONE"],
["Was assigned a dorm on the 8th floor. STR +1",[1,0,0,0,0,0],"NONE"],
["First Aid course turns real when goblins attack. WIS +1",[0,0,0,0,1,0],"NONE"],
["Went without sleep for three days while exams were given. CON +1",[0,0,1,0,0,0],"NONE"],
["Have a knack for Chess. Play constantly. INT +1",[0,0,0,1,0,0],"NONE"],
["Started \"filling out\". Better late than never. CHA +1",[0,0,0,0,0,1],"NONE"],
["Study animal tracks in the field. WIS +1",[0,0,0,0,1,0],"NONE"],
["Lonely nights. You learned to roll coins on your fingers. DEX +1",[0,1,0,0,0,0],"NONE"],
["Housekeeper is a horrible cook. Manage to survive. CON +1",[0,0,1,0,0,0],"NONE"],
["Research trip to ancient ruins. Pack animals died. STR +1",[1,0,0,0,0,0],"NONE"],
["Like to gamble. Lose regularly. Have to fight off bookies. STR +1",[1,0,0,0,0,0],"NONE"],
["One month at a local monastery. CON +1",[0,0,1,0,0,0],"NONE"],
["Hang head wizard's hat on flagpole. DEX +1",[0,1,0,0,0,0],"NONE"],
["Sat in on inquest jury. WIS +1",[0,0,0,0,1,0],"NONE"],
["Overcome your shyness and become more outgoing. CHA +1",[0,0,0,0,0,1],"NONE"],
["Professor killed by bugbear. Visiting elven scholar fills in. INT +1",[0,0,0,1,0,0],"NONE"],
["Scale the highest peak in the area in your free time. CON +1",[0,0,1,0,0,0],"NONE"],
["Tamed Elementals for basics course. Rock drop on foot. WIS +2, DEX -1",[0,-1,0,0,2,0],"NONE"],
["Wizard creates spell to build muscle. He gets rich. You get stronger. STR +1",[1,0,0,0,0,0],"NONE"],
["Conjured a devil, just to see if it actually worked. INT +1",[0,0,0,1,0,0],"NONE"],
["Discovered extinct primitive cult. Wrote book on their lore. INT +2",[0,0,0,2,0,0],"NONE"],
["Delivered a baby during a terrible storm. WIS +1",[0,0,0,0,1,0],"NONE"],
["Close relative was a healer. Taught you many things. WIS +1",[0,0,0,0,1,0],"NONE"],
["Translated ancient scroll into common INT +1",[0,0,0,1,0,0],"NONE"],
["Solved riddle that barred entry to an ancient tomb. INT +1",[0,0,0,1,0,0],"NONE"],
["Passed off transmuted copper as silver. Made 300GP CHA +1",[0,0,0,0,0,1],"NONE"],
["Helped clear out an undead problem at local cemetery. WIS +1",[0,0,0,0,1,0],"NONE"],
["Snuck into class late every day for a month. DEX +1",[0,1,0,0,0,0],"NONE"],
["Alchemy experiment goes awry. You get faster. DEX +1, INT -1",[0,1,0,-1,0,0],"NONE"],
["Survived childhood sickness. CON +1",[0,0,1,0,0,0],"NONE"],
["Crashed the Dean's Dinner uninvited. Blended in. CHA +1",[0,0,0,0,0,1],"NONE"],
["Saved fellow student from a collapsing bookshelf. STR +1",[1,0,0,0,0,0],"NONE"],
["Whittled small wooden animals for local children. DEX +1",[0,1,0,0,0,0],"NONE"],
["Pranked the University with an illusionary Dragon. INT +1",[0,0,0,1,0,0],"NONE"],
["Learned to dance. CHA +1",[0,0,0,0,0,1],"NONE"],
["Lived with primitive people learned from their medicine man. WIS +1",[0,0,0,0,1,0],"NONE"],
["Field trip to other planes of existence. INT +1",[0,0,0,1,0,0],"NONE"],
["Enchanted a kobold that followed you around for a week. INT +1",[0,0,0,1,0,0],"NONE"],
["Campus hit by worst ice storm in history. DEX +1",[0,1,0,0,0,0],"NONE"],
["Blessed words from your deity fall on your ears. WIS+2",[0,0,0,0,0,0],"NONE"],
["Preformed autopsies on several condemned prisoners. WIS +2",[0,0,0,0,2,0],"NONE"],
["Disillusioned with academic system. Move to Life Experience Table.",[0,0,0,0,0,0],"LE"],
["Learned to play the flute. CHA +1",[0,0,0,0,0,1],"NONE"],
["Talked your way into a class you were not qualified for. CHA +1",[0,0,0,0,0,1],"NONE"],
["Spell backfires. Fries your frontal lobe. INT -1",[0,0,0,-1,0,0],"NONE"],
["Fireball training! DEX +1",[0,1,0,0,0,0],"NONE"],
["Rebound books for extra money. DEX +1",[0,1,0,0,0,0],"NONE"],
["Worked special effects for local theater. CHA +1",[0,0,0,0,0,1],"NONE"],
["Sampling tree bark run into Treant. Exchange knowledge. WIS +1",[0,0,0,0,1,0],"NONE"],
["Four weeks with a Master Diviner. INT +1",[0,0,0,1,0,0],"NONE"],
["Study Astronomy and the movements of the moon. INT +1",[0,0,0,1,0,0],"NONE"],
["One month crafting Holy Symbols WIS +1",[0,0,0,0,1,0],"NONE"],
["Identified illness spreading through village. WIS +1",[0,0,0,0,1,0],"NONE"],
["Locked yourself out of your own room. Picked the lock. DEX +1",[0,1,0,0,0,0],"NONE"],
["Edited Professor's newly written book. INT +2",[0,0,0,2,0,0],"NONE"],
["Climbed a cliff face to retrieve rare feather for spell. STR +1",[1,0,0,0,0,0],"NONE"],
["One month tutelage under bad teacher. WIS -1",[0,0,0,0,-1,0],"NONE"],
["Completed a four week fast. CON +1",[0,0,1,0,0,0],"NONE"],
["Mapped nearby river. INT +1",[0,0,0,1,0,0],"NONE"],
["War breaks out. Drafted in military service. Move to Military Table.",[0,0,0,0,0,0],"ML"]
],
    "LE": [
["Arrested. Sentence, infantry service. Move to Military Table",[0,0,0,0,0,0],"ML"],
["Failed to pay debts. Leg broken. DEX -1",[0,-1,0,0,0,0],"NONE"],
["Dusty hovel you moved into had three books left behind. INT +1",[0,0,0,1,0,0],"NONE"],
["Born leader. CHA +1",[0,0,0,0,0,1],"NONE"],
["Tracked an animal for two weeks across snow and ice. CON +1",[0,0,1,0,0,0],"NONE"],
["Your people are renowned for their archery skills. DEX +1",[0,1,0,0,0,0],"NONE"],
["Dock worker. Loading and unloading. STR +1",[1,0,0,0,0,0],"NONE"],
["You are a liar. You lie all the time. You could be lying right now. CHA +1",[0,0,0,0,0,1],"NONE"],
["Learned to juggle. DEX +1",[0,1,0,0,0,0],"NONE"],
["Captured live birds and sold them to travelers. DEX +1",[0,1,0,0,0,0],"NONE"],
["Born with great looks. CHA +1",[0,0,0,0,0,1],"NONE"],
["Body odor is unbearable. CHA -1",[0,0,0,0,0,-1],"NONE"],
["Stable work. Worked with many horses. WIS +1",[0,0,0,0,1,0],"NONE"],
["On a dare, you did find a needle in a haystack. WIS +1",[0,0,0,0,1,0],"NONE"],
["Arrested. One month hard labor. STR +1",[1,0,0,0,0,0],"NONE"],
["Crossed a 300 foot rope bridge in a wind storm. DEX +2",[0,2,0,0,0,0],"NONE"],
["Studied the philosophy of nothingness. WIS +1",[0,0,0,0,1,0],"NONE"],
["You made a chunk of money arm wrestling in pubs. STR +1",[1,0,0,0,0,0],"NONE"],
["Scholarship awarded. Enroll at local Academy. Move to Academic Table",[0,0,0,0,0,0],"AC"],
["Youngest person elected to the Towne Council. CHA +1",[0,0,0,0,0,1],"NONE"],
["Sold snake oil until the Towne Council shut you down. CHA +1",[0,0,0,0,0,1],"NONE"],
["Studied under an enlightened monk. WIS +1",[0,0,0,0,1,0],"NONE"],
["Made ends meet by doing street magic. Sleight of hand. DEX +2",[0,2,0,0,0,0],"NONE"],
["Worked as a guard. Tied up prisoners. DEX +1",[0,1,0,0,0,0],"NONE"],
["Owned a pub for a month. CHA +1",[0,0,0,0,0,1],"NONE"],
["Manual Labor job. STR +1, DEX -1",[1,-1,0,0,0,0],"NONE"],
["Worked the shell game in a large city. DEX +1",[0,1,0,0,0,0],"NONE"],
["Chopped wood for days at a time after your last breakup. STR +1",[1,0,0,0,0,0],"NONE"],
["Survived a fever that killed many. CON +1",[0,0,1,0,0,0],"NONE"],
["Survived in the wild for a month after a natural disaster. WIS +1",[0,0,0,0,1,0],"NONE"],
["Sailed a ship using the stars for guidance. INT +1",[0,0,0,1,0,0],"NONE"],
["Part time blacksmith. STR +1",[1,0,0,0,0,0],"NONE"],
["Family home attacked by bandits. Rendered first aid to those injured. WIS +1",[0,0,0,0,1,0],"NONE"],
["Escaped a prison after you were wrongly arrested. DEX +1",[0,1,0,0,0,0],"NONE"],
["Built a log cabin by hand. STR +1",[1,0,0,0,0,0],"NONE"],
["You are a talented Tenor. CHA +1",[0,0,0,0,0,1],"NONE"],
["Natural with a musical instrument. Not fond of reading. CHA +2, INT -1",[0,0,0,-1,0,2],"NONE"],
["Spent some time as a snaked handler. DEX +1",[0,1,0,0,0,0],"NONE"],
["Traveled with a carnival. Worked with the knife thrower. DEX +1",[0,1,0,0,0,0],"NONE"],
["Gamble frequently. Great bluffer. CHA +2",[0,0,0,0,0,2],"NONE"],
["Played in a band. CHA +1",[0,0,0,0,0,1],"NONE"],
["You have an affinity for the law, but have never gone to school. INT +1",[0,0,0,1,0,0],"NONE"],
["Escaped capture when guards were out to arrest you. DEX +1",[0,1,0,0,0,0],"NONE"],
["When you were born, you were left to die. You survived. CON +1",[0,0,1,0,0,0],"NONE"],
["Come from a noble background. CHA +1",[0,0,0,0,0,1],"NONE"],
["Lived with a native tribe for a while. Learned to forage berries. WIS +1",[0,0,0,0,1,0],"NONE"],
["Avid bird hunter. Crossbow is weapon of choice. DEX +1",[0,1,0,0,0,0],"NONE"],
["Competed in a strong man event. Came in third. STR +1",[1,0,0,0,0,0],"NONE"],
["Survived merchant ship sinking. CON +1",[0,0,1,0,0,0],"NONE"],
["You are one of those annoying people full of trivia. INT +1",[0,0,0,1,0,0],"NONE"],
["Worked as an appraiser for several clients. INT +1",[0,0,0,1,0,0],"NONE"],
["Tortured to reveal a partner's location. CON +1",[0,0,1,0,0,0],"NONE"],
["Part-time grave digging work. STR +1",[1,0,0,0,0,0],"NONE"],
["Circus work. Tight-rope walker. DEX +1",[0,1,0,0,0,0],"NONE"],
["Discovered a cave network behind a waterfall. WIS +1",[0,0,0,0,1,0],"NONE"],
["Worked undercover as a spy for rival nobles. CHA +1",[0,0,0,0,0,1],"NONE"],
["Farm job pays the bills. CON+1",[0,0,0,0,0,0],"NONE"],
["Make a meager living picking pockets. DEX +2, CON -1",[0,2,-1,0,0,0],"NONE"],
["Got drunk and passed out on a stack of books. INT +1",[0,0,0,1,0,0],"NONE"],
["You are a rabble rouser. You alone have started five riots. CHA +1",[0,0,0,0,0,1],"NONE"],
["Have a natural talent for negotiating. CHA +2",[0,0,0,0,0,2],"NONE"],
["Apprenticed as a sculptor. DEX +1",[0,1,0,0,0,0],"NONE"],
["Grew up as an orphan on the streets. DEX +1",[0,1,0,0,0,0],"NONE"],
["You are wonderful with children. They love you. CHA +1",[0,0,0,0,0,1],"NONE"],
["You were groomed to be the village story teller. CHA +1",[0,0,0,0,0,1],"NONE"],
["Your people were persecuted. The clergy hid and cared for you. WIS +1",[0,0,0,0,1,0],"NONE"],
["You are greedy. If you see something you want, you just lift it. DEX +1",[0,1,0,0,0,0],"NONE"],
["Carried a broken wagon four miles to the nearest town. STR +1",[1,0,0,0,0,0],"NONE"],
["Cut across the face in a bar fight. CHA -1, CON +1",[0,0,1,0,0,-1],"NONE"],
["You survived a demonic possession as a child. CON +1",[0,0,1,0,0,0],"NONE"],
["You track and hunted creatures opposed to your morality. WIS +1",[0,0,0,0,1,0],"NONE"],
["You collect rare books. INT +1",[0,0,0,1,0,0],"NONE"],
["Your village was attack when you were a child. You harbor urges for revenge. STR +1",[1,0,0,0,0,0],"NONE"],
["Self-taught on the flute. CHA +1",[0,0,0,0,0,1],"NONE"],
["After a string of defeats, you learned humility. WIS +1",[0,0,0,0,1,0],"NONE"],
["You have great hand-eye coordination. Enjoy sport. DEX +1",[0,1,0,0,0,0],"NONE"],
["You are a seducer. You manipulate the opposite sex with your charm. CHA +1",[0,0,0,0,0,1],"NONE"],
["You know every pub song ever sung. CHA +1",[0,0,0,0,0,1],"NONE"],
["Trained as the village bell ringer. STR +1",[1,0,0,0,0,0],"NONE"],
["Worked the ropes on a ship for a month. DEX +2",[0,2,0,0,0,0],"NONE"],
["Allowed to train with monks. DEX +2",[0,2,0,0,0,0],"NONE"],
["Local Militia offer signing bonus. Move to Military Table.",[0,0,0,0,0,0],"ML"],
["You murdered someone over something minor. Feel guilty. WIS +1",[0,0,0,0,1,0],"NONE"],
["Attended to the injured after earthquake. WIS +1",[0,0,0,0,1,0],"NONE"],
["Voice cracks every time you try to speak. CHA -1",[0,0,0,0,0,-1],"NONE"],
["Manned the gong for the royal court. STR +1",[1,0,0,0,0,0],"NONE"],
["You swam a great lake near your hometown. STR +1",[1,0,0,0,0,0],"NONE"],
["Forgave an enemy on his death bed. WIS +1",[0,0,0,0,1,0],"NONE"],
["Your people have a tradition of walking on hot coals. DEX +1",[0,1,0,0,0,0],"NONE"],
["Leader of a highway bandit crew. CHA +1",[0,0,0,0,0,1],"NONE"],
["Supervised a trade caravan on a long dangerous trek. CHA +1",[0,0,0,0,0,1],"NONE"],
["Worked as the town animal catcher. DEX +1",[0,1,0,0,0,0],"NONE"],
["Assisted a clock maker for many weeks. DEX +1",[0,1,0,0,0,0],"NONE"],
["Construction work at a nearby Keep. STR +1",[1,0,0,0,0,0],"NONE"],
["Eloquent speaker with a huge vocabulary. CHA +1",[0,0,0,0,0,1],"NONE"],
["Traded in scrolls for a brief time. INT +1",[0,0,0,1,0,0],"NONE"],
["Suffered hand injury while loading crates. DEX -1",[0,-1,0,0,0,0],"NONE"],
["You can hold your breath for five minutes. CON +1",[0,0,1,0,0,0],"NONE"],
["Worked as a bouncer at a local pub. CHA +1",[0,0,0,0,0,1],"NONE"],
["A Higher Power calls. Move to Academic Table.",[0,0,0,0,0,0],"AC"],    ],
   "ML": [
["Insubordination. Relieved from duty. Move to Life Experience Table.",[0,0,0,0,0,0],"LE"],
["Punctured a lung in a battle. CON -1",[0,0,-1,0,0,0],"NONE"],
["Studied historical battles. INT +1",[0,0,0,1,0,0],"NONE"],
["Captured and used as slave labor. STR +1",[1,0,0,0,0,0],"NONE"],
["Mediated military disputes between soldiers. WIS +1",[0,0,0,0,1,0],"NONE"],
["Completed a 300 mile crusade in the name of King and God. CON +1",[0,0,1,0,0,0],"NONE"],
["Joined the Archer corps. DEX +1",[0,1,0,0,0,0],"NONE"],
["Forage patrol. Looted a ten mile swath along the main line. STR +1",[1,0,0,0,0,0],"NONE"],
["Marched barefoot for twenty miles. CON +1",[0,0,1,0,0,0],"NONE"],
["Rode out a famine while pinned down at a fort. CON +1",[0,0,1,0,0,0],"NONE"],
["In charge of placing the horses in armor. STR +1",[1,0,0,0,0,0],"NONE"],
["Tore shoulder muscle in a duel. STR -1",[-1,0,0,0,0,0],"NONE"],
["Lead your men on an assault. CHA +1",[0,0,0,0,0,1],"NONE"],
["Conscripted peasants for large offensive. CHA +1",[0,0,0,0,0,1],"NONE"],
["Dodged every arrow during an ambush. DEX +1",[0,1,0,0,0,0],"NONE"],
["Stranded on deserted island after shipwreck. CON +2",[0,0,2,0,0,0],"NONE"],
["Rallied your troops when the odds were against you. CHA +1",[0,0,0,0,0,1],"NONE"],
["Repaired saddles for the mounted division. DEX +1",[0,1,0,0,0,0],"NONE"],
["Master Tactician. Promoted to Officer School. Move to Academic Table.",[0,0,0,0,0,0],"AC"],
["Cut timber and helped build a barracks. STR +1",[1,0,0,0,0,0],"NONE"],
["Built a bridge during a campaign against enemy forces. STR +1",[1,0,0,0,0,0],"NONE"],
["Negotiated a surrender from an enemy. CHA +1",[0,0,0,0,0,1],"NONE"],
["Channeled your inner rage. CON +2",[0,0,2,0,0,0],"NONE"],
["Received forty lashes for punching an officer. CON +1",[0,0,1,0,0,0],"NONE"],
["Weapon training with heavy arms. STR +1",[1,0,0,0,0,0],"NONE"],
["Talked your way out of Physical Training. CHA +1, STR -1",[-1,0,0,0,0,1],"NONE"],
["Served on a ship. Learned to drink like a sailor. CON +1",[0,0,1,0,0,0],"NONE"],
["Learned dozens of knots while working on ship. DEX +1",[0,1,0,0,0,0],"NONE"],
["Assistant to the General. Worked with battle maps. WIS +1",[0,0,0,0,1,0],"NONE"],
["Swore vengeance against a foe that wiped out your company. CHA +1",[0,0,0,0,0,1],"NONE"],
["Integrated magic into an assault. INT +1",[0,0,0,1,0,0],"NONE"],
["Functioned as a sniper. DEX +1",[0,1,0,0,0,0],"NONE"],
["Lead a mounted division. CHA +1",[0,0,0,0,0,1],"NONE"],
["Stood guard duty in the worst weather possible. CON +1",[0,0,1,0,0,0],"NONE"],
["Crossbow practice. Placed first. DEX +1",[0,1,0,0,0,0],"NONE"],
["Lifted a horse off a comrade that was cut down. STR +1",[1,0,0,0,0,0],"NONE"],
["Wrestled bears to show off and prove strength. STR +1, INT -1",[1,0,0,-1,0,0],"NONE"],
["You often boxed fellow soldiers for cash and rations. CON +1",[0,0,1,0,0,0],"NONE"],
["Bitter winter during a tour of duty. CON +1",[0,0,1,0,0,0],"NONE"],
["Was assigned oar duty on a warship. STR +2",[2,0,0,0,0,0],"NONE"],
["Naturally athletic. STR +1",[1,0,0,0,0,0],"NONE"],
["Calculated trajectories for siege weapons. INT +1",[0,0,0,1,0,0],"NONE"],
["Jungle mission. Withstood thousands of insect bites. CON +1",[0,0,1,0,0,0],"NONE"],
["Served as a scout. WIS +1",[0,0,0,0,1,0],"NONE"],
["Deck Duty on a Navy Ship. Riggings and sails. STR +1",[1,0,0,0,0,0],"NONE"],
["Inspired a dying soldier. CHA +1",[0,0,0,0,0,1],"NONE"],
["Food poisoning spreads through camp. Your mom cooks worse. CON +1",[0,0,1,0,0,0],"NONE"],
["Assassinated a commander of enemy troops with one shot. DEX +1",[0,1,0,0,0,0],"NONE"],
["Successfully tracked enemy troops through mountains. WIS +1",[0,0,0,0,1,0],"NONE"],
["Created a logistical system to supply the main army. INT +1",[0,0,0,1,0,0],"NONE"],
["Planned a perfect ambush. Lost no men. INT +1",[0,0,0,1,0,0],"NONE"],
["Helped out in the medical camp. Tended to the injured. WIS +1",[0,0,0,0,1,0],"NONE"],
["Infiltrated enemy headquarters. Extracted information. DEX +1",[0,1,0,0,0,0],"NONE"],
["Had an arrow pushed through and snapped off. CON +1",[0,0,1,0,0,0],"NONE"],
["Turned a double agent. CHA +1",[0,0,0,0,0,1],"NONE"],
["Nine kills during hand to hand combat. STR +1",[1,0,0,0,0,0],"NONE"],
["Identified a spy in your ranks. WIS +1",[0,0,0,0,1,0],"NONE"],
["Arm was caught in the main ropes of a war machine. CON +2, DEX -1",[0,-1,2,0,0,0],"NONE"],
["Got a ship to port after the death of your captain. INT +1",[0,0,0,1,0,0],"NONE"],
["Appointed executioner of prisoners. Beheading with an axe. STR +1",[1,0,0,0,0,0],"NONE"],
["Loaded the catapult during a siege. STR +2",[2,0,0,0,0,0],"NONE"],
["Endured hot iron branding. CON +1",[0,0,1,0,0,0],"NONE"],
["Survived several battles with numerous injuries. CON +1",[0,0,1,0,0,0],"NONE"],
["Holy words inspired your bravery and made you stronger. STR +1",[1,0,0,0,0,0],"NONE"],
["Carried two injured soldiers to safety. STR +1",[1,0,0,0,0,0],"NONE"],
["Impressed the General and received a promotion. CHA +1",[0,0,0,0,0,1],"NONE"],
["Ate the heart of your enemy. CAN +1",[0,0,0,0,0,0],"NONE"],
["Snuck onto an enemy ship and sabotaged it. DEX +1",[0,1,0,0,0,0],"NONE"],
["Fought a giant scorpion. Only got stung once. DEX +1, CON -1",[0,1,-1,0,0,0],"NONE"],
["Saw a deity on the battlefield. WIS +1",[0,0,0,0,1,0],"NONE"],
["Instigated a successful mutiny. CHA +1",[0,0,0,0,0,1],"NONE"],
["Managed supply lines for a battalion. INT +1",[0,0,0,1,0,0],"NONE"],
["Worked the crow’s nest during rough seas. DEX +1",[0,1,0,0,0,0],"NONE"],
["Carried your regimental colors. STR +1",[1,0,0,0,0,0],"NONE"],
["Appointed liaison for an occupied town. CHA +1",[0,0,0,0,0,1],"NONE"],
["Went without sleep for days while observing enemy positions. CON +1",[0,0,1,0,0,0],"NONE"],
["Hoisted up the anchor on a ship. STR +1",[1,0,0,0,0,0],"NONE"],
["Cranked back a ballista by yourself. STR +1",[1,0,0,0,0,0],"NONE"],
["Deserted a battle and escaped while being pursued. DEX +1",[0,1,0,0,0,0],"NONE"],
["Your whole body is tattooed. CON +2",[0,0,2,0,0,0],"NONE"],
["Worked the war-forge making weapons. CON+2",[0,0,0,0,0,0],"NONE"],
["Angered a group of officers. Discharged. Move to Life Experience Table.",[0,0,0,0,0,0],"LE"],
["Gambled with the officers. Took them for two months wages. CHA +1",[0,0,0,0,0,1],"NONE"],
["Bestowed honors of bravery by the King of the realm. CHA +1",[0,0,0,0,0,1],"NONE"],
["Kicked by a Calvary horse. In coma for a month. STR -1",[-1,0,0,0,0,0],"NONE"],
["Ran a message through the battlefield to the Lord in charge. DEX +1",[0,1,0,0,0,0],"NONE"],
["Screwed up. Got put on potato peeling duty. DEX +1",[0,1,0,0,0,0],"NONE"],
["Honorably disarmed and faced an enemy with fists. CHA +1",[0,0,0,0,0,1],"NONE"],
["Stuck out a one month siege of your keep. CON +1",[0,0,1,0,0,0],"NONE"],
["Fought off a pack of war dog while defending a fallen soldier. STR +1",[1,0,0,0,0,0],"NONE"],
["Buried the fallen. STR +1",[1,0,0,0,0,0],"NONE"],
["Continued fighting while you were on fire. CON +1",[0,0,1,0,0,0],"NONE"],
["Had four arrows removed from your leg. CON +1",[0,0,1,0,0,0],"NONE"],
["Disarmed an enemy trap. DEX +1",[0,1,0,0,0,0],"NONE"],
["Worked the battering ram. STR +1",[1,0,0,0,0,0],"NONE"],
["Made money dealing in contraband. Economic of war. INT +1",[0,0,0,1,0,0],"NONE"],
["Contracted disease while serving abroad. CON-1",[0,0,0,0,0,0],"NONE"],
["Saw the true face of evil and swore to destroy it. WIS +1",[0,0,0,0,1,0],"NONE"],
["Dug latrines for entire company STR +1",[1,0,0,0,0,0],"NONE"],
["Military cuts. The brightest are sent to College. Move to Academic Table.",[0,0,0,0,0,0],"AC"],

    ]
}


active_path = master_tables[active_table]
output_list = []

while len(output_list) != 12:

    #Takes path table, shuffles, and grabs a random element
    random.shuffle(active_path)
    new_item = active_path.pop()

    #adds newelement to growing list
    output_list.append(new_item)

    #changes table selection if needed
    if new_item[2] != "NONE":
        #master dictonary with tables
        active_table = new_item[2]
        active_path = master_tables[active_table]

# print(output_list)


#tallies stat point changes
base_stats = [base_stat_value] * 6
for item in output_list:
    base_stats[0] += item[1][0] #STR
    base_stats[1] += item[1][1] #DEX
    base_stats[2] += item[1][2] #CON
    base_stats[3] += item[1][3] #INT
    base_stats[4] += item[1][4] #WIS
    base_stats[5] += item[1][5] #CHA
print(base_stats)

for item in output_list:
    print(item[0])
#todo encapsulate things into functions/classes?