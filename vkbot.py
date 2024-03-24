import vk_api 
import requests

import json

from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType



def main():
    def sections():
        keyboard_sections = VkKeyboard(one_time=True)
        keyboard_sections.add_button('Mobile Legends', color=VkKeyboardColor.POSITIVE)
        keyboard_sections.add_button('LOL', color=VkKeyboardColor.POSITIVE)
        keyboard_sections.add_button('DOTA2', color=VkKeyboardColor.POSITIVE)
        keyboard_sections.add_line()
        keyboard_sections.add_button('SomeGame', color=VkKeyboardColor.POSITIVE)
        keyboard_sections.add_button('Назад', color=VkKeyboardColor.POSITIVE)
        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            message='Выбери интересующую тебя секцию',
            keyboard=keyboard_sections.get_keyboard()
        )
    def head():
        vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Стандартная информация для тех, кто уже много раз заходил. Его не надо приветсвовать. Сюда можно засунуть рандомный факт в киберспорте, анектод или что-то еще',
                keyboard=keyboard_begin.get_keyboard()
            )
    def begin(): 
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='начать':
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard_begin.get_keyboard(),
                    message='Привет. Мы секция киберспорта. Здесь будет начальное сообщение для тех кто вообще мало что знает.',
                        session = requests.Session() 
                )
    def faq():
            keyboard_sections = VkKeyboard(one_time=True)
            keyboard_sections.add_button('Главная', color=VkKeyboardColor.POSITIVE)
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Самые частые вопросы. Как получить зачет? Как получать повышку? Куда идти?',
                keyboard=keyboard_sections.get_keyboard()
            )
    def contacts():
            keyboard_sections = VkKeyboard(one_time=True)
            keyboard_sections.add_button('Главная', color=VkKeyboardColor.POSITIVE)
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Контакты всех главных. К кому и по какому поводу обращаться',
                keyboard=keyboard_sections.get_keyboard()
            )
    
    def MobileLegends():
            keyboard_sections = VkKeyboard(one_time=True)   
            keyboard_sections.add_button('Назад', color=VkKeyboardColor.POSITIVE)
            keyboard_sections.add_button('Главная', color=VkKeyboardColor.POSITIVE)
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message='Все про Mobile Legends',
                keyboard=keyboard_sections.get_keyboard()
            )
        
                    
    tok = "vk1.a.059C8ppH7woEYbGJ25oQmHuoS6ge1fCVtsMEa3sGvPVY-dHGq1iHeFb148YhcAxxG4GLB1mcxlkU5O7QmsyRvmHTWmyBYsYZgVsKbp_CdTgmMHd9-puOFb2-EDQ1rfYV3gbpY6ftwv1jdMAR3rygjFxlvLxH8mGPwKbZeWnVzzuJjeU1ovkaGce5smcC7Tnnta0jCMoAJQkUKyHdldPFkg"
    vk_session = vk_api.VkApi(token=tok)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    
    keyboard_begin = VkKeyboard(one_time=True)
    keyboard_begin.add_button('Секции', color=VkKeyboardColor.SECONDARY)
    keyboard_begin.add_button('FAQ', color=VkKeyboardColor.POSITIVE)
    keyboard_begin.add_button('Контакты', color=VkKeyboardColor.POSITIVE)
    
    for event in longpoll.listen():
        begin()
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='Главная':
            head()
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='Секции':
            sections()   
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='FAQ': 
            faq()
            
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='Контакты': 
            contacts()
            
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='Mobile Legends':
            MobileLegends()
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text=='Назад':
            sections()
            

    
    

    

if __name__ == '__main__':
    main()
    

