from django.shortcuts import render
import dominate
import json
from dominate.tags import *
import string
import os.path
import datetime
from git import Repo

def home(request):
    return render(request, "index.html")

def process(request):
    config = json.loads(request.POST["JSONInput"])
    doc = dominate.document(title="Built Webpage")
    with doc.head:
        style("""\
            
            * {
                margin: 0;
                padding: 0;
            }
            body {
                background: url(https://images.unsplash.com/photo-1527071085976-578712baa7d2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1356&q=80);
                background-size: cover;
                background-position: center center;
                color: #2C232A;
                font-family: sans-serif;
                font-size: 16px;
                color: white;
                font-family: 'lato', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            input[type=text], select, textarea, input[type=file], input[type=password], input[type=date], input[type=email], input[type=range], input[type=number] {
                width: 100%;
                padding: 12px 0 12px 0px;
                border: 1px solid #ccc;
                text-indent:12px;
                border-radius: 4px;
                resize: none;
            }

            textarea {
                width: 100%;
                padding: 12px 0 12px 0px;
                border: 1px solid #ccc;
                text-indent:12px;
                border-radius: 4px;
                resize: vertical;
            }

            form {
                width: 55%;
                background-color: rgba(0, 0, 0, 0.5);
                height: auto;
                border-radius: 5px;
                padding: 30px;
            }
            
            div {
                padding: 10px 0 10px 0;
            }

            label {
                padding: 12px 12px 12px 0;
                display: inline-block;
            }

            input[type=submit] {
                background-color: #4CAF50;
                color: white;
                padding: 12px 20px;
                margin: 30px 0 30px 0;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
                font-size: 16px;
            }

            input[type=submit]:hover {
                background-color: #3e8e41;
            }

        """)

        html = form(action="/", method="GET")
        with html:
            for input_config in config['Attributes']:

                if input_config['Type'] == 'select' or input_config['Type'] == 'Dropdown':
                    input_config['Type'] = "select"
                    generate_select_input(input_config)

                elif input_config['Type'] == 'textarea':
                    generate_textarea_input(input_config)

                elif input_config['Type'] == 'radio' or input_config['Type'] == 'checkbox':
                    generate_radio_input(input_config)

                elif input_config['Type'] == 'date':
                    generate_date_input(input_config)

                elif input_config['Type'] == 'number' or input_config['Type'] == 'range':
                    generate_number_input(input_config)

                elif input_config['Type'] == 'SecretTextBox':
                    input_config['Type'] = "password"
                    generate_file_input(input_config)

                elif input_config['Type'] == 'TextBox':
                    input_config['Type'] = "text"
                    generate_file_input(input_config)

                elif input_config['Type'] == 'RadioButton':
                    input_config['Type'] = "radio"
                    generate_radio_input(input_config)

                elif input_config['Type'] == 'file':
                    generate_text_input(input_config)

                else:
                    generate_text_input(input_config)
            input_(_class='button', type='submit',
                   value=config['ActionDisplayName'])
    generate_file(doc)

    return render(request, "result.html", {"result": doc.render()})

def generate_file(doc):
    dir1 = os.path.join(os.getcwd(), 'RenderedFiles')
    date = datetime.datetime.now()
    now = date.strftime("%Y-%m-%d %H-%M-%S")
    dirPath2 = os.path.join(dir1, 'Rendered_Page_')
    dirPath = dirPath2.rstrip('\n')
    filenameCreated = dirPath+now
    a_file = open(filenameCreated + ".html", "w")
    print(doc.render(), file=a_file)
    a_file.close()

    # Git Push
    repo = Repo('./RenderedFiles')
    repo.index.add([filenameCreated + ".html"])
    repo.index.commit('Rendered File Push'+now)
    origin = repo.remote('origin')
    origin.push()

def generate_text_input(input):
    html = div()
    with html:
        label(input['Name'])
        input_(
            type=input['Type'],
            maxlength=input['Size'] if 'Size' in input else '',)
    return html

def generate_file_input(input):
    html = div()
    with html:
        label(input['Name'])
        input_(
            type=input['Type'])
    return html

def generate_date_input(input):
    html = div()
    with html:
        label(input['Name'])
        input_(
            type=input['Type'],
            max=input['Maximum'] if 'Maximum' in input else '',
            min=input['Minimum'] if 'Minimum' in input else '')
    return html

def generate_number_input(input):
    html = div()
    with html:
        label(input['Name'])
        input_(
            type=input['Type'],
            max=input['Maximum'] if 'Maximum' in input else '',
            min=input['Minimum'] if 'Minimum' in input else '',
            step=input['Step'] if 'Step' in input else '')
    return html

def generate_textarea_input(input):
    html = div()
    with html:
        label(input['Name'])
        textarea(rows=input['RowSize'] if 'RowSize' in input else '20',
                 cols=input['ColSize'] if 'ColSize' in input else '60')

    return html

def generate_select_input(input):
    html = div()
    with html:
        label(input['Name'])
        dropdown = select()
        with dropdown:
            for dropdown_options in input['DropdownValues']:
                option(dropdown_options['DisplayValue'],
                       value=dropdown_options['Value'])

    return html

def generate_radio_input(input):
    html = div()
    with html:
        label(input['Name'])
        for radio_options in input['Options']:
            radiobutton = input_(type=input['Type'],
                                 value=radio_options['Value'],
                                 name=input['Name'])
            label(radio_options['DisplayValue'])

    return html