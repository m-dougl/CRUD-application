import streamlit as st
from services.crud import CRUD


def main():
    st.title("Order list")
    dataframe_expander = st.expander(label="Orders in progress", expanded=True)
    df = CRUD().read()
    dataframe_expander.dataframe(df, hide_index=True, use_container_width=True)

    cols = st.columns((2.5, 5), gap="medium")
    with cols[0]:
        st.write("❌ Cancel your order ")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        cancel_button = st.button("Cancel")

        if cancel_button:
            if all([first_name.capitalize(), last_name.capitalize()]):
                CRUD().delete(first_name=first_name, last_name=last_name)
                st.success("✅️ Your order has been cancelled")
            else:
                st.error("⚠️ Please fill in all the required fields")
            st.experimental_rerun()


if __name__ == "__main__":
    st.set_page_config(page_title="Foods Delivery", layout="wide")
    main()
