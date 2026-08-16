import streamlit as st

from modules.barista import babyccino_price, format_menu, items_with_milk, items_without_milk, items_without_milk_cold

st.set_page_config(page_title="Robot Barista", page_icon="☕", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

:root {
    --pink: #ff2fb0;
    --violet: #a259ff;
    --blue: #00e5ff;
}

#MainMenu, footer, header { visibility: hidden; }

[data-testid="stMainBlockContainer"] { padding-top: 6rem; }

.stApp {
    background: #05010f;
    background-image:
        radial-gradient(ellipse at 50% 0%, rgba(162,89,255,0.25), transparent 60%),
        radial-gradient(ellipse at 50% 100%, rgba(255,47,176,0.15), transparent 60%);
    z-index: 0;
}

html, body, .stMarkdown, .stMarkdown p, label, .stApp span {
    font-family: 'VT323', monospace !important;
    font-size: 20px !important;
    color: #cfc9ff;
}

.neon-title {
    font-family: 'Press Start 2P', monospace;
    font-size: 30px;
    text-align: center;
    letter-spacing: 2px;
    background: linear-gradient(90deg, var(--blue), var(--violet), var(--pink));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    text-shadow: 0 0 20px rgba(162,89,255,0.6), 0 0 40px rgba(255,47,176,0.35);
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    color: var(--blue) !important;
    text-shadow: 0 0 8px var(--blue);
    letter-spacing: 3px;
    margin-bottom: 24px;
}

@property --angle {
    syntax: '<angle>';
    initial-value: 0deg;
    inherits: false;
}

.card {
    position: relative;
    border: 2px solid transparent;
    border-radius: 4px;
    background:
        linear-gradient(rgba(10,4,26,0.85), rgba(10,4,26,0.85)) padding-box,
        conic-gradient(from var(--angle), var(--blue), var(--violet), var(--pink), var(--blue)) border-box;
    box-shadow: 0 0 12px rgba(162,89,255,0.7), inset 0 0 20px rgba(162,89,255,0.15);
    padding: 20px 24px;
    margin-bottom: 20px;
}

.line { color: #cfc9ff; margin-bottom: 6px; }
.line.hi { color: var(--pink) !important; text-shadow: 0 0 6px var(--pink); }

.menu-row { display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px dashed rgba(0,229,255,0.25); }
.menu-row span:last-child { color: var(--blue); text-shadow: 0 0 6px var(--blue); }

button[data-testid^="stBaseButton"] {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 12px !important;
    color: var(--pink) !important;
    background: transparent !important;
    border: 2px solid var(--pink) !important;
    border-radius: 4px !important;
    text-shadow: 0 0 6px var(--pink);
    box-shadow: 0 0 10px rgba(255,47,176,0.5);
    width: 100%;
}
button[data-testid^="stBaseButton"]:hover { background: rgba(255,255,255,0.08) !important; border-color: var(--blue) !important; color: var(--blue) !important; }

[data-testid="stAlert"] {
    background: rgba(20,2,10,0.85) !important;
    border: 2px solid #ff3860 !important;
    border-radius: 4px !important;
    box-shadow: 0 0 10px rgba(255,56,96,0.6), inset 0 0 15px rgba(255,56,96,0.12) !important;
}
[data-testid="stAlert"] p {
    color: #ff3860 !important;
    text-shadow: 0 0 6px #ff3860;
    font-family: 'VT323', monospace !important;
    font-size: 20px !important;
}
[data-testid="stAlert"] svg { display: none; }

[data-testid="stHorizontalBlock"] {
    display: flex !important;
    justify-content: center !important;
    gap: 24px !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stColumn"],
[data-testid="stHorizontalBlock"] [data-testid="stButton"] {
    width: fit-content !important;
    flex: none !important;
}
[data-testid="stHorizontalBlock"] button[data-testid^="stBaseButton"] {
    width: auto !important;
    padding-left: 32px;
    padding-right: 32px;
}

[data-testid="stElementContainer"]:has([data-testid="stButton"]),
[data-testid="stElementContainer"]:has([data-testid="stFormSubmitButton"]) {
    display: flex;
    justify-content: center;
    width: 100%;
}
[data-testid="stButton"], [data-testid="stFormSubmitButton"] {
    width: fit-content !important;
}
[data-testid="stButton"] button, [data-testid="stFormSubmitButton"] button {
    width: auto !important;
    padding-left: 32px;
    padding-right: 32px;
}

[data-testid="stTextInputRootElement"], [data-testid="stNumberInputContainer"] {
    background: rgba(0,0,0,0.4) !important;
    border: 2px solid var(--blue) !important;
    box-shadow: 0 0 8px rgba(0,229,255,0.4);
}
[data-testid="stTextInputRootElement"] input, [data-testid="stNumberInputContainer"] input {
    background: transparent !important;
    color: var(--blue) !important;
    border: none !important;
    font-family: 'VT323', monospace !important;
    font-size: 20px !important;
}

[data-testid="stForm"] { border: none; padding: 0; }

.sun {
    position: fixed;
    top: 20px;
    left: 20px;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: linear-gradient(180deg, var(--pink), var(--violet));
    box-shadow: 0 0 60px 15px rgba(255,47,176,0.5);
    opacity: 0.55;
    pointer-events: none;
    z-index: -2;
}

.moon {
    position: fixed;
    bottom: 170px;
    right: 150px;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: linear-gradient(180deg, var(--blue), var(--violet));
    box-shadow: 0 0 40px 10px rgba(0,229,255,0.4);
    opacity: 0.45;
    pointer-events: none;
    z-index: -2;
}

.streak {
    position: fixed;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--blue), transparent);
    opacity: 0.4;
    pointer-events: none;
    z-index: -2;
}
.streak.one {
    top: 18%;
    left: -5%;
    width: 260px;
    transform: rotate(-18deg);
}
.streak.two {
    bottom: 22%;
    right: -8%;
    width: 340px;
    background: linear-gradient(90deg, transparent, var(--pink), transparent);
    transform: rotate(12deg);
}
.streak.three {
    top: 42%;
    right: 4%;
    width: 140px;
    background: linear-gradient(90deg, transparent, var(--violet), transparent);
    transform: rotate(-8deg);
}

.grid-floor {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 180px;
    background-image:
        linear-gradient(rgba(162,89,255,0.4) 1px, transparent 1px),
        linear-gradient(90deg, rgba(162,89,255,0.4) 1px, transparent 1px);
    background-size: 40px 40px;
    -webkit-mask-image: linear-gradient(to top, black, transparent);
    mask-image: linear-gradient(to top, black, transparent);
    transform: perspective(200px) rotateX(55deg);
    transform-origin: bottom;
    opacity: 0.5;
    pointer-events: none;
    z-index: -1;
    animation: grid-scroll 1.5s linear infinite;
}
@keyframes grid-scroll {
    from { background-position: 0 0; }
    to { background-position: 0 40px; }
}

.starfield {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -3;
    background-image:
        radial-gradient(1.5px 1.5px at 10% 20%, #fff, transparent),
        radial-gradient(1.5px 1.5px at 80% 10%, #fff, transparent),
        radial-gradient(1px 1px at 30% 80%, #fff, transparent),
        radial-gradient(1px 1px at 70% 65%, #fff, transparent),
        radial-gradient(1.5px 1.5px at 90% 40%, #fff, transparent),
        radial-gradient(1px 1px at 15% 55%, #fff, transparent),
        radial-gradient(1px 1px at 50% 15%, #fff, transparent),
        radial-gradient(1.5px 1.5px at 60% 85%, #fff, transparent),
        radial-gradient(1px 1px at 25% 40%, #fff, transparent),
        radial-gradient(1px 1px at 85% 75%, #fff, transparent);
    animation: twinkle 4s ease-in-out infinite alternate;
}
@keyframes twinkle {
    0% { opacity: 0.25; }
    100% { opacity: 0.75; }
}

.scanlines {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 999;
    mix-blend-mode: overlay;
    background: repeating-linear-gradient(
        to bottom,
        rgba(255,255,255,0.035) 0px,
        rgba(255,255,255,0.035) 1px,
        transparent 1px,
        transparent 3px
    );
}

.neon-title { animation: title-pulse 2.5s ease-in-out infinite; }
@keyframes title-pulse {
    0%, 100% { text-shadow: 0 0 20px rgba(162,89,255,0.6), 0 0 40px rgba(255,47,176,0.35); }
    50% { text-shadow: 0 0 30px rgba(162,89,255,0.9), 0 0 60px rgba(255,47,176,0.6), 0 0 80px rgba(0,229,255,0.3); }
}

.cursor { animation: blink 1s step-end infinite; }
@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}

.tower {
    position: fixed;
    top: 0;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    animation: tower-pulse 3s ease-in-out infinite;
}
.tower.left {
    left: 0;
    width: 4px;
    background: linear-gradient(to bottom, transparent, var(--pink) 15%, var(--violet) 45%, transparent 75%);
}
.tower.right {
    right: 0;
    width: 9px;
    background: linear-gradient(to bottom, transparent 10%, var(--blue) 40%, var(--violet) 65%, var(--pink) 90%, transparent);
    animation-delay: 1.5s;
}
@keyframes tower-pulse {
    0%, 100% { opacity: 0.2; }
    50% { opacity: 0.6; }
}

</style>
<div class="starfield"></div>
<div class="scanlines"></div>
<div class="tower left"></div>
<div class="tower right"></div>
<div class="moon"></div>
<div class="streak one"></div>
<div class="streak two"></div>
<div class="streak three"></div>
""", unsafe_allow_html=True)


def reset():
    st.session_state.stage = 'welcome'
    st.session_state.name = ''
    st.session_state.order = ''
    st.session_state.price = 0.0
    st.session_state.quantity = 1
    st.session_state.msg = ''


if 'stage' not in st.session_state:
    reset()


def line(text, highlight=False):
    css_class = 'line hi' if highlight else 'line'
    st.markdown(f'<div class="{css_class}">{text}</div>', unsafe_allow_html=True)


def go(stage, msg=''):
    st.session_state.stage = stage
    st.session_state.msg = msg
    st.rerun()


st.markdown('<h1 class="neon-title">ROBOT BARISTA</h1>', unsafe_allow_html=True)
if st.session_state.stage == 'welcome':
    st.markdown('<div class="subtitle">&gt; welcome to our coffee shop<span class="cursor">_</span></div>', unsafe_allow_html=True)

if st.session_state.msg:
    line(st.session_state.msg, highlight=True)
    st.session_state.msg = ''

stage = st.session_state.stage
name = st.session_state.name

if stage == 'welcome':
    menu_rows = ''.join(
        f'<div class="menu-row"><span>{item.capitalize()}</span><span>{price} €</span></div>'
        for item, price in {**items_without_milk, **items_without_milk_cold, **items_with_milk}.items()
    )
    st.markdown(
        f'<div class="card"><div class="line hi" style="font-size:22px; margin-bottom:12px;">What would you like?</div>{menu_rows}</div>',
        unsafe_allow_html=True,
    )
    if st.button('Enter', key='welcome_enter'):
        go('name')

elif stage == 'name':
    with st.form('name_form', clear_on_submit=True):
        entered_name = st.text_input('What is your name?')
        submitted = st.form_submit_button('Enter')
    if submitted:
        st.session_state.name = entered_name.strip() if entered_name.strip() else 'Honey'
        if st.session_state.name.lower() == 'david':
            go('david_egg')
        else:
            go('age')

elif stage == 'david_egg':
    line('David? You started drinking coffee?', highlight=True)
    col1, col2 = st.columns(2)
    if col1.button('Yes', key='david_yes'):
        st.session_state.name = 'David'
        go('order', 'Wait, really? Someone alert the press.')
    if col2.button('No', key='david_no'):
        st.session_state.name = 'Ester'
        go('order', 'Oh, it is for Ester! Thank you!')

elif stage == 'age':
    with st.form('age_form'):
        age = st.number_input(f'What is your age, {name}?', min_value=0, step=1, format='%d')
        submitted = st.form_submit_button('Enter')
    if submitted:
        if age <= 0:
            st.error('\\> The value is not correct, only positive numbers are allowed.')
        elif age < 16:
            go('babyccino')
        elif name.lower() in ('ben', 'pat'):
            go('evil_yesno')
        else:
            go('order')

elif stage == 'babyccino':
    line(f'We are sorry, {name}, we cannot offer you caffeinated drinks. Would you like to have a babyccino?', highlight=True)
    col1, col2 = st.columns(2)
    if col1.button('Yes', key='baby_yes'):
        st.session_state.order = 'babyccino'
        st.session_state.price = babyccino_price
        st.session_state.quantity = 1
        go('done')
    if col2.button('No', key='baby_no'):
        go('name', 'Okay then. Come back when you are older!<br><br>Next please!')

elif stage == 'evil_yesno':
    line('Are you evil?', highlight=True)
    col1, col2 = st.columns(2)
    if col1.button('Yes', key='evil_yes'):
        go('good_deeds')
    if col2.button('No', key='evil_no'):
        go('order', 'Oh, come on in!')

elif stage == 'good_deeds':
    with st.form('deeds_form'):
        deeds = st.number_input('How many good deeds have you done today?', min_value=0, step=1, format='%d')
        submitted = st.form_submit_button('Enter')
    if submitted:
        if deeds >= 4:
            go('order', 'All right, you can have a coffee.')
        else:
            go('name', 'No coffee for you!')

elif stage == 'order':
    menu_rows = ''.join(
        f'<div class="menu-row"><span>{item.capitalize()}</span><span>{price} €</span></div>'
        for item, price in {**items_without_milk, **items_without_milk_cold, **items_with_milk}.items()
    )
    st.markdown(f'<div class="card">{menu_rows}</div>', unsafe_allow_html=True)
    with st.form('order_form', clear_on_submit=True):
        order = st.text_input('What would you like?')
        submitted = st.form_submit_button('Enter')
    if submitted:
        order = order.strip().lower()
        if order in items_without_milk:
            st.session_state.order = order
            st.session_state.price = items_without_milk[order]
            go('milk')
        elif order in items_without_milk_cold:
            st.session_state.order = order
            st.session_state.price = items_without_milk_cold[order]
            go('milk')
        elif order in items_with_milk:
            st.session_state.order = order
            st.session_state.price = items_with_milk[order]
            go('quantity')
        else:
            go('name', 'Sorry, we do not have that here.<br><br>Next please!')

elif stage == 'milk':
    line('Do you wish to add oat milk?', highlight=True)
    col1, col2 = st.columns(2)
    if col1.button('Yes', key='milk_yes'):
        st.session_state.price += 0.25
        go('quantity')
    if col2.button('No', key='milk_no'):
        go('quantity')

elif stage == 'quantity':
    with st.form('qty_form'):
        qty = st.number_input('How many coffees would you like?', min_value=0, step=1, format='%d')
        submitted = st.form_submit_button('Enter')
    if submitted:
        if qty <= 0:
            st.error('\\> The value is not correct, only positive numbers are allowed.')
        else:
            st.session_state.quantity = qty
            go('done')

elif stage == 'done':
    order = st.session_state.order
    quantity = st.session_state.quantity
    total = st.session_state.price * quantity
    plural = 's' if quantity != 1 else ''
    line(f'The price is {total} €.')
    line(f'We will have your {order}{plural} ready in a minute.', highlight=True)
    if order not in items_without_milk_cold:
        line('Be careful, the drink is hot.')
    line('Next please!', highlight=True)
    if st.button('Next customer'):
        reset()
        st.rerun()

st.markdown('<div class="sun"></div><div class="grid-floor"></div>', unsafe_allow_html=True)
