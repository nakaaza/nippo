# How to start nippo!
## Install daisyUI
ref: [Install daisyUI for Django](https://daisyui.com/docs/install/django/?lang=ja)

1. Run the following commands on terminal app.

```bash
# Your current directory must be `nippo!`
curl -sLo static/css/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
curl -sLo static/css/tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-x64
chmod +x static/css/tailwindcss
curl -sLo static/css/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js
curl -sLo static/css/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js
```

2. Create `static/css/input.css` and add the follwowing code.

```css
@import "tailwindcss" source(none);
@plugin "./daisyui.js";
@source "../../templates";
```

3. Run the Tailwind CSS executable to generate output.css
```bash
static/css/tailwindcss -i static/css/input.css -o static/css/output.css --watch
```

 ## Install packages
 ```bash
 python3 -m pip install -r requirements.txt
 ```

 ## Start the Django server
 ```bash
 python3 manage.py migrate
 python3 manage.py runserver
 ```