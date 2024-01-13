import streamlit as st
import streamlit.components.v1 as components


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.markdown('''
<!-- 

GRADIENT BANNER DESIGN BY SIMON LURWER ON DRIBBBLE:
https://dribbble.com/shots/14101951-Banners

-->
<div class="main-container">
  <div class="heading">
    <h1 class="heading__title">Gradient Banner Cards</h1>
    <p class="heading__credits"><a class="heading__link" target="_blank" href="https://dribbble.com/sl">Design by Simon Lurwer on Dribbble</a></p>
  </div>
  <div class="cards">
    <div class="card card-1">
      <div class="card__icon"><i class="fas fa-bolt"></i></div>
      <p class="card__exit"><i class="fas fa-times"></i></p>
      <h2 class="card__title">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</h2>
      <p class="card__apply">
        <a class="card__link" href="#">Apply Now <i class="fas fa-arrow-right"></i></a>
      </p>
    </div>
    <div class="card card-2">
      <div class="card__icon"><i class="fas fa-bolt"></i></div>
      <p class="card__exit"><i class="fas fa-times"></i></p>
      <h2 class="card__title">Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h2>
      <p class="card__apply">
        <a class="card__link" href="#">Apply Now <i class="fas fa-arrow-right"></i></a>
      </p>
    </div>
    <div class="card card-3">
      <div class="card__icon"><i class="fas fa-bolt"></i></div>
      <p class="card__exit"><i class="fas fa-times"></i></p>
      <h2 class="card__title">Ut enim ad minim veniam.</h2>
      <p class="card__apply">
        <a class="card__link" href="#">Apply Now <i class="fas fa-arrow-right"></i></a>
      </p>
    </div>
    <div class="card card-4">
      <div class="card__icon"><i class="fas fa-bolt"></i></div>
      <p class="card__exit"><i class="fas fa-times"></i></p>
      <h2 class="card__title">Quis nostrud exercitation ullamco laboris nisi.</h2>
      <p class="card__apply">
        <a class="card__link" href="#">Apply Now <i class="fas fa-arrow-right"></i></a>
      </p>
    </div>
    <div class="card card-5">
      <div class="card__icon"><i class="fas fa-bolt"></i></div>
      <p class="card__exit"><i class="fas fa-times"></i></p>
      <h2 class="card__title">Ut aliquip ex ea commodo consequat. Duis aute irure dolor.</h2>
      <p class="card__apply">
        <a class="card__link" href="#">Apply Now <i class="fas fa-arrow-right"></i></a>
      </p>
    </div>
    <div class="card card-1">
      <div class="card__icon"><i class="fas fa-bolt"></i></div>
      <p class="card__exit"><i class="fas fa-times"></i></p>
      <h2 class="card__title">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</h2>
      <p class="card__apply">
        <a class="card__link" href="#">Apply Now <i class="fas fa-arrow-right"></i></a>
      </p>
    </div>
  </div>
</div>
'''
, unsafe_allow_html=True)