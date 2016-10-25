import os
from sqlite3 import OperationalError
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from datetime import datetime

app = Flask(__name__, template_folder='./templates')

config = {
    #DATABASE=os.path.join(app.root_path, 'injection.db'),
    'DATABASE': '/tmp/tablice.sqlite3',
    'DEBUG': True,
    'SECRET_KEY': 'skrivnost_za_naso_sejo',
    'USERNAME': 'admin',
    'PASSWORD': 'pass'
}

app.config.update(config)



DROP_TABLE = '''
    DROP TABLE IF EXISTS tablice;
'''

CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS tablice (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      stevilka TEXT not NULL,
      prekrsek TEXT NOT NULL,
      casovni_zig TEXT NOT NULL
    );
''';

POPULATE_DB = '''
    INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-SZ-001', '2016-11-15 08:15:00', 'Hitrost: 213km/h');
    INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-BORIS', '2016-11-15 08:17:00', 'Hitrost: 180km/h');
    INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-ANA', '2016-11-15 08:22:00', 'Hitrost: 156km/h');
    INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-KS-008', '2016-11-15 08:55:00', 'Hitrost: 140km/h');
    INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('MB-JB-007', '2016-11-15 09:40:00', 'Hitrost: 191km/h');
''';

QUERY_TABLICE = '''
    SELECT * FROM tablice ORDER BY casovni_zig, id;
''';


# Inicializacija podatkovne baze.
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.before_first_request
def init_db():
    db = get_db()
    print(DROP_TABLE)
    db.executescript(DROP_TABLE + CREATE_TABLE + POPULATE_DB)
    print(DROP_TABLE + CREATE_TABLE + POPULATE_DB)
    db.commit()
    print('Populated DB ...')

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods=['GET', ])
def pokazi_vse():
    db = get_db()

    db.executescript(CREATE_TABLE)
    cur = db.execute('SELECT * FROM tablice ORDER BY casovni_zig, id;')
    tablice = cur.fetchall()
    return render_template('tablice.html', tablice=tablice)


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj_tablico():
    if request.method != 'POST':
        return render_template('tablica.html')

    if not request.form['tablica'] or not request.form['prekrsek']:
        flash('Neveljaven vnos!', 'danger')
        return render_template('tablica.html')

    stevilka = request.form['tablica']
    prekrsek = request.form['prekrsek']
    casovni_zig = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db = get_db()
    SQL_STAVEK = '''
        INSERT INTO tablice (casovni_zig, stevilka, prekrsek) VALUES ("{}", "{}", "{}");
    '''.format(casovni_zig, stevilka, prekrsek)
    try:
        db.executescript(SQL_STAVEK)
    except OperationalError:
        pass

    flash(SQL_STAVEK, 'info')
    return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
