from flask import Flask, render_template, redirect, url_for, request,session,flash, get_flashed_messages, Response
from models import db, Sucursal,Paquete,Transporte,Repartidor
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\admin\\Desktop\\facuu\\2do año\\codigos\\Unidad 5\\U5\\instance\\datos.sqlite3'
db.init_app(app)
app.config['SECRET_KEY'] = 'nicoygerman'

@app.route('/')
def paginaInicial():
    sucursales = db.session.query(Sucursal).order_by(Sucursal.numero, Sucursal.provincia).all()
    return render_template('Principal.html', sucursales=sucursales)

@app.route('/inicio', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':
        sucursal_id = request.form.get('sucursal_id')
        session['sucursal_id'] = sucursal_id
        return render_template('seleccion.html')
    return render_template('seleccion.html')
@app.route('/despachante')
def despachante():
    return render_template('despachante.html')
@app.route('/registrar_paquete')
def registrar_paquete():
    return render_template('registrar_paquete.html')

@app.route('/guardar_paquete', methods=['POST', 'GET'])
def guardar_paquete():
    if request.method == 'POST':
        try:
            peso = float(request.form.get('peso'))
        except ValueError:
            flash("El peso debe ser un número válido.", "error")
            return redirect(url_for('registrar_paquete'))
        num = 1000 + ((Paquete.query.count() + 2) * 10)
        sucursalid = session.get('sucursal_id')
        nomdestinatario = request.form.get('nomdestinatario')
        dirdestinatario = request.form.get('dirdestinatario')
        if peso and nomdestinatario and dirdestinatario:
            unpaquete = Paquete(numeroenvio=num, peso=peso, nomdestinatario=nomdestinatario,
                                dirdestinatario=dirdestinatario, entregado=False, observaciones="",
                                idsucursal=sucursalid, idtransporte=0, idrepartidor=0)
            db.session.add(unpaquete)
            db.session.commit()
            return render_template('registrar_paquete_exitoso.html')
        else:
            flash("Todos los campos son obligatorios.", "error")
            return redirect(url_for('registrar_paquete'))
    return render_template('registrar_paquete.html')

@app.route('/salidatransporte', methods=['POST','GET'])
def salidatransporte():
    if request.method == 'POST':
        id= int(request.form.get(Sucursal.id))
    sucursales = db.session.query(Sucursal).order_by(Sucursal.numero, Sucursal.provincia).all()
    return render_template('salidatransporte.html', sucursales=sucursales)
@app.route('/paquetesSinEntregar/<int:sucursalid>', methods=['GET', 'POST'])
def paquetesSinEntregar(sucursalid):
    sucursal = Sucursal.query.get_or_404(sucursalid)
    paquetes = Paquete.query.filter_by(idsucursal=sucursalid, entregado=False, idtransporte = False).all()
    transportes = Transporte.query.filter_by(idsucursal=sucursalid).all()
    if request.method == 'POST':
        paquetes_seleccionados = request.form.getlist('paquete')
        try:    
           numerotransporte = int(request.form.get('numerotransporte'))
        except ValueError:
            mensaje_error = "El Numero del transporte debe de ser un numero"
            return render_template('errorregistro.html', mensaje = mensaje_error)
        if not paquetes_seleccionados:
            mensaje_error = "Error: Debes seleccionar al menos un paquete para registrar el transporte."
            return render_template('errorregistro.html', mensaje=mensaje_error)
        try:
            nuevotransporte = Transporte(numerotransporte=numerotransporte,
                                         fechahorasalida=datetime.now(),
                                         idsucursal=sucursalid)
            db.session.add(nuevotransporte)
            db.session.commit()
            for paquete_id in paquetes_seleccionados:
                paquete = Paquete.query.get(int(paquete_id))
                paquete.idtransporte = nuevotransporte.id 
            db.session.commit()
            return render_template('exitoregistro.html', mensaje="Transporte registrado exitosamente!")
        except Exception as e:
            db.session.rollback()
            mensaje_error = f"Error en el registro del transporte: {str(e)}"
            return render_template('errorregistro.html', mensaje=mensaje_error)
    return render_template('paquetesSinEntregar.html', sucursal=sucursal, paquetes=paquetes, transportes=transportes)

@app.route('/llegadatransporte', methods=['POST', 'GET'])
def llegadatransporte():
    if 'sucursal_id' in session:
        sucursalid = session['sucursal_id']
        transportes = Transporte.query.filter_by(idsucursal=sucursalid, fechahorallegada=None).all()
        if request.method == 'POST':
            transporte_id = request.form.get('transporte_id')
            transporte = Transporte.query.get(transporte_id)
            if transporte:
                try:
                    transporte.fechahorallegada = datetime.now()
                    db.session.commit()
                    flash('Se ha registrado la llegada del transporte de forma exitosa')
                    return redirect(url_for('llegadatransporte'))
                except Exception as e:
                    db.session.rollback()
                    flash(str(e),'error')
            else:
                flash('Transporte no encontrado','error')
        return render_template('llegadatransporte.html', transportes=transportes,mensajes=get_flashed_messages())
    else:
        return redirect(url_for('paginaInicial'))
@app.route('/Asignar_paquetes', methods=['GET', 'POST'])
def asignar_paquete():
    if request.method == 'POST':
        repartidor_id = request.form.get('repartidor_id')
        paquetes_seleccionados = request.form.getlist('paquetes[]')

        for num_envio in paquetes_seleccionados:
            paquete = Paquete.query.filter_by(numeroenvio=num_envio).first()
            if paquete:
                paquete.idrepartidor = repartidor_id
                db.session.commit()

        return render_template('asignar_paquete_exitosamente.html')
    else:
        sucursalid = session.get('sucursal_id')
        if not sucursalid:
            return "Error: No se ha establecido una sucursal."

        repartidores = Repartidor.query.filter_by(idsucursal=sucursalid).all()
        paquetes = Paquete.query.filter_by(idrepartidor=0, entregado=False, idsucursal=sucursalid).all()

        return render_template('asignar_paquetes.html', repartidores=repartidores, paquetes=paquetes)

@app.route('/repartidor_Login', methods=['GET','POST'])
def repartidor_Login():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        dni = request.form.get('dni')
        repartidor = Repartidor.query.filter_by(nombre=nombre, dni=dni).first()
        if repartidor:
            session['repartidor_id'] = repartidor.id
            return redirect(url_for('repartidormenu'))
        else:
            return render_template('repartidor_login_error.html')
    return render_template('repartidor_Login.html')

@app.route('/repartidormenu')
def repartidormenu():
    if 'repartidor_id' in session:
        repartidor = Repartidor.query.get(session['repartidor_id'])
        return render_template('repartidormenu.html', repartidor=repartidor)
    else:
        flash('Por favor, inicia sesión para acceder')
        return redirect(url_for('repartidor_Login'))

@app.route('/ingresarpaquete', methods=['GET', 'POST'])
def ingresarpaquete():
    if 'repartidor_id' not in session:
        return redirect(url_for('repartidor_Login'))
    error = None
    if request.method == 'POST':
        numeroenvio = request.form.get('numeroenvio')
        paquete = Paquete.query.filter_by(numeroenvio=numeroenvio, idrepartidor=session['repartidor_id']).first()
        if paquete:
            if not paquete.entregado:
                session['paquete_id'] = paquete.id
                return redirect(url_for('entregarpaquete'))
            else:
                error = "El paquete ya ha sido entregado"
        else:
            error = "Paquete no encontrado o no asignado a este repartidor"
    return render_template('ingresarpaquete.html', error=error)

@app.route('/entregarpaquete', methods=['GET', 'POST'])
def entregarpaquete():
    if 'repartidor_id' not in session:
        return redirect(url_for('repartidor_Login'))
    paquete = Paquete.query.get_or_404(session.get('paquete_id'))
    if request.method == 'POST':
        estado = request.form.get('estado')
        observaciones = request.form.get('observaciones')
        paquete.entregado = estado == 'Entregado'
        paquete.observaciones = observaciones
        db.session.commit()
        if paquete.entregado:
            flash('Se ha registrado la entrega del paquete de forma exitosa')
        else:
            flash('Se ha registrado la causa de por qué no se ha entregado el paquete')

        return redirect(url_for('ingresarpaquete'))
    return render_template('entregarpaquete.html', paquete=paquete)
@app.route('/salir')
def salir():
    session.pop('repartidor_id', None)
    response = redirect(url_for('repartidor_Login'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == "__main__":
   with app.app_context():
      db.create_all()
   app.run(debug=True)