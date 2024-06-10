from pathlib import Path

from typing import Optional

from fastapi.responses import RedirectResponse

from nicegui import Client, app, ui
import Models 





        
def page_init():
    ui.add_css("""
:root {
               background:
radial-gradient(rgba(255,255,255,0) 0, rgba(255,255,255,.15) 30%, rgba(255,255,255,.3) 32%, rgba(255,255,255,0) 33%) 0 0,
radial-gradient(rgba(255,255,255,0) 0, rgba(255,255,255,.1) 11%, rgba(255,255,255,.3) 13%, rgba(255,255,255,0) 14%) 0 0,
radial-gradient(rgba(255,255,255,0) 0, rgba(255,255,255,.2) 17%, rgba(255,255,255,.43) 19%, rgba(255,255,255,0) 20%) 0 110px,
radial-gradient(rgba(255,255,255,0) 0, rgba(255,255,255,.2) 11%, rgba(255,255,255,.4) 13%, rgba(255,255,255,0) 14%) -130px -170px,
radial-gradient(rgba(255,255,255,0) 0, rgba(255,255,255,.2) 11%, rgba(255,255,255,.4) 13%, rgba(255,255,255,0) 14%) 130px 370px,
radial-gradient(rgba(255,255,255,0) 0, rgba(255,255,255,.1) 11%, rgba(255,255,255,.2) 13%, rgba(255,255,255,0) 14%) 0 0,
linear-gradient(45deg, #343702 0%, #184500 20%, #187546 30%, #006782 40%, #0b1284 50%, #760ea1 60%, #83096e 70%, #840b2a 80%, #b13e12 90%, #e27412 100%);
background-size: 470px 470px, 970px 970px, 410px 410px, 610px 610px, 530px 530px, 730px 730px, 100% 100%;
background-color: #840b2a;
               }
               """)
    # ui.query("main.q-page").classes("flex flex-col")
    # ui.query(".nicegui-content").classes("grow flex-center")
    # ui.add_head_html('<link rel="stylesheet" href="asset/main.css">')
    # #LoginUI.build()


@ui.page("/register")
def register():
    ui.page_title("注册")
    with ui.card().classes("h-1/4 sm:w-1/3 items-stretch px-[2.5rem] login-card"):
        ui.label("欢迎登录！").classes("text-h5 text-center text-dark")
        username = ui.input('账号').props("outlined").style("color: rgb(37 99 235)")
        password = ui.input('密码', password=True, password_toggle_button=True).props("outlined")
        password_2 = ui.input('再次输入', password=True, password_toggle_button=True).props("outlined")
        ui.button('注册')
   
    return True
@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    ui.page_title("登录")
    page_init()
    async def try_login() -> None:  # local function to avoid passing username and password as arguments
        if await Models.User.filter(uname = username.value).get("pwd") == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.row().classes("w-full items-stretch absolute-center justify-center"):
        # ui.label("hahah")
        # with ui.column().classes("col-span-5"):
        #with ui.card().classes("h-1/4 sm:w-1/3 items-stretch px-[2.5rem] login-card"):
        with ui.card().classes("items-stretch login-card col-span-8 inset-shadow-down ").style("""
                                                        gap: 20px;
                                                        border-radius: 10px;
                                                        backdrop-filter: blur(19px);
                                                        background-color: rgba(0,191,255, 0.146);
                                                        box-shadow: rgba(0, 0, 0, 0.3) 2px 8px 8px;
                                                        border: 2px rgba(255,255,255,0.4) solid;
                                                        border-bottom: 2px rgba(40,40,40,0.35) solid;
                                                        border-right: 2px rgba(40,40,40,0.35) solid;
                                                                                               """):
            ui.label("欢迎登录！").classes("text-h5 text-center  text-grey-1 ")
            username = ui.input('账号').on('keydown.enter', try_login).props("""outlined rounded dark""").classes(" ")
            password = ui.input('密码', password=True, password_toggle_button=True).on('keydown.enter', try_login).props("outlined rounded dark").classes(" ")
            ui.button('登录', on_click=try_login)
            ui.space()
            ui.link("""还没有账户？点击注册一下""",target="/register").classes("text-h6 text-center text-light-green-8  ")
            ui.markdown()
        #with ui.column().classes("col-span-7"):
        ui.image("./assets/login.jpg").props(""" width=15% """).classes("inset-shadow-down ")
    with ui.footer():
        ui.label("background css is from https://projects.verou.me/css3patterns/#rainbow-bokeh")
    return None



