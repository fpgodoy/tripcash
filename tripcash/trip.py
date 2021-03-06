from flask import (Blueprint, blueprints, flash, g, redirect, render_template,
                   request, session, url_for)
from werkzeug.exceptions import abort

from tripcash.auth import login_required
from tripcash.db import get_db

bp = Blueprint('trip', __name__)


@bp.route('/trip', methods=('GET', 'POST'))
@login_required
def trip():
    # Get the data
    db = get_db()
    db.execute('SELECT * FROM trip WHERE user_id=%s', (g.user['id'],))
    trip_list = db.fetchall()

    if request.method == 'POST':
        author = session.get('user_id')
        trip = request.form['trip_name'].strip()
        error = None

        # Ensure the typed trip is a new trip
        checktrip = []
        for row in trip_list:
            checktrip.append(row['trip_name'].upper())

        if not trip:
            error = 'Need to fill the trip name.'

        if trip.upper() in checktrip:
            error = f'Trip {trip} is already registered.'

        # Insert the trip on the DB
        if error is None:
            db.execute(
                'INSERT INTO trip (user_id, trip_name) VALUES (%s, %s)',
                (author, trip),
            )
            g.db.commit()

            return redirect(url_for('trip.trip'))

        flash(error)

    return render_template('trip.html', trips=trip_list)


# Edit the name of a registered trip
@bp.route('/<int:id>/edittrip', methods=('GET', 'POST'))
@login_required
def edittrip(id):

    trip = get_trip(id)

    db = get_db()
    db.execute('SELECT trip_name FROM trip WHERE user_id=%s', (g.user['id'],))
    trip_list = db.fetchall()

    if request.method == 'POST':
        user = session.get('user_id')
        trip = request.form['trip_name'].strip()
        error = None

        # Ensure there isn't another trip with the same name and validate the data
        checktrip = []
        for row in trip_list:
            checktrip.append(row[0].upper())

        if not trip:
            error = 'Need to fill the new label name.'

        if trip.upper() in checktrip:
            error = f'Trip {trip} is already registered.'

        # Update the trip name on the DB
        if error is None:
            db.execute(
                'UPDATE trip SET trip_name = %s WHERE trip_id = %s', (trip, id)
            )
            g.db.commit()

            return redirect(url_for('trip.trip'))

    return render_template('edittrip.html', trips=trip_list, trip=trip)


# Delete a registered trip
@bp.route('/<int:id>/deletetrip', methods=('POST',))
@login_required
def deletetrip(id):
    # Get the data
    trip = get_trip(id)
    db = get_db()

    # Get the current trip
    db.execute('SELECT current_trip FROM users WHERE id = %s', (g.user['id'],))
    currentrip = db.fetchone()

    # Delete the trip and all its expenses
    db.execute('DELETE FROM trip WHERE trip_id = %s', (id,))
    db.execute('DELETE FROM post WHERE trip = %s', (id,))
    
    # Check if the deleted trip is the current one and clear the current trip if it is
    if trip['trip_id'] == currentrip[0]:
        db.execute(
            'UPDATE users SET current_trip=NULL WHERE id=%s', (g.user['id'],)
        )
    g.db.commit()

    return redirect(url_for('trip.trip'))


# Get the clicked button trip
def get_trip(id):
    db = get_db()
    db.execute('SELECT * FROM trip WHERE trip_id = %s', (id,))
    trip = db.fetchone()

    if trip is None:
        abort(404, "This trip doesn't exist.")

    if trip['user_id'] != g.user['id']:
        abort(403)

    return trip
