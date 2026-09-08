import streamlit as st

from modules.barista import babyccino_price, format_menu, items_with_milk, items_without_milk, items_without_milk_cold

st.set_page_config(page_title="Robot Barista", page_icon="☕", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Poppins:wght@400;500;600;700&display=swap');

:root {
    --cream: #faf3e8;
    --coffee: #4b3621;
    --coffee-light: #6f4e37;
    --terracotta: #c96f4a;
    --gold: #cfa15c;
}

#MainMenu, footer, header { visibility: hidden; }

[data-testid="stMainBlockContainer"] { padding-top: 3rem; }

.stApp {
    background: var(--cream);
    background-image:
        radial-gradient(circle at 15% 10%, rgba(207,161,92,0.15), transparent 40%),
        radial-gradient(circle at 85% 90%, rgba(201,111,74,0.12), transparent 40%);
    z-index: 0;
}

html, body, .stMarkdown, .stMarkdown p, label, .stApp span {
    font-family: 'Poppins', sans-serif !important;
    font-size: 16px !important;
    color: var(--coffee);
}

.neon-title {
    font-family: 'Fraunces', serif !important;
    font-weight: 700 !important;
    font-size: 40px !important;
    text-align: center;
    color: var(--coffee);
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    color: var(--coffee-light) !important;
    font-style: italic;
    margin-bottom: 24px;
}

.card {
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(75,54,33,0.12);
    border: 1px solid rgba(75,54,33,0.08);
    padding: 24px 28px 16px;
    margin-bottom: 20px;
}

.line { color: var(--coffee); margin-bottom: 6px; }
.line.hi { color: var(--terracotta) !important; font-weight: 600; }

.menu-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid rgba(75,54,33,0.08); }
.menu-row span:last-child { color: var(--coffee-light); font-weight: 700; }

button[data-testid^="stBaseButton"] {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    color: #fff !important;
    background: var(--terracotta) !important;
    border: none !important;
    border-radius: 24px !important;
    box-shadow: 0 4px 10px rgba(201,111,74,0.35);
    width: 100%;
}
button[data-testid^="stBaseButton"]:hover { background: var(--coffee-light) !important; }

[data-testid="stAlert"] {
    background: #fff !important;
    border: 1.5px solid #c94a4a !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 12px rgba(201,74,74,0.15) !important;
}
[data-testid="stAlert"] p {
    color: #c94a4a !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 15px !important;
}

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
    background: #fff !important;
    border: 1.5px solid rgba(75,54,33,0.2) !important;
    border-radius: 8px;
    box-shadow: none;
}
[data-testid="stTextInputRootElement"] input, [data-testid="stNumberInputContainer"] input {
    background: transparent !important;
    color: var(--coffee) !important;
    border: none !important;
    font-family: 'Poppins', sans-serif !important;
    font-size: 16px !important;
}

[data-testid="stForm"] { border: none; padding: 0; }

.bean {
    position: fixed;
    width: 26px;
    height: 38px;
    background: var(--coffee-light);
    border-radius: 50%;
    opacity: 0.16;
    pointer-events: none;
    z-index: -1;
}
.bean::before {
    content: '';
    position: absolute;
    top: 6%;
    left: 50%;
    width: 3px;
    height: 88%;
    background: var(--cream);
    border-radius: 3px;
    transform: translateX(-50%) rotate(8deg);
}

.cup {
    position: fixed;
    width: 36px;
    height: 30px;
    background: var(--terracotta);
    border-radius: 0 0 12px 12px;
    opacity: 0.16;
    pointer-events: none;
    z-index: -1;
}
.cup::before {
    content: '';
    position: absolute;
    right: -11px;
    top: 5px;
    width: 12px;
    height: 15px;
    border: 4px solid var(--terracotta);
    border-left: none;
    border-radius: 0 9px 9px 0;
}
.cup .steam {
    position: absolute;
    top: -14px;
    width: 3px;
    height: 12px;
    background: var(--coffee-light);
    border-radius: 3px;
    opacity: 0.5;
}
.cup .steam.one { left: 8px; transform: rotate(-12deg); }
.cup .steam.two { left: 18px; transform: rotate(10deg); }
</style>
<div class="bean" style="top: 8%; left: 6%; transform: rotate(-25deg); width: 34px; height: 48px;"></div>
<div class="bean" style="top: 22%; left: 12%; transform: rotate(40deg);"></div>
<div class="bean" style="top: 68%; left: 8%; transform: rotate(15deg); width: 30px; height: 42px;"></div>
<div class="bean" style="bottom: 6%; left: 20%; transform: rotate(-10deg);"></div>
<div class="bean" style="top: 10%; right: 8%; transform: rotate(20deg); width: 32px; height: 46px;"></div>
<div class="bean" style="top: 60%; right: 6%; transform: rotate(-30deg);"></div>
<div class="bean" style="bottom: 10%; right: 18%; transform: rotate(35deg); width: 28px; height: 40px;"></div>
<div class="cup" style="top: 14%; left: 22%;"><div class="steam one"></div><div class="steam two"></div></div>
<div class="cup" style="bottom: 16%; right: 10%; width: 44px; height: 36px;"><div class="steam one"></div><div class="steam two"></div></div>
<div class="cup" style="top: 48%; left: 4%; width: 28px; height: 24px;"><div class="steam one"></div></div>
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
    st.markdown('<div class="subtitle">welcome to our coffee shop</div>', unsafe_allow_html=True)

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
