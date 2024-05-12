import streamlit as st
import requests


def main():
    st.title("IPアドレス取得")
    
    # ユーザーのIPアドレスを取得
    ip_address = requests.get('https://api.ipify.org').text
    
    st.write("あなたのIPアドレスは {} です。".format(ip_address))


if __name__ == '__main__':
    main()
