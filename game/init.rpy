# Вы можете расположить сценарий своей игры в этом файле.
define config.end_splash_transition = Dissolve(1.0)
# Определение персонажей игры.
define m = Character("{b}Мама{/b}", color="313447")
define e = Character("{b}Егор{/b}", color="1B9753")

# Backgrounds
image room = "bg/room_in_day.jpg"
image school = "bg/school.jpg"
# image black = "bg/black.jpg"
image episode_1 = "bg/episode_1.jpg"
image kitchen = "bg/kitchen.jpg"
image food = "bg/food.jpg"
image koridor = "bg/korifor.jpg"
image street = "bg/street.jpg"
image phone = "bg/phone.jpg"
image streetDog = "bg/street_with_dog.jpg"
image episode_end = "bg/episode_end.jpg"

# intro
image black = "intro/black.png"
image first = "intro/first.png"
image center_text = "intro/center_text.png"
image loader0 = "intro/loader (0).png"
image loader1 = "intro/loader (1).png"
image loader2 = "intro/loader (2).png"
image loader3 = "intro/loader (3).png"
image loader4 = "intro/loader (4).png"
image loader5 = "intro/loader (5).png"
image loader6 = "intro/loader (6).png"
image loader7 = "intro/loader (7).png"
image loader8 = "intro/loader (8).png"
image loader9 = "intro/loader (9).png"
image loader10 = "intro/loader (10).png"
image loader11 = "intro/loader (11).png"
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Переменные:
$ score_ecaterina = 0
$ score_blondinka = 0
$ score_friend = 0
$ bad_condition = 0
$ good_condition = 0

# Спрайты Rin
image Rin = "Rin/Rin_Casual_OpenSmile_Blush.png"
image RinSmile = "Rin/Rin_Casual_Frown_EyesClosed.png"
image RinDefault = "Rin/Rin_Casual_Smile.png"
image RinBlush = "Rin/Rin_Casual_Smile_Blush.png"

label splashscreen:
    scene black
    pause(0.5)
    scene first with fade
    pause(4)
    scene black
    show center_text:
        xalign 0.5
        yalign 0.5
    with dissolve
    pause
    show loader0:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader1:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader2:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader3:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader4:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader5:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader6:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader7:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader8:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader9:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader10:
        xalign 0.95
        yalign 0.95
    pause(0.5)
    show loader11:
        xalign 0.95
        yalign 0.95
    pause(2)
