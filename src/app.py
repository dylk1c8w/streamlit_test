import datetime
import streamlit as st
from lib.m0 import function_0
from lib.m1 import function_1


def main():
    st.title("テスト用")
    st.write(datetime.datetime.now())
    st.write(function_0())
    st.write(function_1())


if __name__ == '__main__':
    main()
