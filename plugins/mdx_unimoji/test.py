#!/usr/bin/env python3
# -*- coding: utf8 -*-


EMOJI = {
    '😆': ":lol: :funny: :happy: :glad: :laughing:".split(),
    '😊': ":) :-) :] :-] =) =] ^^ ^_^ :smile: :crush: :embarrassed: :shy: :blush:".split(),
    '😃': ":smiley:".split(),
    '😏': ":> :-> :mean: :smug: :smirk:".split(),
    '😍': ":crush: :heart_eyes:".split(),
    '😘': "';* ;-* :kiss: :kissing_heart:".split(),
    '😚': ":* :-* :kissing_closed_eyes:".split(),
    '😳': ":$ :-$ :flustered: :embarassed: :flattered: :flushed:".split(),
    '😌': ":relaxed: :phew: :massage: :happiness: :relieved:".split(),
    '😆': "xD XD :contented: :satisfied:".split(),
    '😁': ":grin:".split(),
    '😉': ";) ;-) ;] ;-] :flirt: :mischievous: :secret: :wink:".split(),
    '😜': ";p ;-p ;P ;-P :childish: :mischievous: :stuck_out_tongue_winking_eye:".split(),
    '😝': ":mischievous: :stuck_out_tongue_closed_eyes:".split(),
    '😀': ":smiling: :grinning:".split(),
    '😗': ":3: :kissing:".split(),
    '😙': ":smooch: :kissing_smiling_eyes:".split(),
    '😛': ":p :-p :P :-P =p =P :childish: :playful: :mischievous: :stuck_out_tongue:".split(),
    '😴': ":asleep: :tired: :sleepy: :night: :zzz: :sleeping:".split(),
    '😟': ":frustrated: :scared: :concern: :nervous: :worried:".split(),
    '😦': ":aw: :what: :frowning:".split(),
    '😧': ":stunned: :nervous: :anguished:".split(),
    '😮': ":surprise: :impressed: :wow: :open_mouth:".split(),
    '😬': ":grimace: :teeth: :grimacing:".split(),
    '😕': ":baffled: :puzzled: :indifference: :huh: :weird: :hmmm: :confused:".split(),
    '😯': ":woo: :shh: :conceal: :hide:".split(),
    '😑': "-_- :deadpan: :indifferent: :meh: :expressionless:".split(),
    '😒': ":/ :-/ :\\ :-\\ =/ =\\ :L :sarcasm: :indifference: :bored: :straight: :serious: :unamused:".split(),
    '😅': ":relief: :laugh: :sweat_smile:".split(),
    '😓': ":-X :X :-# :# :-& :& :stressed: :tired: :exercise: :sweat:".split(),
    '😥': ":phew: :sweat: :nervous: :disappointed_relieved:".split(),
    '😩': ":tired: :sleepy: :frustrated: :upset: :weary:".split(),
    '😔': ":depressed: :okay: :upset: :pensive:".split(),
    '😞': ":( :-( ;( ;-( =( =[ :lonely: :upset: :depressed: :disappointed:".split(),
    '😖': ":s :-s :S :-S :confused: :sick: :unwell: :oops: :confounded:".split(),
    '😨': ":scared: :afraid: :nervous: :scared: :terrified: :oops: :huh: :fearful:".split(),
    '😰': ":scared: :frightened: :nervous: :scared: :cold_sweat:".split(),
    '😣': "x( X( :sick: :no: :upset: :oops: :persevere:".split(),
    '😢': ":,( :'( =,( ='( :tear: :tears: :depressed: :upset: :cry:".split(),
    '😭': ":sad: :cry: :tears: :upset: :depressed: :sob:".split(),
    '😂': ":,D :'D =,D ='D :happytears: :cry: :tears: :weep: :haha: :joy:".split(),
    '😲': ":O :-O 8-O =O :xox: :surprised: :poisoned: :astonished:".split(),
    '😱': ":halloween: :scary: :scared: :terrified: :munch: :omg: :scream:".split(),
    '😫': ":sick: :whine: :upset: :frustrated: :tired_face:".split(),
    '😠': ">:( >=( :mad: :annoyed: :frustrated: :angry:".split(),
    '😡': ":furious: :mad: :hate: :despise: :rage:".split(),
    '😤': ":gas: :phew: :proud: :pride: :triumph:".split(),
    '😪': ":tired: :zzz: :rest: :nap: :sleepy:".split(),
    '😋': ":delicious: :tongue: :silly: :yummy: :yum:".split(),
    '😷': ":sick: :ill: :disease: :mask:".split(),
    '😎': "8) 8-) :shades: :sunglasses:".split(),
    '😵': "x-O X-O :ko: :spent: :unconscious: :xox: :dizzy_face:".split(),
    '👿': ":devil: :horns: :imp:".split(),
    '😈': "3:) 3:-) >:) >:-) >;) >;-) :devil: :horns: :smiling_imp:".split(),
    '😐': ":indifference: :meh: :neutral_face:".split(),
    '😶': ":hellokitty: :silent:".split(),
    '😇': "O:) O:-) :angel: :heaven: :halo: :innocent:".split(),
    '👽': ":extraterrestrial: :UF:O :paul: :weird: :outer_space: :alien:".split(),
    '💛': ":yellow_heart:".split(),
    '💙': ":blue_heart:".split(),
    '💜': ":purple_heart:".split(),
    '❤': "<3 :heart:".split(),
    '💚': ":green_heart:".split(),
    '💔': "</3 :sorry: :break: :broken_heart:".split(),
    '💓': ":heartbeat:".split(),
    '💗': ":heartpulse:".split(),
    '💕': ":two_hearts:".split(),
    '💞': ":revolving_hearts:".split(),
    '💘': ":cupid:".split(),
    '💖': ":sparkling_heart:".split(),
    '✨': ":stars: :shine: :shiny: :awesome: :good: :magic: :sparkles:".split(),
    '⭐': ":night: :star:".split(),
    '💫': ":sparkle: :shoot: :dizzy:".split(),
    '💥': ":explosion: :bomb: :explode: :collision: :blown: :boom: :accident: :fight: :boom:".split(),
    '💢': ":mad: :anger:".split(),
    '❗': ":heavy_exclamation_mark: :danger: :surprise: :punctuation: :wow: :warning: :exclamation:".split(),
    '❓': ":doubt: :confused: :question:".split(),
    '❕': ":surprise: :punctuation: :gray: :wow: :warning: :grey_exclamation:".split(),
    '❔': ":doubts: :gray: :huh: :grey_question:".split(),
    '💤': ":sleep: :bored: :sleepy: :tired: :zzz:".split(),
    '💨': ":wind: :air: :fast: :shoo: :fart: :smoke: :puff: :dash:".split(),
    '💦': ":drip: :oops: :sweat_drops:".split(),
    '🎶': ":notes:".split(),
    '🎵': ":tone: :musical_note:".split(),
    '🔥': ":cook: :flame: :fire:".split(),
    '💩': ":poop: :shitface: :fail: :turd: :hankey:".split(),
    '💩': ":shit: :turd: :poop:".split(),
    '💩': ":poop: :shit:".split(),
    '👍': ":thumbsup: :yes: :agree: :accept: :cool: :+1:".split(),
    '👎': ":dislike: :no: :thumbsdown: :-1:".split(),
    '👌': ":limbs: :perfect: :ok_hand:".split(),
    '👊': ":pound: :punch:".split(),
    '👊': ":violence: :fist: :hit: :attack: :facepunch:".split(),
    '✊': ":grasp: :fist:".split(),
    '✌': ":peace: :deuces: :ohyeah: :victory: :two: :v:".split(),
    '👋': ":hi: :hello: :bye: :hands: :gesture: :goodbye: :solong: :farewell: :palm: :wave:".split(),
    '✋': ":stop: :highfive: :palm: :ban: :raised_hand: :hand:".split(),
    '✋': ":raised_hand:".split(),
    '👐': ":butterfly: :open_hands:".split(),
    '☝': ":point_up:".split(),
    '👇': ":point_down:".split(),
    '👈': ":point_left:".split(),
    '👉': ":point_right:".split(),
    '🙌': "\\o/ :gesture: :hooray: :yea: :celebration: :raised_hands:".split(),
    '🙏': ":please: :hope: :wish: :namaste: :pray:".split(),
    '👏': ":hands: :praise: :applause: :congrats: :yay: :clap:".split(),
    '💪': ":arm: :flex: :strong: :muscle:".split(),
    '🏃': ":walking: :exercise: :race: :running: :runner:".split(),
    '🏃': ":running:".split(),
    '👫': ":date: :dating: :marriage: :couple:".split(),
    '👪': ":parents: :family:".split(),
    '👬': ":gay: :couple: :bromance: :friendship: :two_men_holding_hands:".split(),
    '👭': ":gay: :friendship: :couple: :lesbian: :two_women_holding_hands:".split(),
    '💃': ":dancer:".split(),
    '👯': ":bunny: :girls: :dancers:".split(),
    '🙆': ":ok_woman:".split(),
    '🙅': ":nope: :no_good:".split(),
    '💁': ":information_desk_person:".split(),
    '🙋': ":raising_hand:".split(),
    '👰': ":couple: :marriage: :wedding: :bride_with_veil:".split(),
    '🙎': ":person_with_pouting_face:".split(),
    '🙍': ":depressed: :discouraged: :person_frowning:".split(),
    '🙇': ":bow:".split(),
    '💏': ":dating: :marriage: :couplekiss:".split(),
    '💑': ":dating: :marriage: :couple_with_heart:".split(),
    '💆': ":head: :massage:".split(),
    '💇': ":haircut:".split(),
    '💅': ":manicure: :beauty: :finger: :nail_care:".split(),
    '👦': ":boy:".split(),
    '👧': ":girl:".split(),
    '👩': ":girls: :lady: :woman:".split(),
    '👨': ":mustache: :dad: :classy: :sir: :moustache: :man:".split(),
    '👶': ":infant: :child: :toddler: :baby:".split(),
    '👵': ":grandma: :granny: :lady: :older_woman:".split(),
    '👴': ":grandpa: :grandad: :men: :older_man:".split(),
    '👱': ":blonde: :person_with_blond_hair:".split(),
    '👲': ":man_with_gua_pi_mao:".split(),
    '👳': ":indian: :hinduism: :arabs: :man_with_turban:".split(),
    '👷': ":wip: :build: :construction_worker:".split(),
    '👮': ":police: :policeman: :arrest: :911: :cop:".split(),
    '👼': ":heaven: :wings: :halo: :angel:".split(),
    '👸': ":blond: :crown: :royal: :queen: :princess:".split(),
    '😺': ":^D =^D :smiley_cat:".split(),
    '😸': ":^) :} :-} :3 :-3 :smile_cat:".split(),
    '😻': ":heart_eyes_cat:".split(),
    '😽': ":kissing_cat:".split(),
    '😼': ":smirk_cat:".split(),
    '🙀': ":munch: :scared: :scream_cat:".split(),
    '😿': ":^( :{ :tears: :weep: :upset: :crying_cat_face:".split(),
    '😹': ":haha: :tears: :joy_cat:".split(),
    '😾': ":pouting_cat:".split(),
    '👹': ":namahage: :monster: :mask: :halloween: :scary: :creepy: :devil: :demon: :japanese_ogre:".split(),
    '👺': ":tengu: :evil: :mask: :monster: :scary: :creepy: :japanese_goblin:".split(),
    '🙈': ":haha: :see_no_evil:".split(),
    '🙉': ":hear_no_evil:".split(),
    '🙊': ":omg: :speak_no_evil:".split(),
    '💂': ":royal: :guardsman:".split(),
    '💀': ":scary: :halloween: :dead: :skeleton: :creepy: :skull:".split(),
    '🐾': ":tracking: :footprints: :dog: :cat: :paw_prints: :feet:".split(),
    '👄': ":mouth: :kiss: :lips:".split(),
    '💋': ":lips: :kiss:".split(),
    '💧': ":drip: :faucet: :droplet:".split(),
    '👂': ":hear: :listen: :ear:".split(),
    '👀': ":eye-rolling: :look: :watch: :stalk: :peek: :see: :eyes:".split(),
    '👃': ":smell: :sniff: :nose:".split(),
    '👅': ":mouth: :playful: :tongue:".split(),
    '💌': ":envelope: :love_letter:".split(),
    '👤': ":user: :person: :bust_in_silhouette:".split(),
    '👥': ":group: :team: :busts_in_silhouette:".split(),
    '💬': ":bubble: :message: :talk: :chatting: :speech_balloon:".split(),
    '💭': ":cloud: :speech: :thinking: :thought_balloon:".split(),
    '☀': ":brightness: :sunny:".split(),
    '☂': ":rain: :rainy: :umbrella:".split(),
    '☁': ":sky: :cloud:".split(),
    '❄': ":snowflake:".split(),
    '☃': ":frozen: :snowman: :snowmen:".split(),
    '⚡': ":lightning: :thunder: :lightning: :bolt: :fast: :zap:".split(),
    '🌀': ":swirl: :cloud: :cyclone:".split(),
    '🌁': ":fog: :mountain: :foggy:".split(),
    '🌊': ":waves: :wave: :tsunami: :disaster: :ocean:".split(),
    '🐱': ":meow: :cat:".split(),
    '🐶': ":friend: :woof: :puppy: :faithful: :dog:".split(),
    '🐭': ":cheese: :mouse:".split(),
    '🐹': ":hamster:".split(),
    '🐰': ":rabbit:".split(),
    '🐺': ":wild: :audrey: :lulu:".split(),
    '🐸': ":croak: :frog:".split(),
    '🐯': ":cat: :danger: :wild: :roar: :tiger:".split(),
    '🐨': ":koala:".split(),
    '🐻': ":wild: :bear:".split(),
    '🐷': ":oink: :pig:".split(),
    '🐽': ":oink: :pig_nose:".split(),
    '🐮': ":beef: :ox: :moo: :milk: :cow:".split(),
    '🐗': ":boar:".split(),
    '🐵': ":ape: :monkey_face:".split(),
    '🐒': ":ape: :monkey:".split(),
    '🐴': ":brown: :unicorn: :horse:".split(),
    '🐎': ":gamble: :luck: :racehorse:".split(),
    '🐫': ":desert: :hump: :camel:".split(),
    '🐑': ":wool: :shipit: :sheep:".split(),
    '🐘': ":nose: :thailand: :elephant:".split(),
    '🐼': ":panda_face:".split(),
    '🐍': ":serpent: :evil: :hiss: :snake:".split(),
    '🐦': ":fly: :tweet: :bird:".split(),
    '🐤': ":baby_chick:".split(),
    '🐥': ":baby: :hatched_chick:".split(),
    '🐣': ":bird-egg: :egg: :born: :baby: :hatching_chick:".split(),
    '🐔': ":cluck: :chicken:".split(),
    '🐧': ":penguin:".split(),
    '🐢': ":tortoise: :turtle:".split(),
    '🐛': ":worm: :bug:".split(),
    '🐝': ":honeybee:".split(),
    '🐜': ":insect: :ant:".split(),
    '🐞': ":beetle:".split(),
    '🐌': ":slow: :shell: :snail:".split(),
    '🐙': ":creature: :octopus:".split(),
    '🐠': ":swim: :nemo: :tropical_fish:".split(),
    '🐟': ":fish:".split(),
    '🐳': ":whale:".split(),
    '🐬': ":fish: :flipper: :fins: :dolphin:".split(),
    '🐏': ":sheep: :ram:".split(),
    '🐀': ":mouse: :rodent: :rat:".split(),
    '🐃': ":ox: :cow: :water_buffalo:".split(),
    '🐉': ":dragon:".split(),
    '🐐': ":goat:".split(),
    '🐓': ":rooster:".split(),
    '🐂': ":cow: :beef: :ox:".split(),
    '🐲': ":dragon_face:".split(),
    '🐡': ":blowfish:".split(),
    '🐊': ":alligator: :reptile: :crocodile:".split(),
    '🐪': ":desert: :hump: :dromedary_camel:".split(),
    '🐆': ":leopard:".split(),
    '🐩': ":dog: :101: :poodle:".split(),
    '🐾': ":paw_prints:".split(),
    '💐': ":bouquet:".split(),
    '🌸': ":flower: :cherry_blossom:".split(),
    '🌷': ":tulip:".split(),
    '🍀': ":lucky: :four_leaf_clover:".split(),
    '🌹': ":rose:".split(),
    '🌻': ":fall: :sunflower:".split(),
    '🌺': ":beach: :hibiscus:".split(),
    '🍁': ":canada: :fall: :maple_leaf:".split(),
    '🍃': ":tree: :grass: :lawn: :leaves:".split(),
    '🍂': ":leaves: :fallen_leaf:".split(),
    '🌿': ":medicine: :weed: :grass: :lawn: :herb:".split(),
    '🍄': ":mushroom:".split(),
    '🌵': ":cactus:".split(),
    '🌴': ":beach: :palm_tree:".split(),
    '🌲': ":evergreen_tree:".split(),
    '🌳': ":deciduous_tree:".split(),
    '🌰': ":squirrel: :chestnut:".split(),
    '🌱': ":grass: :lawn: :seedling:".split(),
    '🌼': ":blossom:".split(),
    '🌾': ":ear_of_rice:".split(),
    '🐚': ":beach: :shell:".split(),
    '🌐': ":earth: :international: :world: :internet: :interweb: :i18n: :globe_with_meridians:".split(),
    '🌞': ":sky: :sun_with_face:".split(),
    '🌝': ":full_moon_with_face:".split(),
    '🌚': ":new_moon_with_face:".split(),
    '🌑': ":new_moon:".split(),
    '🌒': ":waxing_crescent_moon:".split(),
    '🌓': ":first_quarter_moon:".split(),
    '🌔': ":waxing_gibbous_moon:".split(),
    '🌕': ":full_moon:".split(),
    '🌖': ":waxing_gibbous_moon: :waning_gibbous_moon:".split(),
    '🌗': ":last_quarter_moon:".split(),
    '🌘': ":waning_crescent_moon:".split(),
    '🌜': ":last_quarter_moon_with_face:".split(),
    '🌛': ":first_quarter_moon_with_face:".split(),
    '🌙': ":night: :sleep: :sky: :evening: :crescent_moon:".split(),
    '🌍': ":europe: :emea: :globe: :world: :international: :earth_africa:".split(),
    '🌎': ":globe: :world: :USA: :international: :earth_americas:".split(),
    '🌏': ":globe: :world: :east: :international: :earth_asia:".split(),
    '🌋': ":disaster: :volcano:".split(),
    '🌌': ":space: :stars: :milky_way:".split(),
    '⛅': ":cloudy: :fall: :partly_sunny:".split(),
    '🎍': ":panda: :bamboo:".split(),
    '💝': ":gift_heart:".split(),
    '🎎': ":toy: :kimono: :dolls:".split(),
    '🎒': ":student: :education: :bag: :school_satchel:".split(),
    '🎓': ":edu: :university: :college: :degree: :graduation: :cap: :hat: :learn: :education: :mortar_board:".split(),
    '🎏': ":fish: :koinobori: :carp: :banner: :flags:".split(),
    '🎆': ":carnival: :congratulations: :fireworks:".split(),
    '🎇': ":stars: :night: :sparkler:".split(),
    '🎐': ":ding: :bell: :wind_chime:".split(),
    '🎑': ":japan: :asia: :tsukimi: :rice_scene:".split(),
    '🎃': ":halloween: :light: :pumpkin: :creepy: :fall: :jack_o_lantern:".split(),
    '👻': ":boom: :halloween: :spooky: :scary: :ghost:".split(),
    '🎅': ":xmas: :christmas: :santa:".split(),
    '🎄': ":december: :celebration: :christmas_tree:".split(),
    '🎁': ":present: :gift:".split(),
    '🔔': ":notification: :chime: :bell:".split(),
    '🔕': ":mute: :quiet: :silent: :no_bell:".split(),
    '🎋': ":branch: :tanabata_tree:".split(),
    '🎉': ":contulations: :tada:".split(),
    '🎊': ":celebration: :confetti_ball:".split(),
    '🎈': ":celebration: :balloon:".split(),
    '🔮': ":disco: :fortune_teller: :crystal_ball:".split(),
    '💿': ":dvd: :disk: :disc: :cd:".split(),
    '📀': ":cd: :disk: :disc: :dvd:".split(),
    '💾': ":floppy_disk:".split(),
    '📷': ":gadgets: :camera:".split(),
    '📹': ":film: :record: :video_camera:".split(),
    '🎥': ":film: :record: :movie_camera:".split(),
    '💻': ":tech: :laptop: :screen: :display: :monitor: :computer:".split(),
    '📺': ":television: :program: :show: :tv:".split(),
    '📱': ":apple: :gadgets: :dial: :iphone:".split(),
    '☎': ":dial: :telephone: :phone:".split(),
    '☎': ":calling: :telephone:".split(),
    '📞': ":dial: :telephone_receiver:".split(),
    '📟': ":bbcall: :pager:".split(),
    '📠': ":fax:".split(),
    '💽': ":data: :disk: :minidisc:".split(),
    '📼': ":record: :video: :vhs:".split(),
    '🔉': ":loud: :noise: :speaker: :broadcast: :sound:".split(),
    '🔈': ":silence: :broadcast: :speaker:".split(),
    '🔇': ":silence: :quiet: :mute:".split(),
    '📢': ":loudspeaker:".split(),
    '📣': ":speaker: :mega:".split(),
    '⌛': ":time: :clock: :limit: :exam: :quiz: :test: :hourglass:".split(),
    '⏳': ":time: :countdown: :hourglass_flowing_sand:".split(),
    '⏰': ":time: :wake: :alarm_clock:".split(),
    '⌚': ":clock: :time: :watch:".split(),
    '📻': ":podcast: :program: :radio:".split(),
    '📡': ":future: :radio: :space: :satellite:".split(),
    '➿': ":tape: :cassette: :loop:".split(),
    '🔍': ":magnifying: :glass: :search: :zoom: :find: :detective: :mag:".split(),
    '🔎': ":mag_right:".split(),
    '🔓': ":privacy: :unlock:".split(),
    '🔒': ":password: :padlock: :lock:".split(),
    '🔏': ":secret: :lock_with_ink_pen:".split(),
    '🔐': ":closed_lock_with_key:".split(),
    '🔑': ":lock: :door: :password: :key:".split(),
    '💡': ":light: :electricity: :idea: :bulb:".split(),
    '🔦': ":dark: :camping: :sight: :night: :flashlight:".split(),
    '🔆': ":light: :high_brightness:".split(),
    '🔅': ":afternoon: :warm: :low_brightness:".split(),
    '🔌': ":charger: :power: :electric_plug:".split(),
    '🔋': ":power: :energy: :sustain: :battery:".split(),
    '📲': ":iphone: :incoming: :calling:".split(),
    '✉': ":envelope: :postal: :letter:".split(),
    '📫': ":inbox: :mailbox:".split(),
    '📮': ":envelope: :postbox:".split(),
    '🛀': ":clean: :shower: :bathroom: :bath:".split(),
    '🛁': ":clean: :shower: :bathroom: :bathtub:".split(),
    '🚿': ":clean: :bathroom: :shower:".split(),
    '🚽': ":restroom: :wc: :washroom: :bathroom: :potty: :toilet:".split(),
    '🔧': ":diy: :ikea: :fix: :maintainer: :wrench:".split(),
    '🔩': ":handy: :fix: :nut_and_bolt:".split(),
    '🔨': ":verdict: :judge: :done: :ruling: :gavel: :hammer:".split(),
    '💺': ":sit: :airplane: :transport: :bus: :flight: :fly: :seat:".split(),
    '💰': ":payment: :coins: :sale: :moneybag:".split(),
    '💴': ":currency: :yen:".split(),
    '💵': ":bill: :currency: :dollar:".split(),
    '💷': ":sterling: :bills: :england: :currency: :pound:".split(),
    '💶': ":currency: :euro:".split(),
    '💳': ":payment: :credit_card:".split(),
    '💸': ":bills: :payment: :sale: :money_with_wings:".split(),
    '📧': ":send: :e:".split(),
    '📥': ":inbox_tray:".split(),
    '📤': ":inbox: :outbox_tray:".split(),
    '✉': ":message: :envelope:".split(),
    '📨': ":inbox: :incoming_envelope:".split(),
    '📯': ":postal_horn:".split(),
    '📪': ":inbox: :mailbox_closed:".split(),
    '📬': ":mailbox_with_mail:".split(),
    '📭': ":mailbox_with_no_mail:".split(),
    '📦': ":box: :gift: :cardboard: :moving: :package:".split(),
    '🚪': ":house: :entry: :exit: :door:".split(),
    '🚬': ":smoke: :kills: :tobacco: :cigarette: :joint: :smoking:".split(),
    '💣': ":boom: :explode: :explosion: :terrorism: :bomb:".split(),
    '🔫': ":violence: :pistol: :revolver: :gun:".split(),
    '🔪': ":knife: :blade: :cutlery: :kitchen: :hocho:".split(),
    '💊': ":medicine: :doctor: :pharmacy: :drug: :pill:".split(),
    '💉': ":hospital: :drugs: :blood: :medicine: :needle: :doctor: :nurse: :syringe:".split(),
    '📄': ":paper: :information: :page_facing_up: :documents:".split(),
    '📃': ":page_with_curl:".split(),
    '📑': ":favorite: :order: :tidy: :bookmark_tabs:".split(),
    '📊': ":bar_chart:".split(),
    '📈': ":recovery: :success: :chart_with_upwards_trend:".split(),
    '📉': ":recession: :failure: :chart_with_downwards_trend:".split(),
    '📜': ":ancient: :history: :scroll:".split(),
    '📋': ":clipboard:".split(),
    '📆': ":schedule: :date: :planning: :calendar:".split(),
    '📅': ":calendar: :date:".split(),
    '📇': ":card_index:".split(),
    '📁': ":file_folder:".split(),
    '📂': ":load: :open_file_folder:".split(),
    '✂': ":cut: :scissors:".split(),
    '📌': ":mark: :here: :pushpin:".split(),
    '📎': ":paperclip:".split(),
    '✒': ":pen: :writing: :write: :black_nib:".split(),
    '📏': ":calculate: :length: :drawing: :architect: :sketch: :straight_ruler:".split(),
    '📐': ":architect: :sketch: :triangular_ruler:".split(),
    '📕': ":learn: :closed_book:".split(),
    '📗': ":study: :green_book:".split(),
    '📘': ":learn: :study: :blue_book:".split(),
    '📙': ":study: :orange_book:".split(),
    '📓': ":record: :notes: :study: :notebook:".split(),
    '📔': ":classroom: :notes: :record: :study: :notebook_with_decorative_cover:".split(),
    '📒': ":notes: :ledger:".split(),
    '📚': ":literature: :study: :books:".split(),
    '🔖': ":favorite: :label: :bookmark:".split(),
    '📛': ":fire: :forbid: :name_badge:".split(),
    '🔬': ":laboratory: :experiment: :zoomin: :science: :study: :microscope:".split(),
    '🔭': ":stars: :space: :zoom: :telescope:".split(),
    '📰': ":press: :headline: :newspaper:".split(),
    '🏈': ":football:".split(),
    '🏀': ":basketball:".split(),
    '⚽': ":football: :fifa: :soccer:".split(),
    '⚾': ":baseball:".split(),
    '🎾': ":tennis:".split(),
    '🏉': ":team: :rugby_football:".split(),
    '🎳': ":bowling:".split(),
    '⛳': ":flag: :hole: :golf:".split(),
    '🚵': ":race: :bike: :mountain_bicyclist:".split(),
    '🚴': ":bike: :exercise: :hipster: :bicyclist:".split(),
    '🏇': ":betting: :competition: :gambling: :luck: :horse_racing:".split(),
    '🏂': ":snowboarder:".split(),
    '🏊': ":exercise: :athlete: :swimmer:".split(),
    '🏄': ":beach: :surfer:".split(),
    '🎿': ":snow: :ski:".split(),
    '♠': ":spades:".split(),
    '♥': ":hearts:".split(),
    '♣': ":clubs:".split(),
    '♦': ":diamonds:".split(),
    '💎': ":ruby: :diamond: :jewelry: :gem:".split(),
    '💍': ":wedding: :propose: :marriage: :diamond: :jewelry: :gem: :ring:".split(),
    '🏆': ":win: :award: :contest: :place: :ftw: :ceremony: :trophy:".split(),
    '🎼': ":treble: :clef: :musical_score:".split(),
    '🎹': ":piano: :musical_keyboard:".split(),
    '🎻': ":orchestra: :symphony: :violin:".split(),
    '👾': ":arcade: :space_invader:".split(),
    '🎮': ":controller: :console: :PS4: :video_game:".split(),
    '🃏': ":poker: :cards: :black_joker:".split(),
    '🎴': ":sunset: :flower_playing_cards:".split(),
    '🎲': ":dice: :random: :tabbletop: :luck: :game_die:".split(),
    '🎯': ":dart:".split(),
    '🀄': ":kanji: :mahjong:".split(),
    '🎬': ":movie: :film: :record: :clapper:".split(),
    '📝': ":writing: :exam: :quiz: :test: :study: :memo:".split(),
    '📝': ":write: :pencil:".split(),
    '📖': ":open_book: :literature: :learn: :study: :book:".split(),
    '🎨': ":design: :paint: :draw: :art:".split(),
    '🎤': ":PA: :microphone:".split(),
    '🎧': ":gadgets: :headphones:".split(),
    '🎺': ":brass: :trumpet:".split(),
    '🎷': ":jazz: :blues: :saxophone:".split(),
    '🎸': ":guitar:".split(),
    '👞': ":shoes:".split(),
    '👠': ":pumps: :stiletto: :high_heel:".split(),
    '💄': ":lipstick:".split(),
    '👢': ":shoes: :boot:".split(),
    '👕': ":formal:".split(),
    '👕': ":casual: :tee:".split(),
    '👔': ":shirt: :suitup: :formal: :necktie:".split(),
    '👚': ":womans_clothes:".split(),
    '👗': ":clothes: :dress:".split(),
    '🎽': ":pageant: :running_shirt_with_sash:".split(),
    '👖': ":jeans:".split(),
    '👘': ":dress: :kimono:".split(),
    '👙': ":swimming: :bikini:".split(),
    '🎀': ":decoration: :bowtie: :ribbon:".split(),
    '🎩': ":magic: :gentleman: :classy: :tophat:".split(),
    '👑': ":king: :kod: :leader: :royalty: :lord: :crown:".split(),
    '👒': ":lady: :womans_hat:".split(),
    '👞': ":mans_shoe:".split(),
    '🌂': ":drizzle: :closed_umbrella:".split(),
    '💼': ":work: :briefcase:".split(),
    '👜': ":accessory: :handbag:".split(),
    '👝': ":bag: :pouch:".split(),
    '👛': ":pocketbook: :purse:".split(),
    '👓': ":eyesight: :nerd: :dork: :geek: :eyeglasses:".split(),
    '🎣': ":hobby: :fishing_pole_and_fish:".split(),
    '☕': ":cafe: :espresso: :coffee:".split(),
    '🍵': ":bowl: :tea:".split(),
    '🍶': ":wine: :drunk: :sake:".split(),
    '🍼': ":container: :milk: :baby_bottle:".split(),
    '🍺': ":relax: :drunk: :pub: :beer:".split(),
    '🍻': ":beers:".split(),
    '🍸': ":booze: :cocktail:".split(),
    '🍹': ":tropical_drink:".split(),
    '🍷': ":drunk: :wine_glass:".split(),
    '🍴': ":cutlery: :kitchen: :fork_and_knife:".split(),
    '🍕': ":pizza:".split(),
    '🍔': "meat :fast_food: :beef: :cheeseburger: :mcdonalds: :burger: :king:".split(),
    '🍟': ":chips: :fast: :food:".split(),
    '🍗': ":drumstick: :turkey: :poultry_leg:".split(),
    '🍖': ":good: :drumstick: :meat_on_bone:".split(),
    '🍝': ":noodles: :noodle: :spaghetti:".split(),
    '🍛': ":indian: :spicy: :curry:".split(),
    '🍤': ":seafood: :appetizer: :fried_shrimp:".split(),
    '🍱': ":box: :bento:".split(),
    '🍣': ":fish: :rice: :sushi:".split(),
    '🍥': ":seafood :naruto: :japan: :fish_cake:".split(),
    '🍙': ":rice_ball:".split(),
    '🍘': ":rice_cracker:".split(),
    '🍚': ":china: :asian: :rice:".split(),
    '🍜': ":noodles: :noodle: :chipsticks: :ramen:".split(),
    '🍲': ":soup: :stew:".split(),
    '🍢': ":oden:".split(),
    '🍡': ":barbecue: :dango:".split(),
    '🍳': ":kitchen: :egg:".split(),
    '🍞': ":toast: :bread:".split(),
    '🍩': ":donut: :doughnut:".split(),
    '🍮': ":custard:".split(),
    '🍦': ":icecream:".split(),
    '🍨': ":ice_cream:".split(),
    '🍧': ":shaved_ice:".split(),
    '🎂': ":cake: :celebration: :birthday:".split(),
    '🍰': ":cake:".split(),
    '🍪': ":oreo: :chocolate: :cookie:".split(),
    '🍫': ":chocolate_bar:".split(),
    '🍬': ":candy:".split(),
    '🍭': ":lollipop:".split(),
    '🍯': ":bees: :kitchen: :honey_pot:".split(),
    '🍎': ":mac: :apple:".split(),
    '🍏': ":green_apple:".split(),
    '🍊': ":tangerine:".split(),
    '🍋': ":lemon:".split(),
    '🍒': ":cherries:".split(),
    '🍇': ":wine: :grapes:".split(),
    '🍉': ":picnic: :watermelon:".split(),
    '🍓': ":strawberry:".split(),
    '🍑': ":peach:".split(),
    '🍈': ":melon:".split(),
    '🍌': ":banana:".split(),
    '🍐': ":pear:".split(),
    '🍍': ":pineapple:".split(),
    '🍠': ":sweet_potato:".split(),
    '🍆': ":aubergine: :eggplant:".split(),
    '🍅': ":tomato:".split(),
    '🌽': ":corn:".split(),
    '🏠': ":house:".split(),
    '🏡': ":house_with_garden:".split(),
    '🏫': ":student: :education: :learn: :teach: :school:".split(),
    '🏢': ":unit: :bureau: :office:".split(),
    '🏣': ":post_office:".split(),
    '🏥': ":surgery: :doctor: :hospital:".split(),
    '🏦': ":cash: :enterprise: :bank:".split(),
    '🏪': ":groceries: :convenience_store:".split(),
    '🏩': ":dating: :love_hotel:".split(),
    '🏨': ":whotel: :accomodation: :checkin: :hotel:".split(),
    '💒': ":couple: :marriage: :bride: :groom: :church: :wedding:".split(),
    '⛪': ":religion: :christ: :church:".split(),
    '🏬': ":mall: :department_store:".split(),
    '🏤': ":european_post_office:".split(),
    '🌇': ":good_morning: :dawn: :city_sunrise:".split(),
    '🌆': ":evening: :sky: :buildings: :city_sunset:".split(),
    '🏯': ":asia: :japanese_castle:".split(),
    '🏰': ":royalty: :history: :european_castle:".split(),
    '⛺': ":camping: :camp: :outdoors: :tent:".split(),
    '🏭': ":industry: :pollution: :smoke: :factory:".split(),
    '🗼': ":asia: :tokyo_tower:".split(),
    '🗾': ":nation: :country: :asia: :island: :japan:".split(),
    '🗻': ":mountain: :mount_fuji:".split(),
    '🌄': ":view: :sunrise_over_mountains:".split(),
    '🌅': ":view: :sunrise:".split(),
    '🌠': ":night: :falling: :sky: :bright: :stars:".split(),
    '🗽': ":newyork: :monument: :head: :statue_of_liberty:".split(),
    '🌉': ":sanfrancisco: :bridge_at_night:".split(),
    '🎠': ":carnival: :ride: :carousel_horse:".split(),
    '🌈': ":unicorn: :sky: :color: :rainbow:".split(),
    '🎡': ":carnival: :londoneye: :ferris_wheel:".split(),
    '⛲': ":fresh: :fountain:".split(),
    '🎢': ":carnival: :playground: :ride: :roller_coaster:".split(),
    '🚢': ":titanic: :deploy: :cruise: :ship:".split(),
    '🚤': ":speedboat:".split(),
    '⛵': ":sailing: :sailboat: :boat:".split(),
    '⛵': ":sailboat:".split(),
    '🚣': ":hobby: :rowboat:".split(),
    '⚓': ":ferry: :boat: :anchor:".split(),
    '🚀': ":launch: :staffmode: :NASA: :outer_space: :outer_space: :fly: :rocket:".split(),
    '✈': ":flight: :fly: :airplane:".split(),
    '🚁': ":fly: :helicopter:".split(),
    '🚂': ":train: :steam_locomotive:".split(),
    '🚊': ":tram:".split(),
    '🚞': ":mountain_railway:".split(),
    '🚲': ":bicycle: :exercise: :hipster: :bike:".split(),
    '🚡': ":ski: :aerial_tramway:".split(),
    '🚟': ":suspension_railway:".split(),
    '🚠': ":ski: :mountain_cableway:".split(),
    '🚜': ":farming: :agriculture: :tractor:".split(),
    '🚙': ":blue_car:".split(),
    '🚘': ":oncoming_automobile:".split(),
    '🚗': ":car:".split(),
    '🚗': ":red_car:".split(),
    '🚕': ":uber: :taxi:".split(),
    '🚖': ":uber: :oncoming_taxi:".split(),
    '🚛': ":express: :articulated_lorry:".split(),
    '🚌': ":bus:".split(),
    '🚍': ":oncoming_bus:".split(),
    '🚨': ":police: :ambulance: :911: :emergency: :alert: :error: :pinged: :rotating_light:".split(),
    '🚓': ":police_car:".split(),
    '🚔': ":911: :oncoming_police_car:".split(),
    '🚒': ":fire_engine:".split(),
    '🚑': ":911: :hospital: :ambulance:".split(),
    '🚐': ":minibus:".split(),
    '🚚': ":truck:".split(),
    '🚋': ":carriage: :public: :travel: :train:".split(),
    '🚉': ":public: :station:".split(),
    ':train2:': ":train2:".split(),
    '🚅': ":speed: :fast: :public: :travel: :bullettrain_front:".split(),
    '🚄': ":bullettrain_side:".split(),
    '🚈': ":light_rail:".split(),
    '🚝': ":monorail:".split(),
    '🚃': ":railway_car:".split(),
    '🚎': ":bart: :trolleybus:".split(),
    '🎫': ":event: :concert: :pass: :ticket:".split(),
    '⛽': ":gasstation: :petroleum: :fuelpump:".split(),
    '🚦': ":driving: :vertical_traffic_light:".split(),
    '🚥': ":stoplight: :signal: :traffic_light:".split(),
    '⚠': ":exclamation: :wip: :alert: :error: :problem: :issue: :warning:".split(),
    '🚧': ":wip: :progress: :caution: :warning: :construction:".split(),
    '🔰': ":badge: :shield: :beginner:".split(),
    '🏧': ":cash: :payment: :bank: :atm:".split(),
    '🎰': ":bet: :gamble: :vegas: :machine: :luck: :casino: :slot_machine:".split(),
    '🚏': ":wait: :busstop:".split(),
    '💈': ":hair: :salon: :style: :barber:".split(),
    '♨': ":bath: :warm: :relax: :hotsprings:".split(),
    '🏁': ":contest: :finishline: :rase: :gokart: :checkered_flag:".split(),
    '🎌': ":nation: :country: :border: :crossed_flags:".split(),
    '🏮': ":light: :halloween: :spooky: :izakaya_lantern:".split(),
    '🗿': ":easter: :island: :statue: :moyai:".split(),
    '🎪': ":carnival: :circus_tent:".split(),
    '🎭': ":acting: :theater: :drama: :performing_arts:".split(),
    '📍': ":location: :map: :here: :round_pushpin:".split(),
    '🚩': ":mark: :milestone: :place: :triangular_flag_on_post:".split(),
    '🔣': ":note: :ampersand: :percent: :glyphs: :characters: :symbols:".split(),
    '◀': ":left: :arrow_backward:".split(),
    '⬇': ":bottom: :arrow_down:".split(),
    '▶': ":right: :arrow_forward:".split(),
    '⬅': ":previous: :back: :arrow_left:".split(),
    '🔠': ":ABCD:".split(),
    '🔡': ":abcd:".split(),
    '🔤': ":abc:".split(),
    '↙': ":arrow_lower_left:".split(),
    '↘': ":arrow_lower_right:".split(),
    '➡': ":next: :arrow_right:".split(),
    '⬆': ":continue: :top: :arrow_up:".split(),
    '↖': ":arrow_upper_left:".split(),
    '↗': ":arrow_upper_right:".split(),
    '⏬': ":arrow_double_down:".split(),
    '⏫': ":arrow_double_up:".split(),
    '🔽': ":arrow_down_small:".split(),
    '⤵': ":arrow_heading_down:".split(),
    '⤴': ":arrow_heading_up:".split(),
    '↩': ":undo: :leftwards_arrow_with_hook:".split(),
    '↪': ":rotade: :arrow_right_hook:".split(),
    '↔': ":left_right_arrow:".split(),
    '↕': ":way: :arrow_up_down:".split(),
    '🔼': ":triangle: :forward: :arrow_up_small:".split(),
    '🔃': ":sync: :cycle: :round: :repeat: :arrows_clockwise:".split(),
    '🔄': ":arrows_counterclockwise:".split(),
    '⏪': ":fast_backward:".split(),
    '⏩': ":speed: :continue: :fast_forward:".split(),
    'ℹ': ":information_source:".split(),
    '🆗': ":OK:".split(),
    '🔀': ":shuffle: :random: :twisted_rightwards_arrows:".split(),
    '🔁': ":loop: :record: :repeat:".split(),
    '🔂': ":repeat_one:".split(),
    '🆕': ":start: :new:".split(),
    '🔝': ":TOP:".split(),
    '🆙': ":above: :high: :UP:".split(),
    '🆒': ":COOL:".split(),
    '🆓': ":FREE:".split(),
    '🆖': ":NG:".split(),
    '🎦': ":movie: :record: :film: :cinema:".split(),
    '🈁': ":here: :katakana: :destination: :koko:".split(),
    '📶': ":reception: :phone: :internet: :connection: :wifi: :bluetooth: :signal_strength:".split(),
    '🈂': ":katakana: :sa:".split(),
    '🚻': ":toilet: :refresh: :wc: :gender: :restroom:".split(),
    '🚹': ":toilet: :restroom: :wc: :gender: :mens:".split(),
    '🚺': ":toilet: :loo: :restroom: :gender: :womens:".split(),
    '🚼': ":child: :baby_symbol:".split(),
    '🚭': ":cigarette: :smell: :smoke: :no_smoking:".split(),
    '🅿': ":parking:".split(),
    '♿': ":disabled: :a11y: :accessibility: :wheelchair:".split(),
    '🚇': ":mrt: :underground: :tube: :metro:".split(),
    '🛄': ":airport: :transport: :baggage_claim:".split(),
    '🉑': ":good: :kanji: :agree: :yes:".split(),
    '🚾': ":toilet: :restroom:".split(),
    '🚰': ":liquid: :restroom: :cleaning: :faucet: :potable_water:".split(),
    '🚮': ":info: :put_litter_in_its_place:".split(),
    'Ⓜ': ":m: :subway:".split(),
    '🛂': ":custom:".split(),
    '🛅': ":travel: :left_luggage:".split(),
    '🛃': ":passport: :border:".split(),
    '🉐': ":kanji: :obtain: :get: :circle: :ideograph_advantage:".split(),
    '🆘': ":help: :emergency: :911: :sos:".split(),
    '🆔': ":id:".split(),
    '🚫': ":forbid: :limit: :denied: :disallow: :circle: :no_entry_sign:".split(),
    '🔞': ":18: :pub: :night: :minor: :circle: :underage:".split(),
    '📵': ":iphone: :mute: :circle: :no_mobile_phones:".split(),
    '🚯': ":trash: :bin: :garbage: :circle: :do_not_litter:".split(),
    '🚱': ":faucet: :tap: :circle: :non:".split(),
    '🚳': ":cyclist: :prohibited: :circle: :no_bicycles:".split(),
    '🚷': ":rules: :crossing: :walking: :circle: :no_pedestrians:".split(),
    '🚸': ":warning: :danger: :driving:".split(),
    '⛔': ":limit: :denied: :circle: :no_entry:".split(),
    '❇': ":stars: :fireworks: :sparkle:".split(),
    '✴': ":eight_pointed_black_star:".split(),
    '💟': ":heart_decoration:".split(),
    '📳': ":phone: :vibration_mode:".split(),
    '📴': ":mute: :silence: :quiet: :mobile_phone_off:".split(),
    '💹': ":yen: :chart:".split(),
    '💱': ":travel: :currency_exchange:".split(),
    '♈': ":aries:".split(),
    '♉': ":taurus:".split(),
    '♊': ":gemini:".split(),
    '♋': ":cancer:".split(),
    '♌': ":leo:".split(),
    '♍': ":virgo:".split(),
    '♎': ":libra:".split(),
    '♏': ":scorpio: :scorpius:".split(),
    '♐': ":sagittarius:".split(),
    '♑': ":capricorn:".split(),
    '♒': ":aquarius:".split(),
    '♓': ":pisces:".split(),
    '⛎': ":zodiac: :constellation: :astrology: :ophiuchus:".split(),
    '🔯': ":religion: :jewish: :hexagram: :six_pointed_star:".split(),
    '❎': ":x: :deny: :negative_squared_cross_mark:".split(),
    '🅰': ":a:".split(),
    '🅱': ":b:".split(),
    '🆎': ":ab:".split(),
    '💠': ":jewel: :gem: :crystal: :fancy: :diamond_shape_with_a_dot_inside:".split(),
    '♻': ":environment: :garbage: :trash: :recycle:".split(),
    '🔚': ":end:".split(),
    '🔙': ":return: :back:".split(),
    '🔛': ":on:".split(),
    '🔜': ":soon:".split(),
    '💲': ":payment: :currency: :heavy_dollar_sign:".split(),
    '©': ":ip: :license: :circle: :copyright:".split(),
    '®': ":circle: :registered:".split(),
    '™': ":trademark: :brand: :tm:".split(),
    '❌': ":no: :delete: :remove: :x:".split(),
    '❗': ":shocked: :surprised: :heavy_exclamation_mark:".split(),
    '‼': ":exclamation: :surprise: :bangbang:".split(),
    '⁉': ":wat: :punctuation: :surprise: :interrobang:".split(),
    '⭕': ":circle: :round: :o:".split(),
    '✖': ":heavy_multiplication_x:".split(),
    '➕': ":addition: :more: :increase: :heavy_plus_sign:".split(),
    '➖': ":subtract: :less: :heavy_minus_sign:".split(),
    '➗': ":divide: :heavy_division_sign:".split(),
    '💮': ":white_flower:".split(),
    '✔': ":nike: :heavy_check_mark:".split(),
    '☑': ":agree: :confirm: :ballot_box_with_check:".split(),
    '🔘': ":input: :old: :circle: :radio_button:".split(),
    '🔗': ":rings: :url: :link:".split(),
    '➰': ":scribble: :draw: :squiggle: :curly_loop:".split(),
    '〰': ":draw: :line: :moustache: :mustache: :squiggle: :scribble: :wavy_dash:".split(),
    '〽': ":part_alternation_mark:".split(),
    '🔱': ":spear: :trident:".split(),
    '▪': ":black_small_square:".split(),
    '▫': ":white_small_square:".split(),
    '◾': ":black_medium_small_square:".split(),
    '◽': ":white_medium_small_square:".split(),
    '◼': ":black_medium_square:".split(),
    '◻': ":white_medium_square:".split(),
    '⬛': ":black_large_square:".split(),
    '⬜': ":white_large_square:".split(),
    '✅': ":white_check_mark:".split(),
    '🔲': ":black_square_button:".split(),
    '🔳': ":white_square_button:".split(),
    '⚫': ":black_circle:".split(),
    '⚪': ":white_circle:".split(),
    '🔴': ":red_circle:".split(),
    '🔵': ":large_blue_circle:".split(),
    '🔷': ":large_blue_diamond:".split(),
    '🔶': ":large_orange_diamond:".split(),
    '🔹': ":small_blue_diamond:".split(),
    '🔸': ":small_orange_diamond:".split(),
    '🔺': ":small_red_triangle:".split(),
    '🔻': ":small_red_triangle_down:".split(),
}


def generate_testfile(filename="test.txt"):
    with open(filename, "w") as f:
        for i, emoji in enumerate(EMOJI.keys()):
            f.write("\n\nFor emoji #{} '{}' :".format(i, emoji))
            for shorttext in EMOJI[emoji]:
                if shorttext[0] == shorttext[-1] == ':':
                    shorttext_only = ': ' + shorttext.replace(':', '') + ' :'
                else:
                    shorttext_only = shorttext
                f.write("\n  - '{}' should convert to '{}' : '{}'".format(shorttext_only, emoji, shorttext))

def main():
    generate_testfile()

if __name__ == '__main__':
    main()