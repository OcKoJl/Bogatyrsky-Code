define old_font = "fonts/ofont.ru_Kramola.ttf"

define mc = Character(name="Добрыня")
define wz = Character(name="Злой колдун")

transform left:
    xalign 0.2

transform right:
    xalign 0.8

transform spin:
    rotate 0
    block:
        linear 2 rotate 360
        linear 0.0 rotate -360
        repeat

transform scale:
    on show:
        xsize 0
        fit "contain"
        linear 0.5 xsize 1000
    
    on hide:
        fit "contain"
        linear 0.7 xsize 0
    

init:
    image white = Solid("#FFFFFF")

    image rain:
        "rain/rain1.png"
        0.2
        "rain/rain3.png"
        0.2
        "rain/rain2.png"
        0.2
        repeat

label start:
    window hide

    scene bg book
    with dissolve

    # TODO звук: письмо на бумаге
    centered"{cps=20}{font=[old_font]}{size=120}{color=#FF0000}В{/color}{/size}{size=80}{color=#191919} далеком XIII веке жил могучий русский богатырь по имени Добрыня. Однажды, сражаясь со злым колдуном, он оказывается втянутым в магический портал, который переносит его прямо в XXI век. Теперь Добрыне предстоит адаптироваться к современному миру, где вместо мечей правят компьютеры, а вместо драконов - алгоритмы. Он решает найти свое новое призвание и становится тестировщиком программного обеспечения.{/size}{/color}{/font}{/cps}"

    jump scene1

label scene1:
    scene white
    # TODO звук: молния

    pause 0.5

    scene bg forest_with_castle
    show rain
    show dobrinya
    with dissolve

    mc "Злой колдун! "
    extend"Я пришел положить конец твоим козням! "

    show white
    $ renpy.pause(0.5)
    hide white with dissolve

    show dobrinya at left
    show wizard at right
    with moveinright

    wz "Ха-ха-ха! "
    extend"Ты думаешь, что сможешь победить меня? "
    extend"Я отправлю тебя туда, где твой меч будет бесполезен! "

    show portal at scale, spin behind dobrinya:
        xpos 0.25
        ypos 0.5
        anchor (0.5, 0.5)
    
    pause 0.7

    hide portal at scale, spin
    hide wizard with easeoutright
    hide dobrinya with Dissolve(0.2)

    jump scene2

label scene2:
    scene black
    show portal at spin, truecenter
    with dissolve
    pause

    show dobrinya at center
    with dissolve

    mc "Что за чертовщина?!"

    scene white with Dissolve(3)

    # TODO звук: удар
    scene black with vpunch

    pause

    jump scene3

label scene3:
    centered"{cps=2}{size=200}...{/size}{/cps}"

    # TODO: Эффект открытия глаз

    scene bg crouded_street
    with dissolve

    "Добрыня лежит на асфальте, оглядывается вокруг."
    "Пешеход" "Эй, мужик, ты как тут оказался?"

    "Добрыня поднимается, осматривается."
    mc "Где я? Что за странные строения? Куда подевались леса и поля?"

    jump scene4

label scene4:
    scene bg bus_stop
    with dissolve

    "Добрыня, гуляя по городу, подходит к автобусной остановке"

    "Оглядевшись, он замечает рекламный щит"
    
    # TODO: что-то с рекламным щитом

    # Как появилась эта ситуация хз
    "Мужчина" "Вот, смотри, тут все есть: интернет, карты, музыка..."

    mc "Какое волшебство!" # Про артефакт никто не говрил
    
    pause
