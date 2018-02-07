# Django Music

### Cara menginstall Aplikasi Music ?

1. Klon aplikasi `$ git clone <repository-url>` atau download

2. Buatlah sebuah virtual environment pada root directory `$ virtualenv env`.

3. Aktifkan virtual environment `$ source env/bin/activate` (Linux dan OSX) atau `C:\Documents\DjangoMusic>env\Scripts\activate` (Windows)

4. Install seluruh dependency  `pip install -r requirements.txt`

5. Migrasikan aplikasi `(env) $ DjangoMusic python website/manage.py migrate` (Linux dan OSX) atau `(env) C:\Documents\DjangoMusic>python website\manage.py migrate` (Windows)

6. Jalankan aplikasi `(env) $ DjangoMusic python website/manage.py runserver` (Linux dan OSX) atau `(env) C:\Documents\DjangoMusic>python website\manage.py runserver` (Windows)
