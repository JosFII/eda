import streamlit as st
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: 100vw 168vh;
    background-position: center;  
    background-repeat: no-repeat;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('back_card_yugioh_hd_by_yugiohoricabr_dbwk3sn_fullv_by_fly00speed_desvyys.jpg')

st.title("The Invoked Archetype")

st.header("Background")

st.text("Invoked is a fusion archetype that was introduced in The set Fusion Enforcers. " 
        "It consists of 6 main deck cards, 2 monsters and 4 spells and traps, and 9 extra deck monsters, 8 fusions and 1 link. "
        "Its plays revolves around the card 'Aleister the Invoker' which is the archetypes starter and is required material for most of its fusion monsters. "
        )

st.header("The Cards")
st.text("For now, i'm only going to talk about some of the important and/or note worthy cards.")
st.subheader("Main Deck")
st.image("https://ms.yugipedia.com//thumb/1/13/AleistertheInvoker-MAGO-EN-PGR-1E.png/411px-AleistertheInvoker-MAGO-EN-PGR-1E.png")
st.text("Aleister the Invoker in the main playmaker of the archetype, and one of two main deck monsters of the achetype. "
        "The second effect to add 'Invocation' to hand on normal summon is the main way you will start your plays. "
        "The effect to increase the stats of your fusion monsters is good when you need a key monster to survive battle, however the cost of dicard the card might hurt the reccursiveness of the combo")

st.image("https://ms.yugipedia.com//thumb/c/ce/Invocation-MGED-EN-PGR-1E.png/409px-Invocation-MGED-EN-PGR-1E.png")
st.text("This is the main way to get to the invoked fusions. The fact you can use both GYs to fuse Invoked monster means you can use your opponts resource, "
        "However when it's really bad when used to fuse non Invoked monsters since it can only fuse cards from hand. "
        "The GY effect of returning Aliester to hand and returning this card to the deck mean you can fuse an invoked monster every turn as long as the aliester stays in hand.")

st.image("https://ms.yugipedia.com//thumb/d/d6/MagicalMeltdown-MAGO-EN-R-1E.png/412px-MagicalMeltdown-MAGO-EN-R-1E.png")
st.text("Magical Meltdown is a field spell that adds Aliester from deck, so it can be used as a starter, or to bait interaction if you have an Aliester in hand already. "
        "The continous effect of this card rarely comes up when making Invoked monsters, however if you play with with another archetype it may become more relevant.")

st.subheader("Extra Deck")
st.image("https://ms.yugipedia.com//thumb/0/07/InvokedMechaba-MGED-EN-PGR-1E.png/410px-InvokedMechaba-MGED-EN-PGR-1E.png")
st.text("Mechaba is the main Fusion that will be made, it requires Aleister and a light monster. "
        "This card can negate the effects of any card, however you are required to discard the same card type (Monster, spell, or trap), so keep that in mind. "
        "Also, since this card isn't a hard OPT, if you can multiple Mechabas in your field you can use it once per copy.")

st.image("https://ms.yugipedia.com//thumb/5/57/InvokedPurgatrio-BLAR-EN-UR-1E.png/419px-InvokedPurgatrio-BLAR-EN-UR-1E.png")
st.text("Purgatrio is one of the finishers AKA OTK tools, it requires Aleister and a fire monster. "
        "It is pretty commonly made because of how of prominent the fire handtrap 'Ash blossom & joyous spring' is played, especially in the ocg format. "
        "This cards effects help this card almost gurantee an OTK, The atk increase means this card deals battle damage and helps it get over large monsters, the peircing damage means it can still deal damage when attacking a monster in defense position, "
        "and it can attack all monster your opponent controls so in can clear their monster while dealing alot of damage.")

st.image('https://ms.yugipedia.com//thumb/d/d2/InvokedAugoeides-MP21-EN-PScR-1E.png/407px-InvokedAugoeides-MP21-EN-PScR-1E.png')
st.text("Augoeides is the second finisher of the archetype, requiring Aleister and a Fusion monster. "
        "This card destroys a monster when its summoned or when your opponents special summons a monster, so this card can get rid of a problematic monster your opponent have, "
        "and if fail to finish your opponent, this can be used as an interuption. "
        "It can also increase it's attack by banishing a fusion monster from your GY.")

st.image("https://ms.yugipedia.com//thumb/b/ba/InvokedCaliga-BLAR-EN-UR-1E.png/417px-InvokedCaliga-BLAR-EN-UR-1E.png")
st.text("Caliga is a flood gate, requiring Aleister and a dark monster. "
        "Its effect of only letting each player activate 1 monster effect is quite devastating, because most deck needs to use more than one monster effect to do their basic plays, "
        "and the effect of only one monster can attack can help it survive the battle phase, since this card has very low stats." 
        "Also if this card is attacked, you can use aleister in your hand, as your one monster effect, to increase its stats to survive the battle.")

st.image('https://ms.yugipedia.com//thumb/7/7a/InvokedRaidjin-BLAR-EN-UR-1E.png/419px-InvokedRaidjin-BLAR-EN-UR-1E.png')
st.text("Raidjin is a good fusion to go into, requiring Aleister and a wind monster. "
        "It can, at quick effect speed, turn a monster face down, which is a powerfull disruption, since face down monsters can't be used as synchro, XYZ or link material. "
        "However this card can be quite troublesome to make since the wind attribute is yhe least supported archetype and there isn't a lot of good generic wind monsters.")

st.subheader("Non-archetypal cards")
st.text("Here I will talk about non-archetypal cards that are good in Invoked decks")

st.image("https://ms.yugipedia.com//thumb/1/11/ArtemistheMagistusMoonMaiden-RA01-EN-SR-1E.png/407px-ArtemistheMagistusMoonMaiden-RA01-EN-SR-1E.png")
st.write("Artemis is a link 1 light monster that can be summoned using aleister, so that you have a guaranteed access to Mechaba")

st.image("https://ms.yugipedia.com//thumb/b/b3/SalamangreatAlmiraj-BLC1-EN-C-1E.png/409px-SalamangreatAlmiraj-BLC1-EN-C-1E.png")
st.image("https://ms.yugipedia.com//thumb/e/e5/SecureGardna-BLAR-EN-UR-1E.png/420px-SecureGardna-BLAR-EN-UR-1E.png")
st.write("Almiraj and Secure gardna are usually replacements for Artemis, since it also gives access to a guaranteed purgatrio on the next turn, however it also takes 2 extra deck slots instead of 1, so some decks still prfer to run Artemis.")

st.header("Deck Construction")
st.text("The main deck and extra deck requirement for Invoked is quite light, so It can also be splashed into other decks as an engine. "
        "For the main deck you play 3x Aleister the Invoker, 3x Magical Meltdown and 2x Invocation, "
        "as for the Extra Deck 1x or 2x Invoked Mechaba, 1x Invoked Purgatorio, 1x Invoked Augoeides, "
        "1x Artemis, the Magistus Moon Maiden or 1x each of salamangreat almiraj and secure gardna if you have the space. "
        "as for the rest of the Invoked fusions, put in ones that suit your decks atribute or suit them to the current META.")

st.header("some video Guides")

Vid1 = "https://www.youtube.com/watch?v=OuuqnA8zpXs"
st.components.v1.html(
    f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{Vid1.split('=')[-1]}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, 
    height=315
)

Vid2 = "https://www.youtube.com/watch?v=Wqz1s-eEGAI"
st.components.v1.html(
    f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{Vid2.split('=')[-1]}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, 
    height=315
)

OOO = "https://www.youtube.com/watch?v=M6vMRXD1dIU"
st.components.v1.html(
    f"""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/{OOO.split('=')[-1]}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, 
    height=315
)

