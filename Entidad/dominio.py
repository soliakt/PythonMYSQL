class Dominio:
    # Dominio 
    # Representa el nombre de la cuenta
    def __init__(self, id, fechaCreacion, fechaExpiracion, propietario, proveedor, importe):
        self.id = id
        self.fechaCreacion = fechaCreacion
        self.fechaExpiracion = fechaExpiracion
        self.propietario = propietario
        self.proveedor = proveedor
        self.importe = importe

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_fecha_creacion(self):
        return self.fechaCreacion

    def set_fecha_creacion(self, fecha_creacion):
        self.fechaCreacion = fecha_creacion

    def get_fecha_expiracion(self):
        return self.fechaExpiracion

    def set_fecha_expiracion(self, fecha_expiracion):
        self.fechaExpiracion = fecha_expiracion

    def get_propietario(self):
        return self.propietario

    def set_propietario(self, propietario):
        self.propietario = propietario

    def get_proveedor(self):
        return self.proveedor

    def set_proveedor(self, proveedor):
        self.proveedor = proveedor

    def get_importe(self):
        return self.importe

    def set_importe(self, importe):
        self.importe = importe