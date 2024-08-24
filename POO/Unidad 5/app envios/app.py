from datetime import datetime
from flask import Flask, request, render_template, session
from models import db, paquete, repartidor, sucursal, transporte

app=Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def inicio():
	return render_template('inicio.html', sucursales=sucursal.query.order_by(sucursal.numero).all())

@app.route('/menu', methods=['POST', 'GET'])
def menu():
	if request.method=='POST':
		sucursalId=request.form.get('id')
		session['sucursalId']=sucursalId
		return render_template('menu.html')
	return render_template('menu.html')

@app.route('/recepcion')
def recepcion():
	return render_template('recepcion.html')

@app.route('/paqueteRegistrado', methods=['POST', 'GET'])
def registro():
	if request.method=='POST':
		try:
			peso=float(request.form.get('peso'))
		except ValueError:
			return render_template('error.html', error="Los datos ingresados no son correctos...")
		if peso<0:
			return render_template('error.html', error="Los datos ingresados no son correctos...")
		else:
			paq1=paquete(numeroenvio=1000+(paquete.query.count()+2*10), peso=peso, nomdestinatario=request.form.get('nom'), dirdestinatario=request.form.get('dir'), entregado=False, observaciones="", idsucursal=session.get('sucursalId'), idtransporte=0, idrepartidor=0)
			db.session.add(paq1)
			db.session.commit()
			return render_template('aviso.html', aviso="El paquete se registró exitosamente!")
	return render_template('recepcion.html')

@app.route('/salida', methods=['POST', 'GET'])
def salida():
	return render_template('salida.html', sucursales=sucursal.query.order_by(sucursal.numero).all())

@app.route('/noEntregados/<int:sucursalId>', methods=['POST', 'GET'])
def noEntregados(sucursalId):
	if request.method=='POST':
		if not request.form.getlist('paquetes'):
			return render_template('error.html', error="No se seleccionó ningún paquete")
		else:
			trans1=transporte(numerotransporte=214+(transporte.query.count()), fechahorasalida=datetime.now(), fechahorallegada=None, idsucursal=sucursalId)
			db.session.add(trans1)
			db.session.commit()
			for paqueteId in request.form.getlist('paquetes'):
				paquete1=paquete.query.get(int(paqueteId))
				paquete1.idtransporte=trans1.id 
			db.session.commit()
			return render_template('aviso.html', aviso="Registrado exitosamente!")
	return render_template('noEntregados.html', paquetes=paquete.query.filter_by(idsucursal=sucursalId, entregado=False, idtransporte = False).all())

@app.route('/llegada', methods=['POST', 'GET'])
def llegada():
	if request.method=='POST':
		if not request.form.get('id'):
			return render_template('error.html', error="No se seleccionó ningún transporte")
		else:
			trans1=transporte.query.get(request.form.get('id'))
			trans1.fechahorallegada=datetime.now()
			db.session.commit()
			return render_template('aviso.html', aviso="Registrado exitosamente!")
	return render_template('llegada.html', transportes=transporte.query.filter_by(idsucursal=session.get('sucursalId'), fechahorallegada=None).all())

if __name__=='__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True)