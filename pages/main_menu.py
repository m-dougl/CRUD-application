import streamlit as st
from models.foods import RequestModel
from services.crud import CRUD
from datetime import datetime


def main():
    st.set_page_config(page_title="Foods Delivery")
    st.title("Foods Delivery")
    CRUD().create()

    # Input data forms
    with st.form("request_forms"):
        st.write("Inform your request")
        # User data
        first_name = st.text_input(label="First name")
        last_name = st.text_input(label="Last name")
        address = st.text_input(label="Address")
        date = datetime.now()

        # Foods acquisition
        foods_area = st.expander(label="Foods List", expanded=True)

        cols = foods_area.columns((7.5, 2))
        with cols[0]:
            burguer_choice = st.selectbox(
                label="Burgers",
                options=[
                    "Hamburger",
                    "Turkey burger",
                    "Portobello mushroom burger",
                    "Elk burger",
                    "Veggie burger",
                    "Wild salmon burger",
                ],
            )

            soup_choice = st.selectbox(
                label="Soups",
                options=[
                    "Chicken Noodle Soup",
                    "Italian Wedding Soup",
                    "Minestrone Soup",
                    "Lentil Soup",
                    "Tomato Soup",
                    "French Onion Soup",
                ],
            )

        with cols[1]:
            burguer_quantity = st.number_input(
                label="Quantity of Burguer", min_value=0, step=1
            )
            soup_quantity = st.number_input(
                label="Quantity of Soup", min_value=0, step=1
            )

        send_button = st.form_submit_button(label="Send")
        if send_button:
            request = RequestModel(
                first_name,
                last_name,
                address,
                date,
                burguer_choice,
                burguer_quantity,
                soup_choice,
                soup_quantity,
            )
            if all([first_name, last_name, address]):
                CRUD().insert(request)
            else:
                st.error("Please fill in all the required fields")


if __name__ == "__main__":
    main()
