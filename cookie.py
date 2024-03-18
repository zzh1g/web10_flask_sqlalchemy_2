from flask import Flask, make_response, request, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 60 сек")
        res.set_cookie("visits_count", '1',
                       max_age=60)
    return res


@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()



