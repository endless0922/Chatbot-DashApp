import json

import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

# import components
from components.navbar import render_navbar
from components.input import render_chat_input

import pages.chatbot.chatbot_controller as chatbot_controller

# define layout
chatbot_layout = html.Div(
    id="display-conversation",
    style={
        "height": "100%",
        "display": "flex",
        "flex-direction": "column",
        "overflow-y": "auto",
        "color": "#f1f1f1",
    },
)


def render_chatbot():
    with open("././context.json", "r") as file:
        context_data = json.load(file)
        context = context_data["context"]

        chatbot_controller.message_history.append(
            {"role": "system", "content": context}
        )
    return html.Div(
        [
            render_navbar(brand_name="AI Chatbot"),
            html.Br(),
            dcc.Store(id="store-conversation", data=""),
            html.Div(id="dummy-output", style={"display": "none"}),
            dbc.Container(
                fluid=True,
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                width=10,
                                children=dbc.Card(
                                    [
                                        dbc.CardBody(
                                            [
                                                chatbot_layout,
                                                html.Div(
                                                    render_chat_input(),
                                                    style={
                                                        "width": "100%",
                                                        "height": "3rem",
                                                        "display": "flex",
                                                        "justify-content": "center",
                                                        "gap": "1rem",
                                                    },
                                                ),
                                                dbc.Spinner(
                                                    html.Div(id="loading-component")
                                                ),
                                            ],
                                            style={
                                                "border-radius": 25,
                                                "background": "#FFFFFF",
                                                "border": "0px solid",
                                                "display": "flex",
                                                "flex-direction": "column",
                                                "justify-content": "space-between",
                                                "height": "85vh",
                                            },
                                        )
                                    ]
                                ),
                            ),
                        ],
                        style={
                            "display": "flex",
                            "justify-content": "center",
                        },
                    )
                ],
            ),
        ]
    )
