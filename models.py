from django.db import models

# -----------------------------
# CATEGORÍA
# -----------------------------
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


# -----------------------------
# PRODUCTO
# -----------------------------
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre_producto


# -----------------------------
# PROVEEDOR
# -----------------------------
class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre


# -----------------------------
# CLIENTE
# -----------------------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre


# -----------------------------
# EMPLEADO
# -----------------------------
class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre


# -----------------------------
# COMPRA A PROVEEDOR
# -----------------------------
class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra {self.id} - {self.proveedor.nombre}"


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre_producto} x {self.cantidad}"


# -----------------------------
# VENTA
# -----------------------------
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venta {self.id} - {self.fecha.date()}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.producto.nombre_producto} x {self.cantidad}"
