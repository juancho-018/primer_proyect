import datetime
import random
from flask import Blueprint, request, jsonify, flash
from app.models.pedido import Pedido
from app.models.venta import Venta
from app.models.cliente import Cliente
from app.models.producto import Producto
from app import db

compra_bp = Blueprint('compra', __name__)

@compra_bp.route('/simular_compra', methods=['POST'])
def simular_compra():
    data = request.get_json() or {}
    items = data.get('items', [])
    
    if not items:
        return jsonify({'status': 'error', 'message': 'El carrito está vacío'}), 400

    try:
        # Calcular totales
        total_items = sum(item.get('cantidad', 1) for item in items)
        monto_total = sum(item.get('precio_num', 0) * item.get('cantidad', 1) for item in items)
        valor_formateado = f"${monto_total:,.0f}".replace(',', '.')

        # Obtener o asignar un cliente por defecto
        cliente = Cliente.query.first()
        cod_cli = cliente.cod_cli if cliente else 1

        # Generar código único para el pedido y la venta
        cod_pe = random.randint(100, 99999)
        while Pedido.query.get(cod_pe):
            cod_pe = random.randint(100, 99999)

        # 1. Crear el Pedido en la base de datos
        nuevo_pedido = Pedido(
            cod_pe=cod_pe,
            f_pe=datetime.date.today(),
            cant_pe=total_items,
            vt_pe=valor_formateado,
            cod_cli1=cod_cli
        )
        db.session.add(nuevo_pedido)
        db.session.flush()  # Para asegurar que la transacción tenga el ID generado

        # 2. Registrar cada producto en la tabla de Ventas
        ventas_creadas = []
        for item in items:
            cod_p = item.get('cod_p')
            if cod_p:
                cod_ven = random.randint(100, 99999)
                while Venta.query.get(cod_ven):
                    cod_ven = random.randint(100, 99999)
                
                nueva_venta = Venta(
                    cod_ven=cod_ven,
                    cod_pe1=cod_pe,
                    cod_p1=cod_p
                )
                db.session.add(nueva_venta)
                ventas_creadas.append(cod_ven)

        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': '¡Compra realizada con éxito y registrada en la base de datos!',
            'pedido_id': cod_pe,
            'total_items': total_items,
            'monto_total': valor_formateado,
            'ventas_count': len(ventas_creadas)
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'Error procesando la compra en BD: {str(e)}'}), 500
