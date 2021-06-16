# Dynamic Webpage Builder

A web application framework to dynamically render template-driven web
pages based on the metadata JSON and push the source code to git.

## Technologies Used:
Python, Django, HTML, CSS, JavaScript

## Packages Used:
Dominate and GitPython

## Sample Input 1:

```
{
  "ActionDisplayName":"Login",
  "Attributes":[
    {
      "Name": "Username",
      "Size": "10",
      "Type": "TextBox"
    },
    {
      "Name": "Password",
      "Size": "10",
      "Type": "SecretTextBox"
    },
    {
      "DropdownValues": [
        {
          "DisplayValue": "Guest",
          "Value": "guest"
        },
        {
          "DisplayValue": "Admin",
          "Value": "admin"
        }
      ],
      "Name": "UserType",
      "Type": "Dropdown"
    }
  ]
}
```

## Sample Output 1:

![Sample Output 1](https://user-images.githubusercontent.com/33464442/121712976-f3bf4c80-caf9-11eb-98d0-b915a94674bd.png)

## Sample Input 2:

```
{
  "ActionDisplayName":"Submit",
  "Attributes":[
    {
      "Name": "Name",
      "Size": "10",
      "Type": "text"
    },
    {
      "Name": "Gender",
      "Options": [
        {
          "DisplayValue": "Male",
          "Value": "male"
        },
        {
          "DisplayValue": "Female",
          "Value": "female"
        }
      ],
      "Type": "RadioButton"
    }
  ]
}
```

## Sample Output 2:

![Sample Output 2](https://user-images.githubusercontent.com/33464442/121713223-40a32300-cafa-11eb-9d96-1399a68c2d58.png)

## Setting up the environment:

Create a repository named RenderedFiles.

Clone it in the DynamicWebpageBuilder folder

In the project directory, you can run:

```
py manage.py runserver
```

It runs the app in the development mode.
Open http://localhost:8000 to view it in the browser.

Generate Dynamic Webpages with JSON!
